import unittest
from core.latitude import Latitude
from core.longitude import Longitude
from core.degree import Degree

class TestDegreeConversion(unittest.TestCase):

    def test_longitude_east(self):
        lon = Longitude(2.3522)  # Longitude of Paris
        self.assertEqual(str(lon), "002°21'07.92\"E", "Failed for Longitude (East)")

    def test_longitude_west(self):
        lon = Longitude(-74.0060)  # Longitude of New York
        self.assertEqual(str(lon), "074°00'21.60\"W", "Failed for Longitude (West)")

if __name__ == '__main__':
    unittest.main()
