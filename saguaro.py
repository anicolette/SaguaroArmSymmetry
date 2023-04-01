import math
import vect


class SaguaroArm:
    """
    aHeight     : distance from ground to emergence of arm
    bHeight     : distance from 1m marker to ground at degree of arm
    cHeight     : distance from ground to top of arm
    dHeight     : distance from 1m marker to ground at degree of arm
    stemDist    : distance between arm and stem
    totalHeight : overall height of the saguaro
    """

    def __init__(self, aHeight, bHeight, cHeight, dHeight, stemDist, degree, totalHeight):
        self.emergence = aHeight - bHeight + 1
        self.height = cHeight - dHeight + 1
        self.stemDist = stemDist
        self.degree = degree
        """
        length is being counted as the hypotenuse of the right triangle defined by
        the distance from the stem and the height of the arm minus the emergence
        """
        self.length = math.sqrt(
            math.pow(self.height - self.emergence, 2) + math.pow(self.stemDist, 2))

        """
        Adjust the magnitude of the vector based on the ratio of the emergence
        height with the overall height of the saguaro. Based on the idea that
        an arm at ground level would have basically no influence on balance
        while an arm at the very top would have a greater influence.
        """
        if totalHeight == 0:
            totalHeight = .01  # prevent divide by zero errors
        self.adjustedMagnitude = (
            float(self.emergence) / float(totalHeight)) * float(self.length)

        self.v = vect.Vect(self.adjustedMagnitude, degree)

    def getAdjustedVectors(self):
        return self.v.getH(), self.v.getV()

    def getMagnitude(self):
        return self.adjustedMagnitude

    def getEmergence(self):
        return self.emergence

    def getLength(self):
        return self.length

    def getDegree(self):
        return self.degree


class Saguaro:
    def __init__(self, height):
        self.height = height
        self.arms = []

    def addArm(self, aHeight, bHeight, cHeight, dHeight, stemDist, degree):
        self.arms.append(SaguaroArm(aHeight, bHeight, cHeight,
                         dHeight, stemDist, degree, self.height))
