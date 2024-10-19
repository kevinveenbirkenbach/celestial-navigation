import unittest
from datetime import timedelta
from core.transit_time import TransitTimeCalculator
from core.celestial import CelestialNavigation
from core.helper import Helper

class TestMainSight(unittest.TestCase):

    def test_transit_time(self):
        # Eingabewerte aus dem Beispiel
        longitude_str = "25°16'W"
        transit_greenwich_str = "11:49"

        # Erwartetes Ergebnis
        expected_transit_time = "13:30:04"  # Transitzeit an EP aus dem Beispiel

        # Transit Time Calculation
        calculator = TransitTimeCalculator(longitude_str, transit_greenwich_str)
        transit_ep_time = calculator.calculate_transit_time_at_ep()

        # Konvertiere das Ergebnis in eine Zeitdarstellung
        actual_transit_time = str(transit_ep_time)

        self.assertEqual(actual_transit_time, expected_transit_time)

    def test_celestial_navigation(self):
        # Eingabewerte aus dem Beispiel
        sextant_altitude_str = "77°00'"
        index_error = 0.0
        observed_altitude_str = "77°00'"
        monthly_correction = 0.1
        declination_str = "04°17.2'N"

        # Erwartete Ergebnisse aus dem Beispiel
        expected_true_altitude = 77.428  # Berechnet: TA = 77°42.8'
        expected_latitude = 8.30  # Berechnete Breite: 08°30'N

        # Celestial Navigation Calculation
        celestial_navigation = CelestialNavigation(sextant_altitude_str, index_error, monthly_correction, declination_str)
        true_altitude = celestial_navigation.calculate_true_altitude()
        latitude = celestial_navigation.calculate_latitude()

        # Vergleiche die berechneten Werte mit den erwarteten Werten
        self.assertAlmostEqual(true_altitude, expected_true_altitude, places=2)
        self.assertAlmostEqual(latitude, expected_latitude, places=2)

if __name__ == '__main__':
    unittest.main()
