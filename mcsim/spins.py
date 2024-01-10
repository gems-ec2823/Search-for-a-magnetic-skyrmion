import numbers

import numpy as np

import matplotlib.pyplot as plt


class Spins:
    """Field of spins on a two-dimensional lattice.

    Each spin is a three-dimensional vector s = (sx, sy, sz). Underlying data
    stucture (``self.array``) is a numpy array (``np.ndarray``) with shape
    ``(nx, ny, 3)``, where ``nx`` and ``ny`` are the number of spins in the x
    and y directions, respectively, and 3 to hold all three vector components of
    the spin.

    Parameters
    ----------
    n: Iterable

        Dimensions of a two-dimensional lattice ``n = (nx, ny)``, where ``nx``
        and ``ny`` are the number of atoms in x and y directions, respectively.
        Values of ``nx`` and ``ny`` must be positive integers.

    value: Iterable

        The value ``(sx, sy, sz)`` that is used to initialise all spins in the
        lattice. All elements of ``value`` must be real numbers. Defaults to
        ``(0, 0, 1)``.

    """

    def __init__(self, n, value=(0, 0, 1)):
        # Checks on input parameters.
        if len(n) != 2:
            raise ValueError(f"Length of iterable n must be 2, not {len(n)=}.")
        if any(i <= 0 or not isinstance(i, int) for i in n):
            raise ValueError("Elements of n must be positive integers.")

        if len(value) != 3:
            raise ValueError(f"Length of iterable value must be 3, not {len(n)=}.")
        if any(not isinstance(i, numbers.Real) for i in n):
            raise ValueError("Elements of value must be real numbers.")

        self.n = n
        self.array = np.empty((*self.n, 3), dtype=np.float64)
        self.array[..., :] = value

        if not np.isclose(value[0] ** 2 + value[1] ** 2 + value[2] ** 2, 1):
            # we ensure all spins' magnitudes are normalised to 1.
            self.normalise()

    @property
    def mean(self):
        """spins mean.

        We compute the mean over each spin index

        Returns
        -------
        np.array

            mean over each spin index

        """
        #mean over each spin index
        mx = np.mean(self.array[..., 0])
        my = np.mean(self.array[..., 1])
        mz = np.mean(self.array[..., 2])
        
        return np.array([mx, my, mz])


    def __abs__(self):
        """spins norm.

        We compute the norm over each spin 

        Returns
        -------
        np.array

            norm over each spin 

        """
        nx, ny, nz = self.array.shape
        self.norm = np.zeros((nx, ny, 1))

        for i in range(nx):
            for j in range(ny):
                spin = self.array[i, j]
                self.norm[i, j, 0] = np.sqrt(spin[0]**2 + spin[1]**2 + spin[2]**2)
                
        return self.norm
                
    def normalise(self):
        """Normalise the magnitude of all spins to 1."""
        self.array = self.array / abs(self)  # This computation will be failing until you implement __abs__.

    def randomise(self):
        """Initialise the lattice with random spins.

        Components of each spin are between -1 and 1: -1 <= si <= 1, and all
        spins are normalised to 1.

        """
        self.array = 2 * np.random.random((*self.n, 3)) - 1
        self.normalise()

    def plot(self):
        """
        spins are traced in a 2D plane and represented by arrows

        """
        nx, ny, nz = self.array.shape

        x, y = np.meshgrid(np.arange(nx), np.arange(ny))

        #obtain the spin components
        u = self.array[..., 0]
        v = self.array[..., 1]
        w = self.array[..., 2]

        fig, ax = plt.subplots(figsize=(10, 10))

        #quiver to view arrows
        quiver = ax.quiver(x, y, u, v, w, scale=10, width=0.005, pivot='middle', cmap='viridis', headwidth=3, headlength=4)

        cbar = plt.colorbar(quiver)
        cbar.set_label('z')

        ax.set_xlim(-0.5, nx-0.5)
        ax.set_ylim(-0.5, ny-0.5)
        ax.set_aspect('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Visualisation of Spins in a 2D Plane')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()








