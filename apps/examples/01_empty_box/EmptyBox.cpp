//======================================================================================================================
//  EmptyBox.cpp - Step 1: Just create the domain
//======================================================================================================================

#include "blockforest/all.h"
#include "core/all.h"
#include "domain_decomposition/all.h"
#include "field/all.h"
#include "timeloop/all.h"

#include "gen/EmptyBox.hpp"

using namespace walberla;

int main(int argc, char** argv)
{
    Environment env(argc, argv);
    auto config = env.config();

    // ============================================================
    // STEP 1: CREATE THE DOMAIN (THE BOX)
    // ============================================================
    auto blocks = blockforest::createUniformBlockGridFromConfig(config);
    auto domain = blocks->getDomain();

    WALBERLA_LOG_INFO_ON_ROOT("========================================")
    WALBERLA_LOG_INFO_ON_ROOT("Empty Box Simulation")
    WALBERLA_LOG_INFO_ON_ROOT("========================================")
    WALBERLA_LOG_INFO_ON_ROOT("Domain: " << domain)
    WALBERLA_LOG_INFO_ON_ROOT("Number of blocks: " << blocks->getNumberOfBlocks())

    // ============================================================
    // STEP 2: CREATE FIELDS
    // ============================================================
    auto pdfs = field::addToStorage< PdfField_T >(blocks, "pdfs", 0.0, field::fzyx);
    auto density = field::addToStorage< ScalarField_T >(blocks, "density", 1.0, field::fzyx);
    auto velocity = field::addToStorage< VelocityField_T >(blocks, "velocity", 0.0, field::fzyx);

    WALBERLA_LOG_INFO_ON_ROOT("Fields created: pdfs, density, velocity")

    // ============================================================
    // STEP 3: DONE!
    // ============================================================
    WALBERLA_LOG_INFO_ON_ROOT("========================================")
    WALBERLA_LOG_INFO_ON_ROOT("Empty box created successfully!")
    WALBERLA_LOG_INFO_ON_ROOT("Next step: Add fluid (LBM) in this box")
    WALBERLA_LOG_INFO_ON_ROOT("========================================")

    return EXIT_SUCCESS;
}