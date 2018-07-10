import IPython
import pickle, h5py, sys
import numpy as np
import networkx as nx
import pyemma as pe 
import analysis_helper as ahelper

if __name__ == "__main__":
    tm_file = sys.argv[1]
    assign_file = sys.argv[2]
    pcca_cluster_count = sys.argv[3]
    
    tm = np.load(tm_file)
    tm = tm[:,:][:,:]

    stm = ahelper.symmetrize(tm)
    rtm = ahelper.row_normalize(stm)
    
    MSM = pe.msm.MSM(rtm, reversible=True)
    pcca = MSM.pcca(pcca_cluster_count)
    p = pcca.coarse_grained_stationary_probability
    ctm = pcca.coarse_grained_transition_matrix
    mstable_assign = pcca.metastable_assignment
    
    a = h5py.File(assign_file, 'r')
    bin_labels = ahelper.get_bin_labels(a)
    
    print("metastable state 0")
    print(bin_labels[mstable_assign.T==0].mean(axis=0))
    print("metastable state 1")
    print(bin_labels[mstable_assign.T==1].mean(axis=0))
    print("metastable state 2")
    print(bin_labels[mstable_assign.T==2].mean(axis=0))
    print("metastable state 3")
    print(bin_labels[mstable_assign.T==3].mean(axis=0))
    
    state_colors = {0: "#FF00FF", 1: "#0000FF", 2: "#FF0000", 3: "#000000"}
    tm = pcca.transition_matrix
    node_sizes = pcca.stationary_probability*1000
    edge_sizes = tm
    
    G = nx.DiGraph()
    for i in range(tm.shape[0]):
        if node_sizes[i] > 0:
            G.add_node(i, weight=float(node_sizes[i]), color=state_colors[mstable_assign[i]])
    
    for i in range(tm.shape[0]):
        for j in range(tm.shape[1]):
            if i != j:
                if edge_sizes[i][j] > 0:
                    G.add_edge(i, j, weight=float(edge_sizes[i][j]))
    
    nx.write_gml(G, "pcca_full.gml")
    
    tm = pcca.coarse_grained_transition_matrix
    node_sizes = pcca.coarse_grained_stationary_probability*1000
    edge_sizes = tm
    print("coarse tm")
    print(edge_sizes)
    print("coarse probs")
    print(pcca.coarse_grained_stationary_probability)
    
    G = nx.DiGraph()
    for i in range(tm.shape[0]):
        if node_sizes[i] > 0:
            G.add_node(i, weight=float(node_sizes[i]), color=state_colors[i])
    
    for i in range(tm.shape[0]):
        for j in range(tm.shape[1]):
            if i != j:
                if edge_sizes[i][j] > 0:
                    G.add_edge(i, j, weight=float(edge_sizes[i][j]))
    
    nx.write_gml(G, "pcca_coarse.gml")
