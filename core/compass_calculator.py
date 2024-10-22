from core.compass import CompassTrueBearing, CompassBearing, CompassVariation, CompassDeviation, CompassMagneticBearing

class CompassCalculator:
    """ Created with CHATGPT @See https://chatgpt.com/share/671726d6-4138-800f-83b0-6b20f9a0ce06"""
    def __init__(self, known_values, values):
        self.known_values = known_values
        self.values = values

    def calculate_magnetic_bearing(self):
        if self.known_values["true_bearing"] and self.known_values["variation"] and not self.known_values["magnetic_bearing"]:
            self.values["magnetic_bearing"] = CompassMagneticBearing(CompassTrueBearing(self.values["true_bearing"]), CompassVariation(self.values["variation"]))
            self.known_values["magnetic_bearing"] = True
            print(f"Calculated Magnetic Bearing: {self.values['magnetic_bearing']}")

    def calculate_true_bearing(self):
        if self.known_values["magnetic_bearing"] and self.known_values["variation"] and not self.known_values["true_bearing"]:
            self.values["true_bearing"] = CompassTrueBearing(CompassMagneticBearing(self.values["magnetic_bearing"]), CompassVariation(self.values["variation"]))
            self.known_values["true_bearing"] = True
            print(f"Calculated True Bearing: {self.values['true_bearing']}")

    def calculate_compass_bearing(self):
        if self.known_values["magnetic_bearing"] and self.known_values["deviation"] and not self.known_values["compass_bearing"]:
            self.values["compass_bearing"] = CompassBearing(CompassMagneticBearing(self.values["magnetic_bearing"]), CompassDeviation(self.values["deviation"]))
            self.known_values["compass_bearing"] = True
            print(f"Calculated Compass Bearing: {self.values['compass_bearing']}")

    def calculate_deviation(self):
        if self.known_values["compass_bearing"] and self.known_values["magnetic_bearing"] and not self.known_values["deviation"]:
            self.values["deviation"] = CompassDeviation(CompassBearing(self.values["compass_bearing"]),CompassMagneticBearing(self.values["magnetic_bearing"]))
            self.known_values["deviation"] = True
            print(f"Calculated Compass Deviation: {self.values['deviation']}")

    def calculate_variation(self):
        if self.known_values["true_bearing"] and self.known_values["magnetic_bearing"] and not self.known_values["variation"]:
            self.values["variation"] = CompassVariation(CompassTrueBearing(self.values["true_bearing"]), CompassMagneticBearing(self.values["magnetic_bearing"]))
            self.known_values["variation"] = True
            print(f"Calculated Compass Variation: {self.values['variation']}")

    def calculate_all(self):
        previous_known = None

        # Iteriere, bis keine neuen Werte mehr berechnet werden
        while previous_known != self.known_values:
            previous_known = self.known_values.copy()

            # Berechnungen ausführen
            self.calculate_magnetic_bearing()
            self.calculate_true_bearing()
            self.calculate_compass_bearing()
            self.calculate_deviation()
            self.calculate_variation()

    def __str__(self):
        print("\nFinal Compass Values:")
        print(f"True Bearing: {self.values.get('true_bearing', 'Unknown')}")
        print(f"Magnetic Bearing: {self.values.get('magnetic_bearing', 'Unknown')}")
        print(f"Compass Bearing: {self.values.get('compass_bearing', 'Unknown')}")
        print(f"Compass Variation: {self.values.get('variation', 'Unknown')}")
        print(f"Compass Deviation: {self.values.get('deviation', 'Unknown')}")
