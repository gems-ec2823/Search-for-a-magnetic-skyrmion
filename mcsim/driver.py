import numpy as np


def random_spin(s0, alpha=0.1):
    """Generate a new random spin based on the original one.

    Parameters
    ----------
    s0: np.ndarray

        The original spin that needs to be changed.

    alpha: float

        Larger alpha, larger the modification of the spin. Defaults to 0.1.

    Returns
    -------
    np.ndarray

        New updated spin, normalised to 1.

    """
    delta_s = (2 * np.random.random(3) - 1) * alpha
    s1 = s0 + delta_s
    return s1 / np.linalg.norm(s1)


class Driver:
    """Driver class.

    Driver class does not take any input parameters at initialisation.

    """

    def __init__(self):
        pass

    def drive(self, system, n, alpha=0.1):
        """perform the monte carlo algorithm with n iterations

        Parameters
        ----------
        system: System object with the spin configuration and necessary parameters
        
        n : int
            
            number of iteration

        alpha: float

            Larger alpha, larger the modification of the spin. Defaults to 0.1.

        Returns
        -------

        """
        for _ in range(n):
            E0 = system.energy()
            i, j = np.random.randint(0, system.s.n[0]), np.random.randint(0, system.s.n[1]) #select i and j at random

            original_spin = system.s.array[i, j].copy() #we keep a copy of the spin just in case
            system.s.array[i, j] = random_spin(original_spin, alpha)

            E1 = system.energy()

            if E1 >= E0:
                system.s.array[i, j] = original_spin






