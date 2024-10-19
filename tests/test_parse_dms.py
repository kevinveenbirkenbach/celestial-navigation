import unittest
from core.helper import Helper

class TestParseDMS(unittest.TestCase):

    def test_parse_dms(self):
        # Eingabewert aus dem Beispiel
        dms_str = "04°17.2'N"

        # Erwarteter Dezimalwert
        expected_decimal = 4.28666666

        # Verwende die parse_dms Funktion
        actual_decimal = Helper.parse_dms(dms_str)

        # Überprüfe, ob der berechnete Wert dem erwarteten Wert entspricht
        self.assertAlmostEqual(actual_decimal, expected_decimal, places=7)

if __name__ == '__main__':
    unittest.main()