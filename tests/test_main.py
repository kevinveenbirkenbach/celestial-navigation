import unittest
from unittest.mock import patch
from io import StringIO
from main import compass_values

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

if __name__ == '__main__':
    unittest.main()
