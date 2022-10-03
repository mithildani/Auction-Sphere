# this is executed when `pip3 install -e .` is run
from setuptools import setup, find_packages

setup(
    name='Auction Sphere',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(where='backend'),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
