import argparse
from core.transit_time import TransitTime
from core.altitude import Altitude, AltitudeSextant, AltitudeTrue
from core.index_error import IndexError
from core.latitude import Latitude
from core.declination import Declination
from core.longitude import Longitude
from core.degree import Degree

def calculate_time():
    print("Time Calculation\n")
    # TIME INPUTS
    longitude_str = input("Enter estimated longitude (in D°M'S\" format, with direction E/W): ")
    longitude = Longitude(longitude_str)  # Verwende die Longitude Klasse
    
    transit_greenwich_str = input("Enter GMT transit time at Greenwich (hh:mm:ss format): ")

    # Calculate transit time at EP
    transit_calculator = TransitTime(longitude, transit_greenwich_str)
    print(transit_calculator)
    transit_ep_time = transit_calculator.calculate_transit_time_at_ep()

def calculate_altitude():
    print("Altitude Calculation\n")
    
    # ALTITUDE INPUTS
    sextant_altitude_str = input("Enter sextant altitude (SA in D°M'S\" format): ")
    index_error_str = input("Enter index error (IE, in D°M'S\" format): ")

    # Verwende die Altitude Klasse für Höhe und Fehler
    sextant_altitude = AltitudeSextant(sextant_altitude_str)
    index_error = IndexError(index_error_str)

    # Altitude Calculation
    altitude = AltitudeTrue(sextant_altitude.decimal, index_error.decimal, 0)

    # Calculate Observed Altitude
    observed_altitude = altitude.calculate_observed_altitude()
    print(f"Observed Altitude (OA): {observed_altitude}")

    # Now that Observed Altitude is available, request Total Corrections
    total_correction_str = input("Enter total correction (from table): ")
    total_correction = Altitude(total_correction_str)
    altitude.monthly_correction = total_correction.decimal

    # Calculate True Altitude
    true_altitude = altitude.calculate_true_altitude()
    print(f"True Altitude (TA): {true_altitude}")

def calculate_latitude(true_altitude=False):
    print("Latitude Calculation\n")

    if not true_altitude:
        true_altitude_str = input("Enter True Altitute (DEC in D°M'S\" format): ")
        true_altitude = Altitude(true_altitude_str)

    # LATITUDE INPUTS
    declination_str = input("Enter declination (DEC in D°M'S\" format): ")
    declination = Declination(declination_str)

    # Latitude Calculation
    latitude = Latitude(true_altitude.decimal, declination.decimal)
    lat = latitude.calculate_latitude()

    print(f"True Altitude (TA): {true_altitude}")
    print(f"Latitude: {lat}")

def main():
    parser = argparse.ArgumentParser(description="Celestial Navigation Calculations")
    parser.add_argument(
        "calculations", 
        nargs="+",  # Allows multiple choices to be passed as a list
        choices=["time", "altitude", "latitude"], 
        help="Choose one or more calculations to perform: 'time', 'altitude', 'latitude'"
    )

    args = parser.parse_args()

    # Execute the selected calculations
    if "time" in args.calculations:
        calculate_time()
    if "altitude" in args.calculations:
        true_altitude = calculate_altitude()
    if "latitude" in args.calculations:
        if true_altitude:
            calculate_latitude(true_altitude)
        else:
            calculate_latitude()

if __name__ == "__main__":
    main()
