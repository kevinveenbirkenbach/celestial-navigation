def get_input(prompt):
    return float(input(prompt))

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
    estimated_longitude = get_input("Enter estimated longitude (in degrees, E/W): ")
    arc_to_time = calculate_arc_to_time(estimated_longitude)
    print(f"Arc to time: {arc_to_time} minutes")

    transit_greenwich = get_input("Enter GMT transit time at Greenwich (h.m format): ")

    # ALTITUDE INPUTS
    sextant_altitude = get_input("Enter sextant altitude (SA): ")
    index_error = get_input("Enter index error (IE, positive or negative): ")
    observed_altitude = get_input("Enter observed altitude (OA): ")
    monthly_correction = get_input("Enter monthly correction (from table): ")

    # Calculate total correction
    total_correction = calculate_total_correction(index_error, monthly_correction)
    true_altitude = calculate_true_altitude(observed_altitude, total_correction)
    print(f"True Altitude (TA): {true_altitude}")

    # LATITUDE INPUTS
    declination = get_input("Enter declination (DEC): ")
    latitude = calculate_latitude(declination, true_altitude)
    print(f"Latitude: {latitude}")

    print("Calculation completed.")

if __name__ == "__main__":
    main()
