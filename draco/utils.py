import numpy as np
import rasterio
from rasterio.warp import calculate_default_transform

def translate_and_rotate_geoimg(input_file, output_file, x_offset, y_offset, rotation):
    
    with rasterio.open(input_file) as src:
        dest_crs = src.crs
        transform, width, height = calculate_default_transform(
            src.crs, dest_crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        transform = transform * rasterio.Affine.translation(x_offset, y_offset)
        transform = transform * rasterio.Affine.rotation(rotation)
        
        kwargs.update({
            'crs': dest_crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        # Crea el nuevo archivo y le asigna la metadata actualizada.
        with rasterio.open(output_file, 'w', **kwargs) as dst:
            for i in range(1, src.count + 1):
                band = src.read(i)
                dst.write(band, i)