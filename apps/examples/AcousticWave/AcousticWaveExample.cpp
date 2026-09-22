//======================================================================================================================
//  AcousticWaveExample.cpp - Step 1: Empty Box
//======================================================================================================================

#include "blockforest/all.h"
#include "core/all.h"
#include "domain_decomposition/all.h"
#include "field/all.h"
#include "timeloop/all.h"
#include "vtk/all.h"

#include "gen/AcousticWaveExample.hpp"

using namespace walberla;

int main(int argc, char** argv)
{
    Environment env(argc, argv);
    auto config = env.config();

    // ============================================================
    // STEP 1: CREATE THE BOX (BlockForest)
    // ============================================================
    auto blocks = blockforest::createUniformBlockGridFromConfig(config);
    auto domainAABB = blocks->getDomain();
    WALBERLA_LOG_INFO_ON_ROOT("Domain: " << domainAABB)
    WALBERLA_LOG_INFO_ON_ROOT("Number of blocks: " << blocks->getNumberOfBlocks())

    // ============================================================
    // STEP 1: DONE!
    // ============================================================
    WALBERLA_LOG_INFO_ON_ROOT("Step 1 complete: Box created successfully")

    return EXIT_SUCCESS;
}