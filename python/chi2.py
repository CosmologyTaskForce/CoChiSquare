# A program for chi2 fitting.
# Find minimum of chi2. Using internal numpy and scipy.

import numpy as np
import scipy
from scipy.integrate import quad
import math as m


# Parameters
.
H0 = 71
c  = 299792


# Define hubble function.

def Hubble(Omegam0,zt,z):
    return H0 * m.sqrt( Omegam0*(1+z)**2 + 1/2 * Omegam0 * (1+zt)**3 +(1 - Omegam0 - 1/2 * Omegam0 * (1 + zt)**3 ) * (1 + z)**2 )


# Define 

def Distancez(Omegam0,zt,z):
    om0 = Omegam0
    ztrans = zt
    return c * (1+z) * quad(lambda tmp: 1/Hubble(om0,ztrans,tmp),0,z)

flag1 = Distancez(0.27,0.5,1)
#print flag1 





def testfunc(testpar,t):
    tmp=testpar
    return quad(lambda x: x+tmp, 1, t)

print testfunc(7,4)

test = quad(lambda x: x, 1, 3)
print test










