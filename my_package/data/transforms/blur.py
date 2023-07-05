# Imports
import PIL
from PIL import Image, ImageFilter


class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        # if the given image is a numpy array
        if not isinstance(image, PIL.Image.Image):
            image = Image.fromarray(image)

        return image.filter(ImageFilter.GaussianBlur(self.radius))

