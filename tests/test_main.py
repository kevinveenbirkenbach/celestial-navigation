import unittest
from unittest.mock import patch
from io import StringIO
from main import compass_values
from core.altitude import AltitudeTrue
import sys

class TestCompassValues(unittest.TestCase):

    @patch('builtins.input', side_effect=['', '89', '', '92', '6°0\'W', ''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculate_compass_values(self, mock_stdout, mock_input):
        """
        Test the calculation of compass values when some are known and others are calculated.
        """
        compass_values()  # Call the function that prompts user for inputs and calculates values

        output = mock_stdout.getvalue()

        # Check if the True Bearing and Compass Bearing have been correctly calculated and printed
        self.assertIn("Calculated True Bearing", output)
        self.assertIn("003°00'00.00", output)  # Expected True Bearing result
        self.assertIn("Calculated Compass Bearing", output)
        self.assertIn("095°00'00.00", output)  # Expected Compass Bearing result

class TestCalculateAltitude(unittest.TestCase):

    def setUp(self):
        # Umleiten von stdout und stdin
        self.old_stdout = sys.stdout
        self.old_stdin = sys.stdin
        self.output = StringIO()  # Puffer für die Ausgabe
        sys.stdout = self.output  # Umleitung der Ausgabe zu stdout

    def tearDown(self):
        # Wiederherstellen von stdout und stdin
        sys.stdout = self.old_stdout
        sys.stdin = self.old_stdin

def test_calculate_altitude(self):
    # Simulierte Benutzereingaben für calculate_altitude
    input_data = (
        "+37°49.3'\n"     # Sextant altitude
        "-00°00.3'\n"     # Index error
        "-00°03'\n"       # Total correction
        "+00°15.0'\n"     # Apparent correction
    )
    sys.stdin = StringIO(input_data)  # Simulierte Eingaben

    # Importiere die zu testende Funktion
    from main import calculate_altitude

    # Führe die Funktion aus
    result = calculate_altitude()

    # Angepasster erwarteter Output mit einer zusätzlichen Leerzeile nach "Altitude Calculation"
    expected_output = (
        "Altitude Calculation\n\n"
        "Enter sextant altitude (SA in D°M'S\" format): Enter index error (IE, in D°M'S\" format): Observed Altitute (OA): 37°49'00.00\"\n"
        "Enter Total Correction (in D°M'S\" format): Observed Altitude Correction: -000°03'00.00\"\n"
        "Apparant Altitute: 37°46'00.00\"\n"
        "Enter Apparent Correction (in D°M'S\" format): True Altitude (TA): 38°01'00.00\"\n"
    )
    
    # Vergleiche die tatsächliche Ausgabe mit der erwarteten
    self.assertEqual(self.output.getvalue(), expected_output)

    # Überprüfe das Ergebnis der Funktion (True Altitude)
    self.assertIsInstance(result, AltitudeTrue)
    self.assertEqual(result.decimal, 38.01666667)  # Erwarteter Wert von 38°01'00.00" in Dezimalgrad

if __name__ == '__main__':
    unittest.main()
