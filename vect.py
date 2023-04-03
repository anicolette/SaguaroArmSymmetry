import math


class Vect:
    NE = 0
    SE = 1
    SW = 2
    NW = 3

    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle % 360
        self.decompose()

    @classmethod
    def fromDecompedVects(cls, h, v):
        magnitude = math.sqrt(math.pow(h, 2) + math.pow(v, 2))

        angle = 0
        if v > 0 and h == 0:  # N
            angle = 0
        elif v == 0 and h > 0:  # E
            angle = 90
        elif v < 0 and h == 0:  # S
            angle = 180
        elif v == 0 and h < 0:  # W
            angle = 270
        elif v > 0 and h > 0:  # NE
            angle = math.degrees(math.atan(float(h)/float(v)))
        elif v < 0 and h > 0:  # SE
            angle = math.degrees(math.atan(float(abs(v))/float(h)))
            angle += 90.0
        elif v < 0 and h < 0:  # SW
            angle = math.degrees(math.atan(float(abs(h))/float(abs(v))))
            angle += 180.0
        elif v > 0 and h < 0:  # NW
            angle = math.degrees(math.atan(float(v)/float(abs(h))))
            angle += 270

        return cls(magnitude, angle)

    def getAngle(self):
        return self.angle

    def getMagnitude(self):
        return self.magnitude

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

        if quad == self.NE:
            self.H = math.sin(math.radians(quadAngle)) * self.magnitude
            self.V = math.cos(math.radians(quadAngle)) * self.magnitude
        elif quad == self.SE:
            self.H = math.cos(math.radians(quadAngle)) * self.magnitude
            self.V = math.sin(math.radians(quadAngle)) * self.magnitude * -1
        elif quad == self.SW:
            self.H = math.sin(math.radians(quadAngle)) * self.magnitude * -1
            self.V = math.cos(math.radians(quadAngle)) * self.magnitude * -1
        elif quad == self.NW:
            self.H = math.cos(math.radians(quadAngle)) * self.magnitude * -1
            self.V = math.sin(math.radians(quadAngle)) * self.magnitude
