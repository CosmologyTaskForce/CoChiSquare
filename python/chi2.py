# A program for chi2 fitting.
# Find minimum of chi2. Using internal numpy and scipy.

import numpy
from scipy.integrate import quad

# from scipy.optmize import fmin


H0 = 71
c  = 299792

def Hubble(Omegam0,zt,z):
    return H0 * sqrt( Omegam0*(1+z)^2 + 1/2 * Omegam0 * (1+zt)^3 +(1 - Omegam0 - 1/2 * Omegam0 * (1 + zt)^3 ) * (1 + z)^2 )


def Distancez(Omegam0,zt,z):
    return c * (1+z) * quad(1/Hubble(Omegam0,zt,tmp),0,z)[0]

Distancez(0.27,0.5,1)
















