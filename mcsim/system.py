import numpy as np


class System:
    """System object with the spin configuration and necessary parameters.

    Parameters
    ----------
    s: mcsim.Spins

        Two-dimensional spin field.

    B: Iterable

        External magnetic field, length 3.

    K: numbers.Real

        Uniaxial anisotropy constant.

    u: Iterable(float)

        Uniaxial anisotropy axis, length 3. If ``u`` is not normalised to 1, it
        will be normalised before the calculation of uniaxial anisotropy energy.

    J: numbers.Real

        Exchange energy constant.

    D: numbers.Real

        Dzyaloshinskii-Moriya energy constant.

    """

    def __init__(self, s, B, K, u, J, D):
        self.s = s
        self.J = J
        self.D = D
        self.B = B
        self.K = K
        self.u = u

    def energy(self):
        """Total energy of the system.

        The total energy of the system is computed as the sum of all individual
        energy terms.

        Returns
        -------
        float

            Total energy of the system.

        """
        #print("Total energy:", self.zeeman() + self.anisotropy() + self.exchange() + self.dmi())
        return self.zeeman() + self.anisotropy() + self.exchange() + self.dmi()

    def zeeman(self):
        """Total zeeman energy.

        We compute the Zeeman energy for the entire two-dimensional lattice as the sum of zeeman energies for all spins

        Returns
        -------
        float

            Total zeeman energy of the system.

        """
        total_energy = 0

        for spin in self.s.array.reshape(-1, 3): #each line will represent a spin
            total_energy -= np.dot(spin, self.B)
        
        return total_energy

    def anisotropy(self):
        """Total anisotropy energy.

        We compute the anisotropy energy for the entire two-dimensional lattice as the sum of anisotropy energies for all spins

        Returns
        -------
        float

            Total anisotropy energy of the system.

        """
        self.u /= np.linalg.norm(self.u)

        total_energy = 0
        
        for spin in self.s.array.reshape(-1, 3):
            total_energy -= self.K * (np.dot(spin, self.u) ** 2)

        return total_energy

    def exchange(self):
        
        """Total exchange energy.

        We compute the exchange energy for the entire two-dimensional lattice as the sum of exchange energies for all spins

        Returns
        -------
        float

            Total exchange energy of the system.

        """
        if self.J < 0:
            raise ValueError("J must be >0")
            
        nx_interactions = np.sum(self.s.array[:-1, :, :] * self.s.array[1:, :, :], axis=2) #scalar product in the x direction
        
        ny_interactions = np.sum(self.s.array[:, :-1, :] * self.s.array[:, 1:, :], axis=2) #scalar product in the y direction

        total_interactions = np.sum(nx_interactions) + np.sum(ny_interactions)

        total_energy = -self.J * total_interactions
        
        return total_energy

    def dmi(self):
        
        """Total dmi energy.

        We compute the dmi energy for the entire two-dimensional lattice as the sum of dmi energies for all spins

        Returns
        -------
        float

            Total dmi energy of the system.

        """
        
        if self.D < 0:
            raise ValueError("D must be > 0 ")

        cross_product_nx = np.cross(self.s.array[:-1, :, :], self.s.array[1:, :, :], axis=2) #vector product
        cross_product_ny = np.cross(self.s.array[:, :-1, :], self.s.array[:, 1:, :], axis=2)

        direction_nx = np.full_like(cross_product_nx, [0, 1, 0]) #new array with the same shape as the first argument and filled with [0,1,0]
        direction_ny = np.full_like(cross_product_ny, [1, 0, 0])

        dmi_nx = np.sum(direction_nx * cross_product_nx, axis=2) #scalar product
        dmi_ny = np.sum(direction_ny * cross_product_ny, axis=2)

        total_energy = -self.D * (np.sum(dmi_nx) + np.sum(dmi_ny))    
        

        return total_energy




