[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Kyi6HUih)
# Search for a magnetic skyrmion

- Deadline: **Friday 20th October 2023**, 16:00 BST

Feel free to modify this `README.md` file as necessary to document your project.

# MCSIM PACKAGE 

The aim of this package is to simulate and visualise the orientation of spins in a two-dimensional grid, in particular to observe structures such as magnetic skyrmions. 

To model our problem, we used a grid representation of spins, each spin being a three-dimensional vector (with x, y and z components). The orientation of these spins is influenced by various energy terms such as the exchange energy, the Dzyaloshinskii-Moriya energy, the Zeeman energy and the anisotropy energy.

We used the Monte Carlo algorithm to simulate the evolution of spin orientations as a function of energy terms. The aim was to minimise the total energy of the system. Matplotlib's quiver function was used to visualise the spin orientations in the 2D grid. The third dimension (z) was represented by colours.

Problems encountered: 

1) Find an aesthetic 3d visualisation that allows us to see that all the arrows are the same size, given that the spin norm is 1 each time. 

## How to use

This package is a python package, you need a conda environment and Python version 3.11. To run the package, you need to:
1) clone the repository by running: git clone url-github-repository
2) navigate into the repository: cd repository-name
3) run: pip install .


```python

```
