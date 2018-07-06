WESTH5_FILE=$1
## assignment first, need to assign to original voronoi bins
w_assign -W $WESTH5_FILE --states-from-file states_8dims.yaml || exit 1
## then we need to calculate transition matrix
python make_transMat.py $WESTH5_FILE assign.h5 tm.npy || exit 1
## use PCCA+ to get the coarse grained system
python make_pcca.py tm.npy assign.h5 4 || exit 1
echo "1 2" > data_to_pull.txt
w_pdist -W $WESTH5_FILE -o pdist.h5 -b 30 --construct-dataset assignment.pull_data
rm data_to_pull.txt
plothist average --title "Conc A vs Conc B" --plot-contour --range 0,10 --first-iter 10 --last-iter 100 -o a_b.png pdist.h5 0:0,35:"[A]" 1:0,35:"[B]"
