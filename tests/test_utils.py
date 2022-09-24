from draco import utils
import rasterio

def test_translation():
    input_file = 'tests/data/rgb.tif'
    output_file = 'tests/data/rgb_translated.tif'
    x_offset = 100
    y_offset = 100
    rotation = 45
    utils.translate_and_rotate_geoimg(input_file, output_file, x_offset, y_offset, rotation)
    with rasterio.open(input_file) as src:
        with rasterio.open(output_file) as dst:
            assert src.crs == dst.crs
            assert src.bounds != dst.bounds
            assert src.width == dst.width
            assert src.height == dst.height
            assert src.transform * rasterio.Affine.translation(x_offset, y_offset) * rasterio.Affine.rotation(rotation) == dst.transform