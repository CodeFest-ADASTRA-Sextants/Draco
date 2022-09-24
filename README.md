# Draco

This open source library makes the translation and rotation of georeferenced images easy.

Currently, the compatible formats are:
- TIFF (GeoTIFF)
- IMG
- JP2

## Run tests
To run tests execute the following command:

python setup.py pytest

## Build Wheel
To build the Wheel run:

python setup.py bdist_wheel

The wheel file will be stored in ./dist.

# Install the library

pip install /path/to/wheelfile.whl


# Use the library


```
from draco import utils

input_file = 'test.tif'
output_file = 'out.tif'
restore_file = 'restored.tif'

# Offsets units based on the original crs 
x_offset = 200
y_offset = 500

# Degrees for image rotation
rotation = 45

# Translate and rotate image.
# This produces a new file at the specified location
utils.translate_and_rotate_geoimg(input_file, output_file, x_offset, y_offset, rotation)

# Recover image from translation and rotation.
# This produces a new file at the specified location
utils.invert(output_file, restore_file, x_offset, y_offset, rotation)

```
