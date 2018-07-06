#!/usr/bin/env python
import numpy

def pcoord_loader(fieldname, coord_filename, segment, single_point=False):
    """
    Loads and stores coordinates

    **Arguments:**
        :*fieldname*:      Key at which to store dataset
        :*coord_filename*: Temporary file from which to load coordinates
        :*segment*:        WEST segment
        :*single_point*:   Data to be stored for a single frame
                           (should always be false)
    """
    # Load coordinates
    pcoord    = numpy.loadtxt(coord_filename, dtype = numpy.float32)
    # Save to hdf5
    if not single_point:
        #print(pcoord.shape, numpy.average(pcoord, axis=1).shape)
        #segment.pcoord = numpy.average(pcoord, axis=1).reshape((1,2))
        #segment.pcoord = numpy.average(pcoord, axis=1).T
        segment.pcoord = pcoord[:,[1,2,3,4,5,6,7,8]]
    else:
        #print(pcoord[[1,2,3]])
        #segment.pcoord = numpy.average(pcoord)
        segment.pcoord = pcoord[[1,2,3,4,5,6,7,8]]

def concs_loader(fieldname, coord_filename, segment, single_point=False):
    # Load coordinates
    concs = numpy.loadtxt(coord_filename, dtype = numpy.float32)

    # Save to hdf5
    if not single_point:
        segment.data[fieldname] = concs[...]
    else:
        segment.data[fieldname] = concs[...]
