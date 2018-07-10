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

def get_bin_labels(assign):
    bin_labels_str = assign['bin_labels'][...]
    bin_labels = []
    for ibstr, bstr in enumerate(bin_labels_str):
        st, ed = bstr.find('['), bstr.find(']')
        bin_labels.append(eval(bstr[st:ed+1]))
    bin_labels = np.array(bin_labels[:])
    return bin_labels
