# Imports
import PIL
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    # initialize the class with an output size
    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        if not isinstance(image, PIL.Image.Image):
            image = Image.fromarray(image)

        self.image = image
        # if only one int is provided the smaller
        if isinstance(self.output_size, int):

            width, height = self.image.size

            if width < height:
                ratio = self.output_size/width
                self.output_size = (self.output_size, int(height * ratio))
            else:
                ratio = self.output_size/height
                self.output_size = (int(width * ratio), self.output_size)

        return self.image.resize(self.output_size)



