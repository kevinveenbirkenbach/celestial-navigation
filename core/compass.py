from .degree import Degree
from .coordinates_geographic import Longitude
from .helper import Helper

# Created with the help of CHAT GPT @see https://chatgpt.com/share/6717189c-905c-800f-8146-1a25ea76428c
class Compass(Degree):
    def __init__(self, opperant_one_instance: str, opperant_two_instance: str, addition:bool, *args):
        super().__init__(Helper.delta(opperant_one_instance, opperant_two_instance, addition, *args))
class CompassVariation(Compass,Longitude):
    """DE: Missweisung
    Formula: 
    True Bearing - Magnetic Bearing = Compass Variation
    The compass variation is the angular difference between true north (geographic north) and magnetic north.
    In this case, variation is subtracted from the true bearing to get the magnetic bearing. 
    """
    def __init__(self, *args):
        super().__init__(CompassTrueBearing,CompassMagneticBearing,False, *args)

class CompassDeviation(Compass,Longitude):
    """DE: Ablenkung
    Formula:
    Magnetic Bearing - Compass Bearing = Compass Deviation
    Deviation is the error introduced by magnetic influences on the vessel. It is subtracted from the magnetic bearing to get the compass bearing.
    """
    def __init__(self, *args):
        super().__init__(CompassBearing, CompassMagneticBearing, False, *args)

class CompassMagneticBearing(Compass):
    """DE: Missweisende Peilung
    Formula:
    True Bearing - Compass Variation = Magnetic Bearing
    The magnetic bearing is the bearing relative to magnetic north, calculated by subtracting the compass variation from the true bearing.
    """
    def __init__(self, *args):
        super().__init__(CompassTrueBearing,CompassVariation, False, *args)

class CompassBearing(Compass):
    """DE: Magnetkompasspeilung
    Formula:
    Magnetic Bearing - Compass Deviation = Compass Bearing
    The compass bearing is the direction read directly from the magnetic compass, calculated by subtracting deviation from the magnetic bearing.
    """
    def __init__(self, *args):
        super().__init__(CompassMagneticBearing,CompassDeviation,False, *args)
class CompassTrueBearing(Compass):
    """DE: Rechtweisende Peilung
    Formula:
    Magnetic Bearing + Compass Variation = True Bearing
    The true bearing is the direction relative to true north, calculated by adding the compass variation to the magnetic bearing.
    """
    def __init__(self, *args):
        super().__init__(CompassMagneticBearing,CompassVariation,False,*args)