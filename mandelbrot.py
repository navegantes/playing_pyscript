import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# import numba
# from numba import jit

# @autojit
# @jit


def mandel():

    px, py = (-2., 0.7), (-1.25, 1.25)
    # px = (.205, .245);
    # py = (-.520, -.560);
    # px = (.205, .245);
    # py = (-.520, -.560);

    width = 1000
    height = 1000
    niter = 50

    x = np.linspace(px[0], px[1], width, dtype=np.float64)
    y = np.linspace(py[0], py[1], height, dtype=np.float64).reshape(-1, 1)
    c = x + 1.0j * y
    M = np.zeros((height, width))
    # z = np.zeros(M.shape, dtype=np.complex64)
    z = np.zeros_like(M, dtype=np.complex64)
    mask = np.ones(M.shape, dtype=bool)

    fig, ax = plt.subplots(1, 1)
    # cmap = 'cividis' #'CMRmap' #'gnuplot2' #'gnuplot' #'viridis' #'jet'
    # cmap = 'coolwarm'  # 'gist_ncar'#'afmhot' #'hot' #'gist_heat' #'gist_ncar'
    # plt.set_cmap(cmap)

    for i in range(niter):
        z[mask] = z[mask]*z[mask] + c[mask]
        
        mask = ((z.real*z.real+z.imag*z.imag) < 4)
        M[mask] = 0
        m2 = ~mask & (M == 0)
        M[m2] = i
        
        ax.imshow(M, origin='lower', extent=(px[0], px[1], py[0], py[1]),
                        cmap=cm.hot)
    plt.title("Conjunto Mandelbrot")
    
    return fig


# if __name__ == '__main__':
mandel()
