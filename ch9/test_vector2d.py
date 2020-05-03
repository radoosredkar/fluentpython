from unittest import TestCase

from ch9.vector import Vector2d

vctr = Vector2d(2, 3)


class TestVector2d(TestCase):
    def test_representation(self):
        self.assertEqual(vctr.x, 2)
        self.assertEqual(vctr.y, 3)
        self.assertEqual(str(vctr), "(2, 3)")

    def test_clone(self):
        vector_clone = eval(repr(vctr))
        self.assertTrue(vctr == vector_clone)

    def test_bool(self):
        self.assertTrue(bool(vctr))

    def test_bytes(self):
        byts = (bytes(vctr))
        vect_from_bytes = Vector2d.frombytes(byts)
        self.assertEqual(vctr, vect_from_bytes)

    def test_format(self):
        self.assertEqual(format(vctr), "(2, 3)")
        self.assertEqual(format(vctr, "2f"), "(2.000000, 3.000000)")
        self.assertEqual(format(vctr, ".3e"), "(2.000e+00, 3.000e+00)")
        self.assertEqual(format(vctr, "p"), "<3.605551275463989, 0.5880026035475675>")

    def test_hash(self):
        self.assertEqual(hash(vctr), 1)
        set({vctr, Vector2d(3, 5)})

    def test_readonly(self):
        with self.assertRaises(AttributeError):
            vctr.x = 42
        with self.assertRaises(AttributeError):
            vctr.y = 42

    def test_changetypecode(self):
        dumped = bytes(vctr)
        self.assertEqual(dumped, b"d\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@")
        vector_clone = eval(repr(vctr))
        vector_clone.typecode = "f"
        dumped = bytes(vector_clone)
        self.assertEqual(dumped, b'f\x00\x00\x00@\x00\x00@@')
