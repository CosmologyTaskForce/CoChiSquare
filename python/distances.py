"""Plot some distance measures versus redshift and omega_M.

"""
import sys
import getopt

import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import cosmolopy.distance as cd
import cosmolopy.constants as cc

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def plot_DM():
    """The dimensionless proper motion distance DM/DH. 
    """

    # Set up an array of redshift values.
    dz = 0.01
    z = numpy.arange(0., 10. + 1.1 * dz, dz)

    # Set up a cosmology dictionary, with an array of matter density values.
    cosmo = {}
    dom = 0.01
    om = numpy.atleast_2d(numpy.linspace(0.1, 1.0, (1.-0.1)/dom)).transpose()
    dzt = 0.01
    zt = numpy.atleast_2d(numpy.linspace(0.1, 1.0, (1.-0.1)/dzt)).transpose()
    cosmo['omega_M_0'] = om
    cosmo['transition_redshift'] = zt
    cosmo['omega_lambda_0'] = 1/2 * cosmo['omega_M_0'] * (1 + cosmo['transition_redshift'])**3
    cosmo['h'] = 0.701
    cosmo['omega_k_0'] = 1 - cosmo['omega_M_0'] - 1/2 * cosmo['omega_M_0'] * ( cosmo['transition_redshift'] + 1 )**3


    # Calculate the hubble distance.
    dhc = cd.comoving_distance(z,z0=0, **cosmo)
    # Calculate the comoving distance.
    dm = cd.comoving_distance_transverse(z, **cosmo)

    # Make plots

    print om.ravel()
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    om, zt = meshgrid(om.ravel(),zt.ravel())
    hub = cd.comoving_distance(1,z0=0,**cosmo)
    surf = ax.plot_surface(om,zt,hub,rstride=1,cstride=1,cmap=cm.jet,linewidth=0,antialiased=False)
#    ax.set_zlim()
    plt.show() 




def plot_DA(filename):
    """The dimensionless angular diameter distance DA/DH. 
    """

    # Set up an array of redshift values.
    dz = 0.1
    z = numpy.arange(0., 10. + dz, dz)

    # Set up a cosmology dictionary, with an array of matter density values.
    cosmo = {}
    dom = 0.01
    om = numpy.atleast_2d(numpy.linspace(0.1, 1.0, (1.-0.1)/dom)).transpose()
    cosmo['omega_M_0'] = om
    cosmo['omega_lambda_0'] = 1. - cosmo['omega_M_0']
    cosmo['h'] = 0.701
    cosmo['omega_k_0'] = 0.0

    # Calculate the hubble distance.
    dh = cd.hubble_distance_z(0, **cosmo)
    # Calculate the angular diameter distance.
    da = cd.angular_diameter_distance(z, **cosmo)

    # Make plots.
    plot_dist(z, dz, om, dom, da, dh, 'angular diameter distance', r'D_A',
              filename)
    plot_dist_ony(z, dz, om, dom, da, dh, 'angular diameter distance', r'D_A',
                  filename)

def plot_dist(z, dz, om, dom, dist, dh, name, mathname, filename=None):
    """Make a 2-D plot of a distance versus redshift (x) and matter density (y).
    """
    # Grid of redshift and matter density values.
    x, y = numpy.meshgrid(z, om)
    plt.figure(figsize=(5.5,4.5))    
    plt.imshow(dist/dh, 
                 extent=(z.min() - dz/2., 
                         z.max() + dz/2.,
                         om.max() + dom/2.,
                         om.min() - dom/2., 
                         ),
                 interpolation='nearest',
                 aspect = z.max()/om.max(),
                 cmap = cm.Spectral,
                 )
    cb = plt.colorbar()
    cb.ax.set_ylabel(r'$' + mathname + '/D_H$')

    plt.contour(x, y, dist/dh, 10, colors='k')
    plt.xlim(z.min(), z.max())
    plt.ylim(om.min(), om.max()) 
    plt.xlabel("redshift z")
    plt.ylabel(r"$\Omega_M = 1 - \Omega_\lambda$")
    plt.title(name)
    if filename is not None:
        prefix, extension = filename.split('.')
        plt.savefig(prefix + '_' + mathname + '.' + extension,
                      bbox_inches="tight")


def plot_dist_ony(z, dz, om, dom, dist, dh, name, mathname, filename=None):
    """Make a 2-D plot of matter density versus redshift (x) and distance (y)
    """


    dist = dist/dh
    z = z * numpy.ones(dist.shape)
    om = om * numpy.ones(dist.shape)

    plt.figure(figsize=(5.5,4.5))    


    plt.contour(z, dist, om, 50)
    cb = plt.colorbar()
    cb.ax.set_ylabel(r'$\Omega_M = 1 - \Omega_\lambda$')
    
    plt.xlim(z.min(), z.max())
    plt.ylim(dist.min(), dist.max()) 
    plt.xlabel("redshift z")
    plt.ylabel(name + r': $'+mathname+'/D_H$')
    plt.title(name)
    if filename is not None:
        prefix, extension = filename.split('.')
        plt.savefig(prefix + '_' + mathname + '_ony.' + extension,
                      bbox_inches="tight")        

if __name__ == "__main__":
#    if len(sys.argv)==1:
#        print "Run with a filename argument to produce image files, e.g.:"
#        print " python plot_2d_distances.py dist2d.png"
#        print " python plot_2d_distances.py dist2d.eps"
#    if len(sys.argv) > 1:
#        filename = sys.argv[1]
#    else:
#        filename = None
        
    plot_DM()

#    if filename is None:
#        plt.show()

