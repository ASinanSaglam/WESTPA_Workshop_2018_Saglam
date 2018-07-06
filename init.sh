#!/bin/bash
#
# init.sh
#

source env.sh

rm -rf traj_segs seg_logs istates west.h5 
mkdir   seg_logs traj_segs 

cp $WEST_SIM_ROOT/bngl_conf/init.net bstates/0.net

BSTATE_ARGS="--bstate-file bstates/bstates.txt"

$WEST_ROOT/bin/w_init \
  $BSTATE_ARGS \
  --segs-per-state 10 \
  --work-manager=threads "$@"
