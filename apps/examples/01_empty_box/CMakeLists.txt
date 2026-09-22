walberla_link_files_to_builddir (*.prm)

waLBerla_generate_target_from_python (
    NAME EmptyBoxCodeGen
    FILE EmptyBox.py
    OUT_FILES EmptyBoxStorageSpecification.h
              EmptyBoxStorageSpecification.cpp
              EmptyBoxSweepCollection.h
              EmptyBoxSweepCollection.cpp
              EmptyBoxBoundaryCollection.h
              InfoHeader.h
)
add_executable (EmptyBox EmptyBox.cpp)
target_link_libraries (
    EmptyBox
    walberla::blockforest
    walberla::boundary
    walberla::core
    walberla::domain_decomposition
    walberla::field
    walberla::geometry
    walberla::lbm_generated
    walberla::timeloop
    walberla::vtk
    EmptyBoxCodeGen
)