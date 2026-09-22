walberla_link_files_to_builddir (*.prm)

waLBerla_generate_target_from_python (
    NAME AcousticWaveExampleCodeGen
    FILE AcousticWaveExample.py
    OUT_FILES AcousticWaveExampleStorageSpecification.h
              AcousticWaveExampleStorageSpecification.cpp
              AcousticWaveExampleSweepCollection.h
              AcousticWaveExampleSweepCollection.cpp
              AcousticWaveExampleBoundaryCollection.h
              InfoHeader.h
)

add_executable (AcousticWaveExample AcousticWaveExample.cpp)
target_link_libraries (
    AcousticWaveExample
    walberla::blockforest
    walberla::boundary
    walberla::core
    walberla::domain_decomposition
    walberla::field
    walberla::geometry
    walberla::lbm_generated
    walberla::timeloop
    walberla::vtk
    AcousticWaveExampleCodeGen
)