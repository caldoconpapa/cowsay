# class file (dragon) that is derived from cow
from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        self.set_image(image)
    @staticmethod
    def can_breathe_fire():
        return True
