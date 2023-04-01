import math


class SaguaroArm:
    """
    aHeight  : distance from ground to emergence of arm
    bHeight  : distance from 1m marker to ground at degree of arm
    cHeight  : distance from ground to top of arm
    dHeight  : distance from 1m marker to ground at degree of arm
    stemDist : distance between arm and stem
    """

    def __init__(self, aHeight, bHeight, cHeight, dHeight, stemDist, degree):
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