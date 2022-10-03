# this is executed when `pip install -e .` is run
from setuptools import setup

setup(
    name='Auction Sphere',
    version='1.0',
    long_description=__doc__,
    packages=['yourapplication'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)