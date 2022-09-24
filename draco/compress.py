from osgeo import gdal


def compress_image(image_path, output_path):
    '''
        Compresses an image using the LZW algorithm.
        Supports .tif and .tiff files.
        param image_path: path to the image to be compressed
        param output_path: path to the output image
    '''

    # Compression using ZSTD Algorithm

    # String variable that represents the compression algorithm used
    compression_type = 'ZSTD'

    # Translation options
    creation_options = ['COMPRESS={}'.format(compression_type), 'DISCARD_LSB=10', 'TILED=YES', 'COPY_SRC_OVERVIEWS=YES',
                        'BLOCKXSIZE=512', 'BLOCKYSIZE=512', 'NUM_THREADS=ALL_CPUS']

    t_options = gdal.TranslateOptions(creationOptions=creation_options)

    c_options = ['GDAL_CACHEMAX=16000000000']

    # Application of the compression method
    gdal.Translate(output_path, image_path, options=t_options,
                   config_options=c_options)
