from core.time import UTCDatetime, ArcToTime, TransitTime, ObservationTime
from core.altitude import AltitudeObserved, AltitudeSextant, AltitudeTrue, Altitude, AltitudeApperant
from core.corrections import ObservedAltitudeCorrection, ObservedAltitudeCorrectionDIP, ObservedAltitudeCorrectionMonthly, ApparentAltitudeCorrection
from core.index_error import IndexError
from core.coordinates_celestial import Declination
from core.coordinates_geographic import Longitude, CalculatedLatitude, Latitude
from core.degree import Degree
from core.hour_angles import GreenwhichHourAngle, LocaleHourAngle
from core.compass_calculator import CompassCalculator


def calculate_star_sight():
    star_sight_time = UTCDatetime(input("Enter the time for the star sight (YYYY-MM-DDTHH:MM:SS format): "))
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
    chosen_longitude = Longitude(input("Enter the chosen longitude (in D°M'S\" format): "))
    locale_hour_angle = LocaleHourAngle(interpolated_gha, chosen_longitude)
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
    
    observation_time = ObservationTime(nautical_transit_time, civil_transit_time, sunrise_transit_time)
    print(f"{observation_time}")

def calculate_time():
    print("Time Calculation\n")
    longitude_str = input("Enter longitude (in D°M'S\" format, with direction E/W): ")
    longitude = Longitude(longitude_str) 
    
    arc_to_time = ArcToTime(longitude)
    print(f"ARC to time: {arc_to_time}")

    transit_greenwich_str = input("Enter GMT transit time at Greenwich (YYYY-MM-DDTHH:MM:SS format): ")
    transit_greenwich = UTCDatetime(transit_greenwich_str)

    transit_calculator = TransitTime(arc_to_time, transit_greenwich)
    print(f"Transit Time: {transit_calculator}")

def calculate_altitude():
    print("Altitude Calculation\n")
    
    altitude_sextant = AltitudeSextant(
        input("Enter sextant altitude (SA in D°M'S\" format): ")
    )

    index_error = IndexError(
        input("Enter index error (IE, in D°M'S\" format): ")
    )

    observed_altitude = AltitudeObserved(altitude_sextant, index_error)
    print(f"Observed Altitute (OA): {observed_altitude}")

    observed_altitude_correction_string = input("Enter Total Correction (in D°M'S\" format): ")

    if bool(observed_altitude_correction_string):
        observed_altitude_correction = ObservedAltitudeCorrection(observed_altitude_correction_string)
    else:
        correction_dip = ObservedAltitudeCorrectionDIP(
            input("Enter DIP Correction (in D°M'S\" format): ")
        )
        correction_monthly = ObservedAltitudeCorrectionMonthly(
            input("Enter Monthly Correction (in D°M'S\" format): ")
        )
        observed_altitude_correction = ObservedAltitudeCorrection(correction_monthly, correction_dip)
    print(f"Observed Altitude Correction: {observed_altitude_correction}")
    
    apparant_altitude = AltitudeApperant(observed_altitude, observed_altitude_correction)
    print(f"Apparant Altitute: {apparant_altitude}")

    apparant_altitude_correction_string = input("Enter Apparent Correction (in D°M'S\" format): ")
    apparant_altitude_correction = ApparentAltitudeCorrection(apparant_altitude_correction_string)

    true_altitude = AltitudeTrue(apparant_altitude, apparant_altitude_correction)
    print(f"True Altitude (TA): {true_altitude}")
    
    return true_altitude

def calculate_latitude(true_altitude=None):
    print("Latitude Calculation\n")

    if not true_altitude:
        true_altitude_str = input("Enter True Altitude (in D°M'S\" format): ")
        true_altitude = AltitudeTrue(true_altitude_str)

    declination_str = input("Enter declination (DEC in D°M'S\" format): ")
    declination = Declination(declination_str)
    estimated_latitude_str = input("Enter the estimated latitude (DEC in D°M'S\" format): ")
    estimated_latitude = Latitude(estimated_latitude_str)

    latitude = CalculatedLatitude(true_altitude, declination, estimated_latitude)
    print(f"Zenith Distance (ZD): {latitude.zenith_distance}")
    print(f"Latitude: {latitude}")

def determine_known_values():
    print("Enter the known compass values (leave blank if unknown):")
    values = {
        "true_bearing": input("Enter the True Bearing (in degrees) or press Enter to skip: ").strip(),
        "magnetic_bearing": input("Enter the Magnetic Bearing (in degrees) or press Enter to skip: ").strip(),
        "compass_bearing": input("Enter the Compass Bearing (in degrees) or press Enter to skip: ").strip(),
        "variation": input("Enter the Compass Variation (in degrees) or press Enter to skip: ").strip(),
        "deviation": input("Enter the Compass Deviation (in degrees) or press Enter to skip: ").strip(),
    }

    # Mark known values
    known_values = {key: bool(value) for key, value in values.items()} 
    return known_values, values

def compass_values():
    known_values, values = determine_known_values()
    calculator = CompassCalculator(known_values, values)
    calculator.calculate_all()

def main():
    print("Choose the calculation(s) to perform:")
    options = {
        "1": "Star Sight",
        "2": "Observation Time",
        "3": "Time",
        "4": "Altitude",
        "5": "Latitude",
        "6": "Compass Values"
    }
    
    for key, value in options.items():
        print(f"{key}: {value}")
    
    choices = input("Enter the numbers of the calculations you want to perform, separated by commas (e.g., 1,3): ")
    selected_options = choices.split(",")

    true_altitude = None
    
    for option in selected_options:
        if option == "1":
            calculate_star_sight()
        elif option == "2":
            calculate_observation_time()
        elif option == "3":
            calculate_time()
        elif option == "4":
            true_altitude = calculate_altitude()
        elif option == "5":
            calculate_latitude(true_altitude)
        elif option == "6":
            compass_values()

if __name__ == "__main__":
    main()
