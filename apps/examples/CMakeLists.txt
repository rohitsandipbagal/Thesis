if(WALBERLA_ENABLE_SWEEPGEN)
    add_subdirectory (DoubleShearLayer)
    add_subdirectory (FlowAroundSphere)
    add_subdirectory (ParallelPlates)
    add_subdirectory (AcousticWave)
    add_subdirectory (01_empty_box)
endif()

if(WALBERLA_BUILD_WITH_CODEGEN)
    add_subdirectory (MeshRefinementExample)
    add_subdirectory (AdaptiveMeshRefinementExample)
endif()

add_subdirectory (TimingPool)
