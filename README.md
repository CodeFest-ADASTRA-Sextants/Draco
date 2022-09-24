# lib_template
This is the template for making Python libraries

# Run tests
To run tests execute the following command:

python setup.py pytest

# Build Wheel
To build the Wheel run:

python setup.py bdist_wheel

The wheel file will be stored in ./dist.

# Install the library

pip install /path/to/wheelfile.whl


# Use the library

import mypythonlib
from mypythonlib import myfunctions
