from setuptools import find_packages, setup
setup(
    name='lib_name',
    packages=find_packages(include=['lib_name']),
    version='0.1.0',
    description='A Python library',
    author='Sextants @ Codefest',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
