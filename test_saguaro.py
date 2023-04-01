import unittest
import saguaro


class SaguaroTest(unittest.TestCase):
    def test_arm_length(self):
        # 3/4/5 right triangle for simplicity
        fiveArm = saguaro.SaguaroArm(3, 1, 7, 1, 3, 0)

        self.assertEqual(fiveArm.getLength(), 5)

        # 6/8/10 but with uneven ground
        tenArm = saguaro.SaguaroArm(6, 2, 16, 4, 6, 0)
        self.assertEqual(tenArm.getEmergence(), 5)
        self.assertEqual(tenArm.getLength(), 10)

    if __name__ == '__main__':
        unittest.main()
