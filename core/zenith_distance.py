from .degree import Degree
from .altitude import AltitudeTrue

class ZenithDistance(Degree):
    """
    The Zenith Distance (ZD) represents the angular distance between the observer's zenith (the point directly overhead)
    and the celestial body being observed. In other words, it is the complement of the observed altitude. 

    Formula:
    ZD = 90° - True Altitude (TA)

    - If the altitude of a celestial object is measured as 90°, the object is directly overhead (Zenith), and the zenith distance is 0°.
    - If the altitude is lower than 90°, the zenith distance increases accordingly.
    - The zenith distance is used in the calculation of latitude and other positional elements in celestial navigation.
    """

    def __init__(self, altitude_true: AltitudeTrue):
        # Calculate the zenith distance by subtracting the true altitude from 90°.
        # The altitude_true.decimal gives the altitude in decimal degrees.
        zenith_distance = 90 - altitude_true.decimal
        
        # Pass the calculated zenith distance to the parent class (Degree) constructor.
        super().__init__(zenith_distance)
