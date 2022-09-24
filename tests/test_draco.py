from draco import compress, transform
import rasterio
import os

def test_translation():
    '''
        Tests the translation of a georeferenced image.
        Uses the file example inside the tests/data folder.
        Checks if the new image:
            - Has the same number of bands as the original image.
            - Has the same CRS as the original image.
            - Has different bounds than the original image.
            - Has the same width as the original image.
            - Has the same height as the original image.
            - Has the new transform (with translation and rotation) compared to the original image.


    '''
    input_file = 'tests/data/rgb.tif'
    output_file = 'tests/data/rgb_translated.tif'
    x_offset = 100
    y_offset = 100
    rotation = 45
    transform.translate_and_rotate_geoimg(input_file, output_file, x_offset, y_offset, rotation)
    with rasterio.open(input_file) as src:
        with rasterio.open(output_file) as dst:
            assert src.count == dst.count
            assert src.crs == dst.crs
            assert src.bounds != dst.bounds
            assert src.width == dst.width
            assert src.height == dst.height
            assert src.transform * rasterio.Affine.translation(x_offset, y_offset) * rasterio.Affine.rotation(rotation) == dst.transform


def test_compress():
    '''
        Test compress_image function
    '''
    # Arrange
    image_path = 'tests/data/rgb.tif'
    output_path = 'tests/data/rgb.compressed.tif'
    # Act
    compress.compress_image(image_path, output_path)
    # Assert
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) < os.path.getsize(image_path)
    # Cleanup
    os.remove(output_path)