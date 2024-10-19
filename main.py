import argparse
from core.transit_time import TransitTimeCalculator
from core.celestial import CelestialNavigation
from core.helper import Helper

def calculate_time():
    print("Time Calculation\n")
    # TIME INPUTS
    longitude_str = Helper.get_input("Enter estimated longitude (in D°M'S\" format, with direction E/W): ")
    transit_greenwich_str = Helper.get_input("Enter GMT transit time at Greenwich (hh:mm:ss format): ")

    # Calculate transit time at EP
    transit_calculator = TransitTimeCalculator(longitude_str, transit_greenwich_str)
    transit_ep_time = transit_calculator.calculate_transit_time_at_ep()
    print(f"ARC to time: {transit_calculator.get_arc_to_time_string()}")
    print(f"Transit Time at EP: {transit_ep_time}")

def calculate_altitude():
    print("Altitude Calculation\n")
    # ALTITUDE INPUTS
    sextant_altitude_str = Helper.get_input("Enter sextant altitude (SA in D°M'S\" format): ")
    index_error = float(Helper.get_input("Enter index error (IE, positive or negative): "))

    # Celestial Navigation Calculations
    celestial_navigation = CelestialNavigation(sextant_altitude_str, index_error, 0, 0)  # Placeholder for monthly_correction and declination

    # Calculate Observed Altitude
    observed_altitude = celestial_navigation.calculate_observed_altitude()
    print(f"Observed Altitude (OA): {observed_altitude}")

    # Now that Observed Altitude is available, request Total Corrections
    total_correction = float(Helper.get_input("Enter total correction (from table): "))
    celestial_navigation.monthly_correction = total_correction

    # Calculate True Altitude
    true_altitude = celestial_navigation.calculate_true_altitude()
    print(f"True Altitude (TA): {true_altitude}")

def calculate_latitude():
    print("Latitude Calculation\n")
    # ALTITUDE INPUTS
    sextant_altitude_str = Helper.get_input("Enter sextant altitude (SA in D°M'S\" format): ")
    index_error = float(Helper.get_input("Enter index error (IE, positive or negative): "))

    # Celestial Navigation Calculations
    celestial_navigation = CelestialNavigation(sextant_altitude_str, index_error, 0, 0)  # Placeholder for monthly_correction and declination

    # Calculate Observed Altitude
    observed_altitude = celestial_navigation.calculate_observed_altitude()
    print(f"Observed Altitude (OA): {observed_altitude}")

    # Now that Observed Altitude is available, request Total Corrections
    total_correction = float(Helper.get_input("Enter total correction (from table): "))
    celestial_navigation.monthly_correction = total_correction

    # LATITUDE INPUTS
    declination_str = Helper.get_input("Enter declination (DEC in D°M'S\" format): ")
    celestial_navigation.declination = Helper.parse_dms(declination_str)

    # Calculate True Altitude and Latitude
    true_altitude = celestial_navigation.calculate_true_altitude()
    latitude = celestial_navigation.calculate_latitude()

    print(f"True Altitude (TA): {true_altitude}")
    print(f"Latitude: {latitude}")

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
        calculate_altitude()
    if "latitude" in args.calculations:
        calculate_latitude()

if __name__ == "__main__":
    main()
