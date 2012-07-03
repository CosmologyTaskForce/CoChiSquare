# A program for chi2 fitting.
# Find minimum of chi2. Using internal numpy and scipy.

import numpy as np
import scipy
from scipy.integrate import quad
import math as m

import fileinput

# Parameters

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



def mag(Omegam0,zt,z):
    om0 =Omegam0
    ztrans = zt
    return 5*np.log10(Distancez(om0,ztrans,z)) + 25

print "mag is"
print mag(0.27,0.5,0.5)

def testfunc(testpar,t):
    tmp=testpar
    return quad(lambda x: x+tmp, 1, t)

print testfunc(7,4)

test = quad(lambda x: x, 1, 3)
print test





# Input data file.

#fileinput.close()

SCPUnion21tmp = []
for line in fileinput.input("../DATA/UNION2/SCPUnion2_mu_vs_z_adjust.txt"):
    linesplit = line.split()
    SCPUnion21tmp = np.append([float(linesplit[1]),float(linesplit[2]),float(linesplit[3])],SCPUnion21tmp)
    pass
fileinput.close()

print SCPUnion21tmp


lenSCPUnion21tmp = len(SCPUnion21tmp)

print lenSCPUnion21tmp

SCPUnion21 = np.reshape(SCPUnion21tmp,(lenSCPUnion21tmp/3,3))
print SCPUnion21


print SCPUnion21[556,2]


print "mag is"+"str(mag(0.25,0.5,1))"

# define chisquare


def chi2union2e(Omegam0,zt):
    om0 =  Omegam0
    ztt = zt
    i=0
    chi2union2esum = 0
    chi2union2esumflag = lenSCPUnion21tmp/3
    while i < chi2union2esumflag:
        (SCPUnion21[i,1] - mag(om0,ztt,SCPUnion21[i,0]))**2/(SCPUnion21[i,2])**2
    return chi2union2esum

print chi2union2e(0.27,1)




