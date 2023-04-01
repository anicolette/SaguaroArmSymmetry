import unittest
import vect


class VectTest(unittest.TestCase):
    def testN(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 0)
        neVect2 = vect.Vect(5, 360)

        self.assertAlmostEqual(neVect.getV(), 5)
        self.assertAlmostEqual(neVect.getH(), 0)

    def testE(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 90)

        self.assertAlmostEqual(neVect.getV(), 0)
        self.assertAlmostEqual(neVect.getH(), 5)

    def testS(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 180)

        self.assertAlmostEqual(neVect.getV(), -5)
        self.assertAlmostEqual(neVect.getH(), 0)

    def testW(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 270)

        self.assertAlmostEqual(neVect.getV(), 0)
        self.assertAlmostEqual(neVect.getH(), -5)

    def testNE(self):
        # 3/4/5 triangle for simplicity
        neVect = vect.Vect(5, 53.130102354155978703144387440907)

        self.assertAlmostEqual(neVect.getV(), 4)
        self.assertAlmostEqual(neVect.getH(), 3)

    def testSE(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 143.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), -4)
        self.assertAlmostEqual(seVect.getH(), 3)

    def testSW(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 233.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), -4)
        self.assertAlmostEqual(seVect.getH(), -3)

    def testNW(self):
        # 3/4/5 triangle for simplicity
        seVect = vect.Vect(5, 323.130102354155978703144387440907)

        self.assertAlmostEqual(seVect.getV(), 4)
        self.assertAlmostEqual(seVect.getH(), -3)
