#!/bin/sh
#
# env.sh
#
# This script defines environment variables that are used by other shell
# scripts, both when setting up the simulation and when running the simulation.
#

################################ BNG ###########################################
export WEST_SIM_ROOT="$PWD"
export RunNet="$WEST_SIM_ROOT/bngl_conf/run_network"

############################## Python and WESTPA ###############################
export WEST_PYTHON=$(which python2.7)
export WEST_ROOT=../../../
source $WEST_ROOT/westpa.sh
export SIM_NAME=$(basename $WEST_SIM_ROOT)

# IF SUBMITTING TO H2P SET THESE EXPLICITLY
# I suggest setting python explicitly if submitting
#export WEST_PYTHON=/PATH/TO/YOUR/PYTHON/anaconda/bin/python
# You have to assign a scratch space on the nodes, otherwise the simulation will 
# slow down since it will have to transfer the data over the network 
#export SCRATCH=$SLURM_SCRATCH
