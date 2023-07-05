# Imports
import PIL
from PIL import Image


class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        # create PIL image if it is a nnumpy array
        if not isinstance(image, PIL.Image.Image):
            image = Image.fromarray(image)

        self.image = image

        if self.flip_type == 'horizontal':
            return self.image.transpose(Image.FLIP_LEFT_RIGHT)

        elif self.flip_type == 'vertical':
            return self.image.transpose(Image.FLIP_TOP_BOTTOM)
        


