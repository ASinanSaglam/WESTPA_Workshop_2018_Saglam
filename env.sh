#!/bin/sh
#
# env.sh
#
# This script defines environment variables that are used by other shell
# scripts, both when setting up the simulation and when running the simulation.
#

################################ BNGL #######################################
export WEST_SIM_ROOT="$PWD"
export RunNet="$WEST_SIM_ROOT/bngl_conf/run_network"

############################## Python and WESTPA ###############################
export WEST_PYTHON=$(which python2.7)
export WEST_ROOT=../../../
source $WEST_ROOT/westpa.sh
export SIM_NAME=$(basename $WEST_SIM_ROOT)
