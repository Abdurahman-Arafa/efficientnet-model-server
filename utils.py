from werkzeug.exceptions import BadRequest
from PIL.Image import open
from numpy import asarray, float32
from torch import from_numpy, stack
from pillow_heif import register_heif_opener

def get_preprocessed_images(binary_images):
    '''
    Function to preprocess the images before turning them into tensors
    :param binary_images: list of binary images from the request.files
    :return: list of preprocessed images as np.arrays
    '''

    # those mimeTypes are formats supported by the model or convertable to be
    supported_formats = {'image/png', 'image/jpg', 'image/jpeg',
                        'image/heif', 'image/heic', 'image/bmp',
                        'image/tiff', 'image/webp'}

    register_heif_opener() #make PIL compatible with HEIF/HEIC

    if binary_images.__len__() != 10:
        raise BadRequest("Model accepts exactly 10 images.")
    preprocessed_images = []

    for binary_image in binary_images:
        if binary_image[0].content_type not in supported_formats:
            raise BadRequest("image format isn't supprted, try uploading: jpeg,jpg, png, heif, heic, bmp, tiff or webp")

        image = open(binary_image[0])
        if image.mode != 'L':
            image = image.convert('L')
        if image.size != (256, 256):
            image = image.resize((256, 256))
        image = asarray(image, dtype = float32)/255
        preprocessed_images.append(image)
    return preprocessed_images

def images_to_tensors(images):
    '''
    Function to turn images into tensors
    :param images: list of images
    :return: tensor of images
    '''
    # model input shape is (1, 10, 256, 256)
    tensor = stack([from_numpy(img) for img in images]).unsqueeze(0)
    return tensor
