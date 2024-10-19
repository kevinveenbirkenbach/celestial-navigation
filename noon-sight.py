from core.transit_time import TransitTimeCalculator
from core.celestial import CelestialNavigation
from core.helper import Helper

def main():
    print("Noon Sight Calculation Pro Forma\n")

    # TIME INPUTS
    longitude_str = Helper.get_input("Enter estimated longitude (in D°M'S\" format, with direction E/W): ")
    transit_greenwich_str = Helper.get_input("Enter GMT transit time at Greenwich (hh:mm format): ")

    # Calculate transit time at EP
    transit_calculator = TransitTimeCalculator(longitude_str, transit_greenwich_str)
    transit_ep_time = transit_calculator.calculate_transit_time_at_ep()
    print(f"Transit Time at EP: {transit_ep_time}")

    # ALTITUDE INPUTS
    sextant_altitude_str = Helper.get_input("Enter sextant altitude (SA in D°M'S\" format): ")
    index_error = float(Helper.get_input("Enter index error (IE, positive or negative): "))
    monthly_correction = float(Helper.get_input("Enter monthly correction (from table): "))

    # LATITUDE INPUTS
    declination_str = Helper.get_input("Enter declination (DEC in D°M'S\" format): ")

    # Celestial Navigation Calculations
    celestial_navigation = CelestialNavigation(sextant_altitude_str, index_error, monthly_correction, declination_str)
    true_altitude = celestial_navigation.calculate_true_altitude()
    latitude = celestial_navigation.calculate_latitude()

    print(f"True Altitude (TA): {true_altitude}")
    print(f"Latitude: {latitude}")

if __name__ == "__main__":
    main()
