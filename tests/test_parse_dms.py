import unittest
from core.helper import Helper

class TestParseDMS(unittest.TestCase):

    def test_parse_ddmmss(self):
        # Eingabewert aus dem Beispiel
        dms_str = "04°17.2'N"

        # Erwarteter Dezimalwert
        expected_decimal = 4.28666666

        # Verwende die parse_ddmmss Funktion
        actual_decimal = Helper.parse_ddmmss(dms_str)

        # Überprüfe, ob der berechnete Wert dem erwarteten Wert entspricht
        self.assertAlmostEqual(actual_decimal, expected_decimal, places=7)

if __name__ == '__main__':
    unittest.main()