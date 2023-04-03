import unittest
import saguaro


class SaguaroTest(unittest.TestCase):
    def test_saguaro_overall_N(self):
        nSag = saguaro.Saguaro(10)
        nSag.addArm(6, 2, 16, 4, 6, 0)
        overallV = nSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(v, 5)

        nSag.addArm(3, 1, 7, 1, 3, 180)
        overallV = nSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(v, 3.5)

    def test_saguaro_overall_S(self):
        sSag = saguaro.Saguaro(10)
        sSag.addArm(6, 2, 16, 4, 6, 180)
        overallV = sSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(v, -5)

        sSag.addArm(3, 1, 7, 1, 3, 0)
        overallV = sSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 0)
        self.assertAlmostEqual(v, -3.5)

    def test_saguaro_overall_E(self):
        eSag = saguaro.Saguaro(10)
        eSag.addArm(6, 2, 16, 4, 6, 90)
        overallV = eSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 5)
        self.assertAlmostEqual(v, 0)

        eSag.addArm(3, 1, 7, 1, 3, 270)
        overallV = eSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, 3.5)
        self.assertAlmostEqual(v, 0)

    def test_saguaro_overall_W(self):
        wSag = saguaro.Saguaro(10)
        wSag.addArm(6, 2, 16, 4, 6, 270)
        overallV = wSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, -5)
        self.assertAlmostEqual(v, 0)

        wSag.addArm(3, 1, 7, 1, 3, 90)
        overallV = wSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertAlmostEqual(h, -3.5)
        self.assertAlmostEqual(v, 0)

    def test_saguaro_overall_NE(self):
        # 6/8/10 at half height
        neSag = saguaro.Saguaro(10)
        neSag.addArm(6, 2, 16, 4, 6, 45)
        overallV = neSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()

        self.assertAlmostEqual(h, 3.5355339059327376220042218105242)
        self.assertAlmostEqual(v, 3.5355339059327376220042218105242)
        self.assertAlmostEqual(overallV.getAngle(), 45)

        neSag.addArm(3, 1, 7, 1, 3, 300)
        overallV = neSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertTrue(h > 0)
        self.assertTrue(v > 0)

    def test_saguaro_overall_SE(self):
        # 6/8/10 at half height
        seSag = saguaro.Saguaro(10)
        seSag.addArm(6, 2, 16, 4, 6, 135)
        overallV = seSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()

        self.assertAlmostEqual(h, 3.5355339059327376220042218105242)
        self.assertAlmostEqual(v, -3.5355339059327376220042218105242)
        self.assertAlmostEqual(overallV.getAngle(), 135)

        seSag.addArm(3, 1, 7, 1, 3, 300)
        overallV = seSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertTrue(h > 0)
        self.assertTrue(v < 0)

    def test_saguaro_overall_SW(self):
        # 6/8/10 at half height
        swSag = saguaro.Saguaro(10)
        swSag.addArm(6, 2, 16, 4, 6, 225)
        overallV = swSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()

        self.assertAlmostEqual(h, -3.5355339059327376220042218105242)
        self.assertAlmostEqual(v, -3.5355339059327376220042218105242)
        self.assertAlmostEqual(overallV.getAngle(), 225)

        swSag.addArm(3, 1, 7, 1, 3, 300)
        overallV = swSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertTrue(h < 0)
        self.assertTrue(v < 0)

    def test_saguaro_overall_NW(self):
        # 6/8/10 at half height
        swSag = saguaro.Saguaro(10)
        swSag.addArm(6, 2, 16, 4, 6, 315)
        overallV = swSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()

        self.assertAlmostEqual(h, -3.5355339059327376220042218105242)
        self.assertAlmostEqual(v, 3.5355339059327376220042218105242)
        self.assertAlmostEqual(overallV.getAngle(), 315)

        swSag.addArm(3, 1, 7, 1, 3, 135)
        overallV = swSag.getOverallVect()
        h, v = overallV.getH(), overallV.getV()
        self.assertTrue(h < 0)
        self.assertTrue(v > 0)

    def test_arm_length_and_magnitude(self):
        # 3/4/5 right triangle for simplicity
        fiveArm = saguaro.SaguaroArm(3, 1, 7, 1, 3, 0, 10)

        self.assertEqual(fiveArm.getLength(), 5)
        self.assertAlmostEqual(fiveArm.getMagnitude(), 1.5)

        # 6/8/10 but with uneven ground
        tenArm = saguaro.SaguaroArm(6, 2, 16, 4, 6, 0, 10)
        self.assertEqual(tenArm.getEmergence(), 5)
        self.assertEqual(tenArm.getLength(), 10)
        self.assertAlmostEqual(tenArm.getMagnitude(), 5)

    def test_arm_vectors_N(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 0, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 0)
        self.assertAlmostEqual(sq2Y, 1.4142135623730950488016887242097)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 0, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, 0)
        self.assertAlmostEqual(sq2YH, .70710678118654752440084436210485)

        sqrtTwoArm2 = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 360, 10)
        self.assertAlmostEqual(sqrtTwoArm2.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm2.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm2.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 0)
        self.assertAlmostEqual(sq2Y, 1.4142135623730950488016887242097)

        sqTwoHalfWay2 = saguaro.SaguaroArm(5, 1, 6, 1, 1, 360, 10)
        self.assertAlmostEqual(sqTwoHalfWay2.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay2.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay2.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, 0)
        self.assertAlmostEqual(sq2YH, .70710678118654752440084436210485)

    def test_arm_vectors_E(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 90, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 1.4142135623730950488016887242097)
        self.assertAlmostEqual(sq2Y, 0)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 90, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, .70710678118654752440084436210485)
        self.assertAlmostEqual(sq2YH, 0)

    def test_arm_vectors_S(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 180, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 0)
        self.assertAlmostEqual(sq2Y, -1 * 1.4142135623730950488016887242097)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 180, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, 0)
        self.assertAlmostEqual(sq2YH, -1 * .70710678118654752440084436210485)

    def test_arm_vectors_W(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 270, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, -1 * 1.4142135623730950488016887242097)
        self.assertAlmostEqual(sq2Y, 0)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 270, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, -1 * .70710678118654752440084436210485)
        self.assertAlmostEqual(sq2YH, 0)

    def test_arm_vectors_NE(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 45, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 1)
        self.assertAlmostEqual(sq2Y, 1)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 45, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, .5)
        self.assertAlmostEqual(sq2YH, .5)

    def test_arm_vectors_SE(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 135, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, 1)
        self.assertAlmostEqual(sq2Y, -1)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 135, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, .5)
        self.assertAlmostEqual(sq2YH, -1 * .5)

    def test_arm_vectors_SW(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 225, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, -1)
        self.assertAlmostEqual(sq2Y, -1)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 225, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, -1 * .5)
        self.assertAlmostEqual(sq2YH, -1 * .5)

    def test_arm_vectors_NW(self):
        # 1/1/sqrt(2) right triangle for simplicity
        sqrtTwoArm = saguaro.SaguaroArm(
            10, 1, 11, 1, 1, 315, 10)
        self.assertAlmostEqual(sqrtTwoArm.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(sqrtTwoArm.getMagnitude(),
                               1.4142135623730950488016887242097)

        sq2H, sq2Y = sqrtTwoArm.getAdjustedVectors()
        self.assertAlmostEqual(sq2H, -1)
        self.assertAlmostEqual(sq2Y, 1)

        sqTwoHalfWay = saguaro.SaguaroArm(5, 1, 6, 1, 1, 315, 10)
        self.assertAlmostEqual(sqTwoHalfWay.getLength(),
                               1.4142135623730950488016887242097)
        self.assertAlmostEqual(
            sqTwoHalfWay.getMagnitude(), .70710678118654752440084436210485)

        sq2HH, sq2YH = sqTwoHalfWay.getAdjustedVectors()
        self.assertAlmostEqual(sq2HH, -1 * .5)
        self.assertAlmostEqual(sq2YH, .5)

    if __name__ == '__main__':
        unittest.main()
