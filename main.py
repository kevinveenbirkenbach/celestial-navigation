import argparse
from core.time import UTCDatetime, ArcToTime, TransitTime
from core.altitude import AltitudeObserved, AltitudeSextant, AltitudeTrue, Altitude
from core.corrections import CorrectionSum, CorrectionDIP, CorrectionMonthly
from core.index_error import IndexError
from core.latitude import CalculatedLatitude, Latitude
from core.declination import Declination
from core.longitude import Longitude
from core.degree import Degree

def calculate_time():
    print("Time Calculation\n")
    # TIME INPUTS
    longitude_str = input("Enter longitude (in D°M'S\" format, with direction E/W): ")
    longitude = Longitude(longitude_str)  # Verwende die Longitude Klasse
    
    arc_to_time = ArcToTime(longitude)
    print(f"ARC to time: {arc_to_time}")

    transit_greenwich_str = input("Enter GMT transit time at Greenwich (YYYY-MM-DDTHH:MM:SS format): ")
    transit_greenwich = UTCDatetime(transit_greenwich_str)

    # Calculate transit time at EP
    transit_calculator = TransitTime(arc_to_time, transit_greenwich)
    print(f"Transit Time: {transit_calculator}")

def calculate_altitude():
    print("Altitude Calculation\n")
    
    # SEXTANT ALTITUDE
    altitude_sextant = AltitudeSextant(
        input("Enter sextant altitude (SA in D°M'S\" format): ")
    )

    # INDEX ERROR
    index_error = IndexError(
        input("Enter index error (IE, in D°M'S\" format): ")
    )

    # OBSERVED ALTITUDE
    observed_altitude = AltitudeObserved(altitude_sextant,index_error)
    print(observed_altitude)

    # CORRECTIONS
    correction_dip = CorrectionDIP(
        input("Enter DIP Correction ( in D°M'S\" format): ")
    )
    correction_monthly = CorrectionMonthly(
        input("Enter Monthly Correction ( in D°M'S\" format): ")
    )
    correction_sum = CorrectionSum(correction_monthly, correction_dip)
    print(correction_sum)

    # TRUE ALTITUDE
    true_altitude = AltitudeTrue(altitude_sextant,correction_sum)
    print(true_altitude)

def calculate_latitude(true_altitude=False):
    print("Latitude Calculation\n")

    if not true_altitude:
        true_altitude_str = input("Enter True Altitute (DEC in D°M'S\" format): ")
        true_altitude = AltitudeTrue(true_altitude_str)

    # LATITUDE INPUTS
    declination_str = input("Enter declination (DEC in D°M'S\"(N\S) format): ")
    declination = Declination(declination_str)
    estimated_latitude_str = input("Enter the estimated latitude (DEC in D°M'S\"(N\S) format): ")
    estimated_latitude = Latitude(estimated_latitude_str)

    # Latitude Calculation
    latitude = CalculatedLatitude(true_altitude, declination, estimated_latitude)
    print(f"Zenith Distance (ZD): {latitude.zenith_distance.decimal}")
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
        true_altitude = calculate_altitude()
    if "latitude" in args.calculations:
        try:
            calculate_latitude(true_altitude)
        except NameError:
            calculate_latitude()

if __name__ == "__main__":
    main()
