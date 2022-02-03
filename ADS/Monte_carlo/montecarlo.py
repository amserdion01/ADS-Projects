from random import random


class MonteCarlo:

    def __init__(self, length, width, rectangles):

        # constructor
        self.length = length  # :param length -- length of the enclosing rectangle
        self.width = width    # :param width -- width of the enclosing rectangle
        self.rectangles = []  # :param rectangles -- array that contains the embedded rectangles

        if rectangles:   # appending the embedded rectangles to the rectagles list for montecarlo
            for rect in rectangles:
                self.rectangles.append(rect)

    def area(self, num_of_shots):
        # Method to estimate the area of the enclosing rectangle that is not covered by the embedded rectangles
        # :param num_of_shots -- Number of generated random points whose location (inside/outside) is analyzed

        if num_of_shots == None:  # :raises ValueError if any of the parameters is None
            raise ValueError

        random_points = []
        inside = 0
        outside = 0
        shots = num_of_shots
        for i in range(shots):

            random_x = random() * self.length
            random_y = random() * self.width
            random_points.append([random_x,random_y])

        for i in random_points:
            ok = 0
            for j in self.rectangles:
                if self.inside(i[0],i[1],j):
                    ok = 1
                    break
            if ok == 0:
                outside = outside + 1
            else:
                inside = inside + 1

        return self.width * self.length * ( 1 - ( inside / ( outside + inside ) ) )


        # :return float -- the area of the enclosing rectangle not covered.

    def inside(self, x, y, rect):

        """Method to determine if a given point (x,y) is inside a given rectangle

        Keyword arguments:
        :param x,y -- coordinates of the point to check
        :param rect -- given rectangle


        """
        if x == None or y == None or rect == None:
            raise ValueError  # :raises ValueError if any of the parameters is None

        origin_x = rect.get_x()
        origin_y = rect.get_y()

        upper_x = origin_x + rect.get_length()
        upper_y = origin_y + rect.get_width()

        # :return bool

        if origin_x <= x <= upper_x and origin_y <= y <= upper_y:
            return True

        return False