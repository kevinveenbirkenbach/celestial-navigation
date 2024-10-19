import re

def parse_dms(input_str):
    """Parse a string in the format of degrees, minutes, and seconds to decimal degrees."""
    dms_pattern = re.compile(r"(?P<degrees>-?\d+\.?\d*)°(?P<minutes>\d*\.?\d*)'(?P<seconds>\d*\.?\d*)\"?(?P<direction>[EWNS])?")
    match = dms_pattern.match(input_str)
    if not match:
        raise ValueError("Invalid format. Use D°M'S\" format.")
    
    degrees = float(match.group('degrees'))
    minutes = float(match.group('minutes')) if match.group('minutes') else 0
    seconds = float(match.group('seconds')) if match.group('seconds') else 0
    direction = match.group('direction')
    
    decimal_degrees = degrees + minutes / 60 + seconds / 3600
    
    # Adjust for direction
    if direction in ['W', 'S']:
        decimal_degrees = -abs(decimal_degrees)
    
    return decimal_degrees

def get_input(prompt):
    return input(prompt)

def calculate_arc_to_time(longitude):
    """Calculate arc to time from longitude."""
    return longitude * 4  # Longitude in degrees to time in minutes (4 min per degree)

def calculate_total_correction(index_error, monthly_correction):
    """Calculate the total correction (Page 41 refers to standard correction tables)."""
    return index_error + monthly_correction

def calculate_true_altitude(observed_altitude, total_correction):
    """Calculate the true altitude."""
    return observed_altitude + total_correction

def calculate_latitude(declination, true_altitude):
    """Calculate the latitude using declination and true altitude (ZD = 90° - TA)."""
    ZD = 90 - true_altitude
    if declination > true_altitude:
        return ZD + declination
    else:
        return declination - ZD

def main():
    print("Noon Sight Calculation Pro Forma\n")

    # TIME INPUTS
    longitude_str = get_input("Enter estimated longitude (in D°M'S\" format, with direction E/W): ")
    estimated_longitude = parse_dms(longitude_str)
    arc_to_time = calculate_arc_to_time(estimated_longitude)
    print(f"Arc to time: {arc_to_time} minutes")

    transit_greenwich = get_input("Enter GMT transit time at Greenwich (h.m format): ")

    # ALTITUDE INPUTS
    sextant_altitude = get_input("Enter sextant altitude (SA in D°M'S\" format): ")
    sextant_altitude = parse_dms(sextant_altitude)
    
    index_error = float(get_input("Enter index error (IE, positive or negative): "))
    observed_altitude = get_input("Enter observed altitude (OA in D°M'S\" format): ")
    observed_altitude = parse_dms(observed_altitude)
    
    monthly_correction = float(get_input("Enter monthly correction (from table): "))

    # Calculate total correction
    total_correction = calculate_total_correction(index_error, monthly_correction)
    true_altitude = calculate_true_altitude(observed_altitude, total_correction)
    print(f"True Altitude (TA): {true_altitude}")

    # LATITUDE INPUTS
    declination = get_input("Enter declination (DEC in D°M'S\" format): ")
    declination = parse_dms(declination)
    
    latitude = calculate_latitude(declination, true_altitude)
    print(f"Latitude: {latitude}")

    print("Calculation completed.")

if __name__ == "__main__":
    main()
