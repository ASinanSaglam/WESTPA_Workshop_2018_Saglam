import numpy as np
import pickle, sys
from westpa.binning import NopMapper, RectilinearBinMapper

index_dtype = np.uint16

# CUSTOM CLUSTERER
class wrapped_clusterer(NopMapper):
    def __init__(self, clusterer):
        super(NopMapper,self).__init__()
        self.predictor = clusterer
        self.labels = [0,1,2,3]
        self.nbins = 4
        
    def assign(self, coords, mask=None, output=None):
        assigned = np.array(self.predictor.predict(coords), dtype=index_dtype)
        try:
            output[...] = assigned[...]
        except:
            pass
        return assigned 

def assign_cluster():
    print("making the wrapped clusterer")
    WClusterer = wrapped_clusterer(clusterer)
    return WClusterer
# CUSTOM CLUSTERER

# CUSTOM PLOTTING OPTIONS
def avg(hist, midpoints, binbounds):
    import matplotlib.pyplot as plt
    plt.xlabel('Protein A concentration')
    plt.ylabel('Protein B concentration') 
    plt.xlim((0,30))
    plt.ylim((0,30))
# CUSTOM PLOTTING OPTIONS

# PULLING SPECIFIC PCOORDS
def pull_data(n_iter, iter_group):
    '''
    This function reshapes the progress coordinate and 
    auxiliary data for each iteration and retuns it to
    the tool.
    '''
    data_to_pull = np.loadtxt("data_to_pull.txt") - 1
    d1, d2 = data_to_pull 
    pcoord  = iter_group['pcoord'][:,:,[d1,d2]]
    return pcoord
# PULLING SPECIFIC PCOORDS

# LOADING A SPECIFIC MAPPER
def load_mapper(file_name, iter_no=None):
    import h5py, pickle, IPython
    h = h5py.File(file_name, 'r')
    topol_grp = h['bin_topologies']
    if iter_no == None:
        iter_no = h.attrs['west_current_iteration']
    hashval = h['iterations/iter_%08d'%(iter_no)].attrs['binhash']

    index = topol_grp['index']
    pickles = topol_grp['pickles']
    n_entries = len(index)

    for istart in xrange(0,n_entries,chunksize):
        chunk = index_ds[istart:min(istart+chunksize,n_entries)]
        for i in xrange(len(chunk)):
            if chunk[i]['hash'] == hashval:
                pkldat = bytes(pickle_ds[istart+i,0:chunk[i]['pickle_len']].data)
                mapper = pickle.loads(pkldat) 
                return mapper
# LOADING A SPECIFIC MAPPER
