from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# +
setup(
    name="mcsim",  # Package name must be mcsim.
    # Extend setup.py file as required.
    version='1.0.0',
    packages=['mcsim'],
    install_requires=requirements,
    description='Example of a simulation of magnetic skyrmions', 
    author='Elias CHERIF GEMS', 
    author_email='ec2823@imperial.ac.uk',
    
)
# -


