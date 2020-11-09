from PIL import Image, ImageFilter

class CustomImage(object):
    def __init__(self, img_path, radius=8):
        self.img = Image.open(img_path)
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius_in):
        if(radius_in < 0): 
            raise ValueError("Blur radius should be equal or greater than 0") 
        self._radius = radius_in

    def full_blur(self):
        return self.img.filter(ImageFilter.GaussianBlur(self._radius))