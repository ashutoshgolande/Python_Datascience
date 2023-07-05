#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    dataset = Dataset(annotation_file,transforms)
    download = Download()

    #Print image names and their captions from annotation file using dataset object
    length = len(dataset)
    for i in range(length):
        x = dataset.__getann__(i)
        print(x["file_name"])
        print(x["captions"])

    #Download images to ./data/imgs/ folder using download object
    for i in range(length):
        x = dataset.__getann__(i)
        download("./data/imgs/"+x["file_name"],x["url"])
    #Transform the required image (roll number mod 10) and save it seperately
    transformed_images = dataset.__transformitem__("./data/imgs/1.jpg")
    for count,img in enumerate(transformed_images):
        img.save("./output/1."+str(count)+".jpg","jpeg")
    #Get the predictions from the captioner for the above saved transformed image  
    model = ImageCaptioningModel()
    for i in range(len(transformed_images)):
        print("./output/1."+str(i)+".jpg")
        print(model("./output/1."+str(i)+".jpg",3))

def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage("horizontal"), BlurImage(3),RescaleImage((1280,960)),RescaleImage((320,240)),RotateImage(270),RotateImage(45)], None) # Sample arguments to call experiment()


if __name__ == '__main__':
    main()