#!/bin/bash
#
# runseg.sh
#
if [ -n "$SEG_DEBUG" ] ; then
  set -x
  env | sort
fi

######################## Set up for running the dynamics #######################
# Set up the directory where data for this segment will be stored.
# appropriately setup if $SCRATCH is set
if [[ -n $SCRATCH ]];then
  mkdir -pv $WEST_CURRENT_SEG_DATA_REF
  mkdir -pv ${SCRATCH}/$WEST_CURRENT_SEG_DATA_REF
  cd ${SCRATCH}/$WEST_CURRENT_SEG_DATA_REF
else
  mkdir -pv $WEST_CURRENT_SEG_DATA_REF
  cd $WEST_CURRENT_SEG_DATA_REF
fi
############################## Run the dynamics ################################
# For BNGL run_network using SSA
# run_network options
# -a: something about tolerance? sets "atol = atof(argv[iarg++])"
# -b: if solver is dense, sets solver to GMRES else sets to GMRES_J
# -c: check steady state sets to 1
# -d: sets solver to DENSE_J? similar to -b
# -e: prints end network
# -f: prints fluxes
# -h: random seed? should be < max int
# -g: group input file? 
# -i: sets t_start, so initial tim
# -j: enables species statistics
# -k: sets remove_zero to 0
# -m: sets propagator to SSA
# -n: saves network every iteration in case it crashes
# -o: sets outpre, prepends every output file with this string
# -p: sets the propagator
# -r: sets rtol
# -s: sets save file to 1
# -t: sets atol=rtol=arg
# -u: sets gillspie update interval
# -v: verbose
# -x: sets the continuation flag to 1
# -z: sets outtime
# -?: ++error?
# -M: max steps set here?
# -I: step interval
# --cdat: 0 surprsesses .cdat output
# --fdat: 0 surpresses .fdat output
# --pla_output: same
# --stop-cond: stopping condition
# Last two numbers are STEP_SIZE and NUMBER_OF_STEPS, in the reference paper these were
# 2 steps and tau was set to 10, so 5 was step size and 2 was number of steps
if [ "$WEST_CURRENT_SEG_INITPOINT_TYPE" = "SEG_INITPOINT_CONTINUES" ]; then
  if [[ -n $SCRATCH ]];then
    cp $WEST_PARENT_DATA_REF/seg_end.net ./parent.net
  else
    ln -sv $WEST_PARENT_DATA_REF/seg_end.net ./parent.net
  fi
  $RunNet -o ./seg -p ssa -h $WEST_RAND16 --cdat 0 --fdat 0 -x -e -g ./parent.net ./parent.net 5000 2
  cat seg.gdat > $WEST_PCOORD_RETURN
elif [ "$WEST_CURRENT_SEG_INITPOINT_TYPE" = "SEG_INITPOINT_NEWTRAJ" ]; then
  if [[ -n $SCRATCH ]];then
    cp $WEST_PARENT_DATA_REF ./parent.net
  else
    ln -sv $WEST_PARENT_DATA_REF ./parent.net
  fi
  $RunNet -o ./seg -p ssa -h $WEST_RAND16 --cdat 0 --fdat 0 -e -g ./parent.net ./parent.net 5000 2
  tail -n -2 seg.gdat > $WEST_PCOORD_RETURN
fi

if [[ -n $SCRATCH ]];then
  cp ${SCRATCH}/$WEST_CURRENT_SEG_DATA_REF/seg_end.net $WEST_CURRENT_SEG_DATA_REF/.
  rm -rf ${SCRATCH}/$WEST_CURRENT_SEG_DATA_REF
fi
