from setuptools import find_packages, setup
from dltp8tdylp import __version__

setup(
    name='dltp8tdylp',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version=__version__,
    description='mlops-demo',
    author='christopher chalcraft'
)
