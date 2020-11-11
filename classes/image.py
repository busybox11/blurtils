from PIL import Image, ImageFilter

class CustomImage(object):
    def __init__(self, img_path, radius=8):
        self.img_path = img_path
        self.img = Image.open(self.img_path)
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

    def region_blur(self, crop):
        crop_img = self.img.crop(crop)
        edit_img = crop_img.filter(ImageFilter.GaussianBlur(self._radius))
        self.img.paste(edit_img, crop)
        return self.img

    def clear_edits(self):
        self.img.close()
        self.img = Image.open(self.img_path)