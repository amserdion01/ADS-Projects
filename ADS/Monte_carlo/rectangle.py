class Rectangle():

    def __init__(self, origin_x, origin_y, length, width):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.length = length
        self.width = width

    def get_x(self):
        return self.origin_x

    def get_y(self):
        return self.origin_y

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width