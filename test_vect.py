import unittest
import vect as vect


class VectTest(unittest.TestCase):
    def testNFromDecomp(self):
        nVect = vect.Vect.fromDecompedVects(0, 5)
        self.assertAlmostEqual(nVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(nVect.getAngle(), 0, 2)
        self.assertAlmostEqual(nVect.getV(), 5, 2)
        self.assertAlmostEqual(nVect.getH(), 0, 2)

    def testSFromDecomp(self):
        sVect = vect.Vect.fromDecompedVects(0, -5)
        self.assertAlmostEqual(sVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(sVect.getAngle(), 180, 2)
        self.assertAlmostEqual(sVect.getV(), -5, 2)
        self.assertAlmostEqual(sVect.getH(), 0, 2)

    def testEFromDecomp(self):
        sVect = vect.Vect.fromDecompedVects(5, 0)
        self.assertAlmostEqual(sVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(sVect.getAngle(), 90, 2)
        self.assertAlmostEqual(sVect.getV(), 0, 2)
        self.assertAlmostEqual(sVect.getH(), 5, 2)

    def testWFromDecomp(self):
        sVect = vect.Vect.fromDecompedVects(-5, 0)
        self.assertAlmostEqual(sVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(sVect.getAngle(), 270, 2)
        self.assertAlmostEqual(sVect.getV(), 0, 2)
        self.assertAlmostEqual(sVect.getH(), -5, 2)

    def testNEFromDecomp(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect.fromDecompedVects(3, 4)
        self.assertAlmostEqual(neVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(
            neVect.getAngle(), 36, 2)
        self.assertAlmostEqual(neVect.getV(), 4, 2)
        self.assertAlmostEqual(neVect.getH(), 3, 2)

    def testSEFromDecomp(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect.fromDecompedVects(3, -4)
        self.assertAlmostEqual(seVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(
            seVect.getAngle(), 143, 2)
        self.assertAlmostEqual(seVect.getV(), -4, 2)
        self.assertAlmostEqual(seVect.getH(), 3, 2)

    def testSWFromDecomp(self):
        # 3/4/5 triangle for simplicity
        swVect = vect.Vect.fromDecompedVects(-3, -4)
        self.assertAlmostEqual(swVect.getMagnitude(), 5, 2)
        self.assertAlmostEqual(
            swVect.getAngle(), 216, 2)
        self.assertAlmostEqual(swVect.getV(), -4, 2)
        self.assertAlmostEqual(swVect.getH(), -3, 2)

    def testNWFromDecomp(self):
        # 3/4/5 triangle for simplicity
        nwVect = vect.Vect.fromDecompedVects(-3, 4)
        self.assertAlmostEqual(nwVect.getMagnitude(), 5)
        self.assertAlmostEqual(
            nwVect.getAngle(), 323, 2)
        self.assertAlmostEqual(nwVect.getV(), 4, 2)
        self.assertAlmostEqual(nwVect.getH(), -3, 2)

    def testN(self):
        # 3/4/5 triangle for simplicity
        nVect = vect.Vect(5, 0)

        self.assertAlmostEqual(nVect.getV(), 5, 2)
        self.assertAlmostEqual(nVect.getH(), 0, 2)

    def testE(self):
        # 3/4/5 triangle for simplicity
        eVect = vect.Vect(5, 90)

        self.assertAlmostEqual(eVect.getV(), 0, 2)
        self.assertAlmostEqual(eVect.getH(), 5, 2)

    def testS(self):
        # 3/4/5 triangle for simplicity
        sVect = vect.Vect(5, 180)

        self.assertAlmostEqual(sVect.getV(), -5, 2)
        self.assertAlmostEqual(sVect.getH(), 0, 2)

    def testW(self):
        # 3/4/5 triangle for simplicity
        wVect = vect.Vect(5, 270)

        self.assertAlmostEqual(wVect.getV(), 0, 2)
        self.assertAlmostEqual(wVect.getH(), -5, 2)

    def testNE(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 53.130102354155978703144387440907)

        self.assertAlmostEqual(neVect.getV(), 3, 2)
        self.assertAlmostEqual(neVect.getH(), 4, 2)

    def testSE(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 143.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), -4, 2)
        self.assertAlmostEqual(seVect.getH(), 3, 2)

    def testSW(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 233.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), -3, 2)
        self.assertAlmostEqual(seVect.getH(), -4, 2)

    def testNW(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 323.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), 4, 2)
        self.assertAlmostEqual(seVect.getH(), -3, 2)


if __name__ == '__main__':
    unittest.main()
