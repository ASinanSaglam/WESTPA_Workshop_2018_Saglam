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
    metastab_ass = pcca.metastable_assignment
    f = open("metasble_assignments.pkl", "w")
    pickle.dump(metastab_ass, f)
    f.close()
    
    a = h5py.File(assign_file, 'r')
    bin_labels = ahelper.get_bin_labels(a)
    bin_labels_01 = np.array(map(lambda x: (x[0], x[1]), bin_labels))
    bin_labels_01 = bin_labels_01[1:]
    
    print("metastab 0")
    print(bin_labels[metastab_ass.T==0].mean(axis=0))
    print("metastab 1")
    print(bin_labels[metastab_ass.T==1].mean(axis=0))
    print("metastab 2")
    print(bin_labels[metastab_ass.T==2].mean(axis=0))
    print("metastab 3")
    print(bin_labels[metastab_ass.T==3].mean(axis=0))
    
    state_colors = {0: "#FF00FF", 1: "#0000FF", 2: "#FF0000", 3: "#000000"}
    tm = pcca.transition_matrix
    node_sizes = pcca.stationary_probability*1000
    edge_sizes = tm
    
    G = nx.DiGraph()
    for i in range(tm.shape[0]):
        if node_sizes[i] > 0:
            G.add_node(i, weight=float(node_sizes[i]), color=state_colors[metastab_ass[i]], LabelGraphics={"text": " "}, #)
                   graphics={"type": "circle", "fill": state_colors[metastab_ass[i]], "w": node_sizes[i], "h": node_sizes[i]})
    
    for i in range(tm.shape[0]):
        for j in range(tm.shape[1]):
            if i != j:
                if edge_sizes[i][j] > 0:
                    G.add_edge(i, j, weight=float(edge_sizes[i][j]), graphics={"type": "arc", "targetArrow": "none", "fill": state_colors[metastab_ass[i]]})
    
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
            G.add_node(i, weight=float(node_sizes[i]), color=state_colors[i], LabelGraphics={"text": " "}, #)
                   graphics={"type": "circle", "fill": state_colors[i], "w": node_sizes[i], "h": node_sizes[i]})
    
    for i in range(tm.shape[0]):
        for j in range(tm.shape[1]):
            if i != j:
                if edge_sizes[i][j] > 0:
                    G.add_edge(i, j, weight=float(edge_sizes[i][j]), graphics={"type": "arc", "targetArrow": "none", "fill": state_colors[i]})
    
    nx.write_gml(G, "pcca_coarse.gml")
