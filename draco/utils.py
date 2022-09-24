import rasterio

def translate_and_rotate_geoimg(input_file, output_file, x_offset=0, y_offset=0, rotation=0):
    '''
        Given the georeferenced image at [input_file], translate and rotate the image by [x_offset], [y_offset], and [rotation] respectively.
        The new image is written to [output_file].
    '''
    
    with rasterio.open(input_file) as src:

        # Gets the original transform and calculates the new transform
        transform = src.meta['transform']
        transform = calculate_transform(transform, x_offset, y_offset, rotation)
        
        # Updates the metadata with the new transform
        kwargs = src.meta.copy()
        kwargs.update({'transform': transform})

        write_to_file(output_file, kwargs, src)

def inverse(input_file, output_file, x_offset=0, y_offset=0, rotation=0):
    '''
        Inverses the translation and rotation of a georeferenced image.
        This function uses the same parameters as translate_and_rotate_geoimg.
    '''
    translate_and_rotate_geoimg(input_file, output_file, -x_offset, -y_offset, -rotation)

def calculate_transform(original_transform, x_offset=0, y_offset=0, rotation=0):
    '''
        Calculates the new transform of a georeferenced image given the original transform, x_offset, y_offset, and rotation.
        param original_transform: The original transform of the image.
        param x_offset: The x offset of the translation.
        param y_offset: The y offset of the translation.
        param rotation: The rotation of the image.
        return: The new transform of the image.
    '''
    transform = original_transform * rasterio.Affine.translation(x_offset, y_offset)
    transform = transform * rasterio.Affine.rotation(rotation)
    return transform

def write_to_file(file_name, meta, src):
    '''
        Writes the new image to a file using all of its bands.
        param file_name: The name of the file to write to.
        param meta: The metadata of the new image.
        param src: The source image read by rasterio.
    '''
    with rasterio.open(file_name, 'w', **meta) as dst:
            for i in range(1, src.count + 1):
                band = src.read(i)
                dst.write(band, i)