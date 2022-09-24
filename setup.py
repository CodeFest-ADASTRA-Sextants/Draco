from setuptools import find_packages, setup
setup(
    name='draco',
    packages=find_packages(include=['draco']),
    version='0.1.0',
    description='Open source library for geospatial image translation and rotation',
    author='Sextants @ Codefest',
    license='MIT',
    install_requires=[
        'numpy',
        'rasterio'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
