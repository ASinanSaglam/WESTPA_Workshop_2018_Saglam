#!/bin/sh
#
# env.sh
#
# This script defines environment variables that are used by other shell
# scripts, both when setting up the simulation and when running the simulation.
#

################################ BNGL #######################################
export BNG_PL="/home/boltzmann/apps/BioNetGen-2.3.1/BNG2.pl"
export RunNet="/home/boltzmann/apps/BioNetGen-2.3.1/bin/run_network"
export timeTaken="/home/boltzmann/apps/time_mili.sh"

############################## Python and WESTPA ###############################
# Next inform WESTPA what python it should use.  
export WEST_PYTHON=$(which python2.7)

# Check to make sure that the environment variable WEST_ROOT is set. 
# Here, the code '[ -z "$WEST_ROOT"]' will return TRUE if WEST_ROOT is not set,
# causing us to enter the if-statement, print an error message, and exit.
if [ -z "$WEST_ROOT" ]; then
  echo "The environment variable WEST_ROOT is not set."
  echo "Try running 'source westpa.sh' from the WESTPA installation directory"
fi

# Explicitly name our simulation root directory.  Similar to the statement 
# above, we check if the variable is not set.  If the variable is not set,
# the we set it 
export WEST_SIM_ROOT="$PWD"

# Set the simulation name.  Whereas "WEST_SIM_ROOT" gives us the entire 
# absolute path to the simulation directory, running the "basename" command
# will give us only the last part of that path (the directory name).
export SIM_NAME=$(basename $WEST_SIM_ROOT)
#export SCRATCH=/dev/shm
