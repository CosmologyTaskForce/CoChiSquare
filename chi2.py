# A program for chi2 fitting.
# Find minimum of chi2. Using internal numpy and scipy.

import numpy
import pylab

# from scipy.optmize import fmin


H0=71


def hubble(om0,z):
    return H0*sqrt(om0*(1+z))
