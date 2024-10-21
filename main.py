import argparse
from core.time import UTCDatetime, ArcToTime, TransitTime, ObservationTime
from core.altitude import AltitudeObserved, AltitudeSextant, AltitudeTrue, Altitude
from core.corrections import CorrectionSum, CorrectionDIP, CorrectionMonthly
from core.index_error import IndexError
from core.latitude import CalculatedLatitude, Latitude
from core.declination import Declination
from core.longitude import Longitude
from core.degree import Degree
from core.hour_angles import GreenwhichHourAngle, LocaleHourAngle
from core.time import UTCDatetime

def calculate_star_sight():
    star_sight_time=UTCDatetime(input("Enter the time for the star sight (YYYY-MM-DDTHH:MM:SS format): "))
    greenwhich_hour_angle_i = GreenwhichHourAngle(
        input("Enter the nearest GHA (in D°M'S\" format): "),
        UTCDatetime(input("Enter the time for the GHA (YYYY-MM-DDTHH:MM:SS format): "))
        )
    greenwhich_hour_angle_ii = GreenwhichHourAngle(
        input("Enter the second nearest GHA (in D°M'S\" format): "),
        UTCDatetime(input("Enter the time for the GHA (YYYY-MM-DDTHH:MM:SS format): "))
        )
    interpolated_gha = GreenwhichHourAngle.new_interpolated_gha(
        greenwhich_hour_angle_i,
        greenwhich_hour_angle_ii,
        star_sight_time
        )
    print(f"GHA: {interpolated_gha}")
    choosen_longitude = Longitude(input("Enter the choosen longitude (in D°M'S\" format): "))
    locale_hour_angle = LocaleHourAngle(interpolated_gha,choosen_longitude)
    print(f"LHA: {locale_hour_angle}")

def calculate_observation_time():
    print("Observation Time Calculation\n")
    
    longitude_str = input("Enter longitude (in D°M'S\" format, with direction E/W): ")
    longitude = Longitude(longitude_str) 
    
    arc_to_time = ArcToTime(longitude)
    print(f"ARC to time: {arc_to_time}")

    nautical_transit_time = TransitTime(
        arc_to_time,
        UTCDatetime(input("Enter Nautical Twilight at Greenwich (YYYY-MM-DDTHH:MM:SS format): "))
    )
    print(f"Nautical Twilight at Position: {nautical_transit_time}")

    civil_transit_time = TransitTime(
        arc_to_time,
        UTCDatetime(input("Enter Civil Twilight at Greenwich (YYYY-MM-DDTHH:MM:SS format): "))
    )
    print(f"Civil Twilight at Position: {civil_transit_time}")
    
    sunrise_transit_time = TransitTime(
        arc_to_time,
        UTCDatetime(input("Enter Sunrise at Greenwich (YYYY-MM-DDTHH:MM:SS format): "))
    )
    print(f"Sunrise at Position: {sunrise_transit_time}")
    
    observation_time = ObservationTime(nautical_transit_time,civil_transit_time,sunrise_transit_time)
    print(f"{observation_time}")

def calculate_time():
    print("Time Calculation\n")
    # TIME INPUTS
    longitude_str = input("Enter longitude (in D°M'S\" format, with direction E/W): ")
    longitude = Longitude(longitude_str) 
    
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
    declination_str = input("Enter declination (DEC in D°M'S\" format): ")
    declination = Declination(declination_str)
    estimated_latitude_str = input("Enter the estimated latitude (DEC in D°M'S\" format): ")
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
        choices=["time", "altitude", "latitude","observation_time","star_sight"], 
        help="Choose one or more calculations to perform: 'time', 'altitude', 'latitude'"
    )

    args = parser.parse_args()

    if "star_sight" in args.calculations:
        calculate_star_sight()
    if "observation_time" in args.calculations:
        calculate_observation_time()
    if "transittime" in args.calculations:
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
