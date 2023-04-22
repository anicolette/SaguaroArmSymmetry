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
        return round(self.v.getH(), 2), round(self.v.getV(), 2)

    def getMagnitude(self):
        return self.adjustedMagnitude

    def getEmergence(self):
        return self.emergence

    def getLength(self):
        return self.length

    def getDegree(self):
        return int(self.degree)


class Saguaro:
    def __init__(self, plotNo, sID, recorder, date, easting, northing, height):
        self.plotNo = plotNo
        self.sID = sID
        self.recorder = recorder
        self.date = date
        self.easting = easting
        self.northing = northing
        self.height = float(height)
        self.vSum = 0.0
        self.hSum = 0.0
        self.asymTotal = 0.0
        self.arms = []

    def getOutputRow(self):
        overallVect = self.getOverallVect()
        return "%d,%d,%s,%s,%d,%d,%.2f,%d,%.2f,%.2f,%d" % (self.plotNo, self.sID, self.recorder, self.date, self.easting, self.northing, self.height, len(self.arms), self.getSymmetryScore(), overallVect.getMagnitude(), overallVect.getAngle())

    """
        Symmetry score is the magnitude of the sum of adjusted vectors divided by 
        the magnitude of a theoretical vector if all arms pointed in the same direction.
        A score of 0 would indicate perfect symmetry, while a score of 1 would indicate
        complete asymmetry.
    """

    def getSymmetryScore(self):
        if len(self.arms) == 0:
            return 0.0
        if len(self.arms) == 1:
            return 1.0
        overallVect = self.getOverallVect()
        return overallVect.getMagnitude() / self.asymTotal

    def getHeight(self):
        return self.height

    def addArm(self, aHeight, bHeight, cHeight, dHeight, stemDist, degree):
        newArm = SaguaroArm(aHeight, bHeight, cHeight,
                            dHeight, stemDist, degree, self.height)
        newH, newV = newArm.getAdjustedVectors()
        self.hSum += newH
        self.vSum += newV
        self.asymTotal += newArm.getMagnitude()
        self.arms.append(newArm)

    def getOverallVect(self):
        return vect.Vect.fromDecompedVects(self.hSum, self.vSum)
