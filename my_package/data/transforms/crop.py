# Imports
import PIL
from PIL import Image
import random


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.crop_type = crop_type
        self.h = shape[0]
        self.w = shape[1]

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        # if image is a numpy array, then convert into PIL Image
        if not isinstance(image, PIL.Image.Image):
            image = Image.fromarray(image)

        if self.crop_type == 'center':
            left = (image.width - self.w) // 2
            right = (image.width + self.w) // 2
            top = (image.height - self.h) // 2
            bottom = (image.height + self.h) // 2
            return image.crop((left, top, right, bottom))

        # randomly cropping
        elif self.crop_type == 'random':
            left = random.randint(0, image.width - self.w)
            top = random.randint(0, image.height - self.h)
            right = left + self.w
            bottom = top + self.h
            return image.crop((left, top, right, bottom))

        else:
            raise ValueError("Invalid cropping")


