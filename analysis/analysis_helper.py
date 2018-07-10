import numpy as np
import h5py, pickle
import matplotlib

def row_normalize(mat):
    rnmat = np.zeros(mat.shape)
    for irow, row in enumerate(mat):
        if row.sum() != 0:
            rnmat[irow] = row/row.sum() 
    return rnmat

def symmetrize(mat):
    smat = np.zeros(mat.shape)
    smat = 0.5*(mat+mat.T)
    return smat

def get_bin_labels(assign):
    bin_labels_str = assign['bin_labels'][...]
    bin_labels = []
    for ibstr, bstr in enumerate(bin_labels_str):
        st, ed = bstr.find('['), bstr.find(']')
        bin_labels.append(eval(bstr[st:ed+1]))
    bin_labels = np.array(bin_labels[:])
    return bin_labels

# Rest taken from Josh Adelman (@synapticarbors on GitHub)
# -----------------------------------------------------------------------------
# Voronoi diagram from a list of points
# Copyright (C) 2011  Nicolas P. Rougier
#
# Distributed under the terms of the BSD License.
# -----------------------------------------------------------------------------
def circumcircle(P1,P2,P3):
    ''' 
    Adapted from:
    http://local.wasp.uwa.edu.au/~pbourke/geometry/circlefrom3/Circle.cpp
    '''
    delta_a = P2 - P1
    delta_b = P3 - P2
    if np.abs(delta_a[0]) <= 0.000000001 and np.abs(delta_b[1]) <= 0.000000001:
        center_x = 0.5*(P2[0] + P3[0])
        center_y = 0.5*(P1[1] + P2[1])
    else:
        aSlope = delta_a[1]/delta_a[0]
        bSlope = delta_b[1]/delta_b[0]

        if aSlope == 0.0:
            aSlope = 1E-6

        if bSlope == 0.0:
            bSlope = 1E-6

        if np.isinf(aSlope):
            aSlope = 1E6

        if np.isinf(bSlope):
            bSlope = 1E6

        if np.abs(aSlope-bSlope) <= 0.000000001:
            return None
        center_x= (aSlope*bSlope*(P1[1] - P3[1]) + bSlope*(P1[0] + P2 [0]) \
                        - aSlope*(P2[0]+P3[0]) )/(2* (bSlope-aSlope) )
        center_y = -1*(center_x - (P1[0]+P2[0])/2)/aSlope +  (P1[1]+P2[1])/2;
    return center_x, center_y

def voronoi(X,Y):
    P = np.zeros((X.size+4,2))
    P[:X.size,0], P[:Y.size,1] = X, Y
    # We add four points at "infinity"
    m = max(np.abs(X).max(), np.abs(Y).max())*1e5
    P[X.size:,0] = [-m, -m, +m, +m]
    P[Y.size:,1] = [-m, +m, -m, +m]
    D = matplotlib.tri.Triangulation(P[:,0],P[:,1])
    T = D.triangles
    n = T.shape[0]
    C = np.zeros((n,2))
    for i in range(n):
        C[i] = circumcircle(P[T[i,0]],P[T[i,1]],P[T[i,2]])
    X,Y = C[:,0], C[:,1]
    segments = []
    for i in range(n):
        for j in range(3):
            k = D.neighbors[i][j]
            if k != -1:
                segments.append( [(X[i],Y[i]), (X[k],Y[k])] )
    return segments
