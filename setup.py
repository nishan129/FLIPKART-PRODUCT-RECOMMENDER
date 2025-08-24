from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name='flipkart-recommender',
    version='0.1.0',
    author='Nishant Borkar',
    packages=find_packages(),
    install_requires=requirements,
)