# This file is part of waLBerla. waLBerla is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# waLBerla is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along   #ssfg
# with waLBerla (see COPYING.txt). If not, see <http://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from dataclasses import replace

from lbmpy import (
    LBStencil,
    Stencil,
    LBMConfig,
    Method,
)
from lbmpy.boundaries import NoSlip, UBB, SimpleExtrapolationOutflow, QuadraticBounceBack

from lbmpy.source_terms import SourceTerm   # ← ADD THIS

import sympy as sp
import pystencils as ps

from pystencilssfg  import SourceFileGenerator      
from sweepgen import Sweep, get_build_config
from sweepgen.boundaries import SparseBoundary
from sweepgen.prefabs import LbmBulk

from sweepgen.build_config import DEBUG

DEBUG.use_cpu_default()

with SourceFileGenerator(keep_unknown_argv=True) as sfg:
    Sweep.use_v8core_fields()
    sfg.namespace("FlowAroundSphereExample::gen")

    stencil = LBStencil(Stencil.D3Q19)
    omega = sp.symbols("omega")
    inflow_vel = sp.symbols("inflow_vel")

    base_lbm_config = LBMConfig(
        stencil=stencil,
        method=Method.CUMULANT,
        compressible=True,
        relaxation_rate=omega,
    )

    lbm_bulk = LbmBulk(sfg, "LBM", base_lbm_config)
    sfg.generate(lbm_bulk)

    rho, u = lbm_bulk.rho, lbm_bulk.u

    initial_state_assignments = [
        ps.Assignment(rho(), 1),
        ps.Assignment(u(0), inflow_vel)
    ]

    init_fields = Sweep("IntializeMacroFields", initial_state_assignments)
    sfg.generate(init_fields)

    noSlip = SparseBoundary(NoSlip(name="NoSlip"), lbm_bulk.lb_method, lbm_bulk.pdfs)
    sfg.generate(noSlip)

    qbb = SparseBoundary(QuadraticBounceBack(omega, name="QBB"), lbm_bulk.lb_method, lbm_bulk.pdfs)
    sfg.generate(qbb)

    inflow_velocity = (inflow_vel, 0, 0)
    ubb = SparseBoundary(UBB(inflow_velocity, name="UBB"), lbm_bulk.lb_method, lbm_bulk.pdfs)
    sfg.generate(ubb)

    outflow = SparseBoundary(SimpleExtrapolationOutflow((1, 0, 0), stencil, name="Outflow"), lbm_bulk.lb_method, lbm_bulk.pdfs)
    sfg.generate(outflow)
    # ============================================================
    # ACOUSTIC SOURCE (Monopole) - YOUR THESIS ADDITION
    # ============================================================
    # Define acoustic source parameters
    amplitude = sp.symbols("amplitude")      # Q₀ (source strength)
    frequency = sp.symbols("frequency")      # ω (angular frequency)
    time = sp.symbols("time")                # t (time)

    # Monopole source term: j_i = w_i * Q₀ * sin(ω·t)
    # This is from Chapter 12.3.3 of the textbook
    acoustic_source = SourceTerm(
        stencil=stencil,
        source=(amplitude * sp.sin(frequency * time))  # Q₀ * sin(ω·t)
    )

    # Generate the acoustic source sweep
    acoustic_sweep = Sweep("AcousticSource", acoustic_source)
    sfg.generate(acoustic_sweep)