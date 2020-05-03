from unittest import TestCase
import array
from ch10.vectorV2 import Vector2d

vctr = Vector2d([2, 3])


class TestVector2d(TestCase):
    def test_representation(self):
        self.assertEqual(repr(Vector2d([3.1, 4.2])), "Vector2d([3.1, 4.2])")

    def test_clone(self):
        vector_clone = eval(repr(vctr))
        self.assertTrue(vctr == vector_clone)

    def test_bool(self):
        self.assertTrue(bool(vctr))

    def test_bytes(self):
        byts = (bytes(vctr))
        vect_from_bytes = Vector2d.frombytes(byts)
        self.assertEqual(vctr, vect_from_bytes)


    def test_changetypecode(self):
        dumped = bytes(vctr)
        self.assertEqual(dumped, b"d\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@")
        vector_clone = eval(repr(vctr))
        vector_clone.typecode = "f"
        dumped = bytes(vector_clone)
        self.assertEqual(dumped, b'f\x00\x00\x00@\x00\x00@@')

    def test_len(self):
        self.assertEqual(len(vctr), 2)

    def test_slicing(self):
        vector = Vector2d([1,2,3,4,5,6])
        self.assertEqual(vector[0], 1)
        self.assertEqual(vector[1:4], array.array('d', [2.0, 3.0, 4.0]))

    def test_vect_by_name(self):
        vector = Vector2d(range(10))
        self.assertEqual(vector.x, 0)
        self.assertEqual((vector.y, vector.z, vector.t), (1, 2, 3))

    def test_format(self):
        self.assertEqual(format(Vector2d([-1, -1, -1, -1]), 'h'), '<2.0, 2.0943951023931957, 2.186276035465284, 3.9269908169872414>')
