import numpy as np

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

