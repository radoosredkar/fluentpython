from unittest import TestCase

from ch1.NumericTypes import Vector


class TestVector(TestCase):

    def testAddVectorOk(self):
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        self.assertTrue(v1 + v2, Vector(4, 5))

    def testMultiplyVectorOk(self):
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        print(v1)
        self.assertTrue(v1 * v2, Vector(4, 4))

