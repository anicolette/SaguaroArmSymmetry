import math


class Vect:
    NE = 0
    SE = 1
    SW = 2
    NW = 3

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
        self.decompose()

    def getV(self):
        return self.V

    def getH(self):
        return self.H

    def getQuad(self):
        return self.angle/90

    def decompose(self):
        quadAngle = self.angle % 90
        quad = int(self.angle / 90)
        if self.angle == 0 or self.angle == 360:
            self.V = self.magnitude
            self.H = 0
            return
        elif self.angle == 90:
            self.V = 0
            self.H = self.magnitude
            return
        elif self.angle == 180:
            self.V = -1 * self.magnitude
            self.H = 0
            return
        elif self.angle == 270:
            self.V = 0
            self.H = -1 * self.magnitude
            return

        self.V = math.sin(math.radians(quadAngle)) * self.magnitude
        self.H = math.cos(math.radians(quadAngle)) * self.magnitude

        if quad == self.SE:
            self.V = self.V * -1
        elif quad == self.SW:
            self.V = self.V * -1
            self.H = self.H * -1
        elif quad == self.NW:
            self.H = self.H * -1
