import sympy as sp 
import pystencils as ps

from lbmpy import LBMConfig, LBMOptimisation, LBStencil, Method, Stencil
from lbmpy.creationfunctions import create_lb_collision_rule, create_lb_method

from pystencils_walberla import CodeGeneration, generate_info_header
from lbmpy_walberla import generate_lbm_package, lbm_boundary_generator

with CodeGeneration() as ctx:
    data_type = "float64" if ctx.double_accuracy else "float32"
    