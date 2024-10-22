import unittest
from core.degree import Degree
from core.compass import (
    Compass,
    CompassVariation,
    CompassDeviation,
    CompassMagneticBearing,
    CompassBearing,
    CompassTrueBearing,
)

class TestCompassClasses(unittest.TestCase):

    def test_compass_variation_west(self):
        magnetic_bearing = CompassMagneticBearing(CompassTrueBearing(90), CompassVariation("5°00'W"))
        self.assertEqual(magnetic_bearing.decimal, 95)

    def test_compass_variation_east(self):
        magnetic_bearing = CompassMagneticBearing(CompassTrueBearing(90), CompassVariation("5°00'E"))
        self.assertEqual(magnetic_bearing.decimal, 85)

    def test_compass_deviation_neutral(self):
        compass_bearing = CompassBearing(CompassMagneticBearing(95), CompassDeviation(3))
        self.assertEqual(compass_bearing.decimal, 92)

    def test_compass_deviation_east(self):
        compass_bearing = CompassBearing(CompassMagneticBearing(95), CompassDeviation("3°00'E"))
        self.assertEqual(compass_bearing.decimal, 92)

    def test_compass_deviation_west(self):
        compass_bearing = CompassBearing(CompassMagneticBearing(85), CompassDeviation("5°00'W"))
        self.assertEqual(compass_bearing.decimal, 90)

    def test_compass_true_bearing_east(self):
        true_bearing = CompassTrueBearing(CompassMagneticBearing(85), CompassVariation("5°00'E"))
        self.assertEqual(true_bearing.decimal, 80)

    def test_compass_true_bearing_west(self):
        true_bearing = CompassTrueBearing(CompassMagneticBearing(85), CompassVariation("5°00'W"))
        self.assertEqual(true_bearing.decimal, 90)

    def test_invalid_compass_variation(self):
        with self.assertRaises(TypeError):
            CompassVariation(Degree(90), "invalid_type")

    def test_invalid_number_of_arguments(self):
        with self.assertRaises(TypeError):
            Compass(True, Degree(90))  # Should raise TypeError for wrong number of arguments

if __name__ == '__main__':
    unittest.main()
