import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot, cm
from matplotlib.colors import Normalize
import numpy
import cfd_burger as cfdb


def simulate():
    cfd = cfdb.Burgers(2, 2, 41, 41)
    u = cfd.fetch_u()
    v = cfd.fetch_v()
    for i in range(0, 2510, 50):
        cfd.evolve(i)
        ax = pyplot.figure()
        norm = Normalize()
        magnitude = numpy.sqrt(u[::2] ** 2 + v[::2] ** 2)
        pyplot.quiver(u[::2], v[::2], norm(magnitude), scale=60, cmap=pyplot.cm.jet)
        ax.savefig("frame" + str(i).zfill(5) + ".png", dpi=300)
        ax.clear()
    return True
