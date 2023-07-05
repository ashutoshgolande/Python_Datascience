# Imports
import PIL
from PIL import Image


class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self.degrees = degrees

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if not isinstance(image, PIL.Image.Image):
            image = Image.fromarray(image)

        self.image = image
        return self.image.rotate(self.degrees)
    
