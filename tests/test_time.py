import unittest
from datetime import datetime, timezone, timedelta
from core.time import UTCDatetime, ArcToTime, TransitTime, ObservationTime
from core.longitude import Longitude


class TestUTCDatetime(unittest.TestCase):

    def test_utc_datetime_from_string(self):
        # Test parsing of valid datetime string
        utc_dt = UTCDatetime("2024-06-21T12:00:00")
        expected = datetime(2024, 6, 21, 12, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(utc_dt, expected)
        self.assertEqual(str(utc_dt), "2024-06-21 12:00:00+00:00")

    def test_utc_datetime_from_naive_datetime(self):
        # Test conversion of naive datetime to UTC
        naive_dt = datetime(2024, 6, 21, 12, 0, 0)
        utc_dt = UTCDatetime(naive_dt)
        expected = naive_dt.replace(tzinfo=timezone.utc)
        self.assertEqual(utc_dt, expected)

    def test_utc_datetime_from_aware_datetime(self):
        # Test conversion of aware datetime (with timezone info) to UTC
        aware_dt = datetime(2024, 6, 21, 12, 0, 0, tzinfo=timezone(timedelta(hours=2)))
        utc_dt = UTCDatetime(aware_dt)
        expected = datetime(2024, 6, 21, 10, 0, 0, tzinfo=timezone.utc)  # Adjusted to UTC
        self.assertEqual(utc_dt, expected)

    def test_invalid_datetime_format(self):
        # Test parsing of an invalid datetime string
        with self.assertRaises(ValueError):
            UTCDatetime("invalid-date")


class TestArcToTime(unittest.TestCase):

    def test_arc_to_time_conversion(self):
        # Test ArcToTime conversion from longitude
        longitude = Longitude("90°00'00\"E")  # 90 degrees
        arc_to_time = ArcToTime(longitude)
        expected = timedelta(minutes=360)  # 90 * 4 = 360 minutes
        self.assertEqual(arc_to_time, expected)
        self.assertEqual(str(arc_to_time), "06:00:00")

    def test_arc_to_time_east(self):
        # Test ArcToTime conversion for negative longitude (West)
        longitude = Longitude("45°00'00\"W")  # -45 degrees
        arc_to_time = ArcToTime(longitude)
        expected = timedelta(minutes=-180).total_seconds()  # -45 * 4 = -180 minutes
        self.assertEqual(arc_to_time.total_seconds(), expected)
        self.assertEqual(str(arc_to_time), "-03:00:00")

    def test_arc_to_time_west(self):
        # Test ArcToTime conversion for negative longitude (West)
        longitude = Longitude("45°00'00\"E")  # -45 degrees
        arc_to_time = ArcToTime(longitude)
        expected = timedelta(minutes=180).total_seconds()  # 45 * 4 = 180 minutes
        self.assertEqual(arc_to_time.total_seconds(), expected)
        self.assertEqual(str(arc_to_time), "03:00:00")


class TestTransitTime(unittest.TestCase):

    def test_transit_time_east_longitude(self):
        # Test transit time calculation at longitude
        longitude = Longitude("30°00'00\"E")
        arc_to_time = ArcToTime(longitude)
        transit_time_greenwich = UTCDatetime("2024-06-21T12:00:00")
        
        # Calculate expected transit time at longitude
        expected_transit_time = transit_time_greenwich - timedelta(minutes=120)  # 30 * 4 = 120 minutes
        transit_time_at_longitude = TransitTime(arc_to_time, transit_time_greenwich)
        
        self.assertEqual(transit_time_at_longitude, expected_transit_time)
        self.assertEqual(str(transit_time_at_longitude), "2024-06-21 10:00:00+00:00")

    def test_transit_time_west_longitude(self):
        # Test transit time for negative longitude (West)
        longitude = Longitude("15°00'00\"W")
        arc_to_time = ArcToTime(longitude)
        transit_time_greenwich = UTCDatetime("2024-06-21T12:00:00")
        
        # Calculate expected transit time at longitude
        expected_transit_time = transit_time_greenwich + timedelta(minutes=60)  # -15 * 4 = +60 minutes
        transit_time_at_longitude = TransitTime(arc_to_time, transit_time_greenwich)
        
        self.assertEqual(transit_time_at_longitude, expected_transit_time)
        self.assertEqual(str(transit_time_at_longitude), "2024-06-21 13:00:00+00:00")
class TestObservationTime(unittest.TestCase):

    def setUp(self):
        # Set example times for the test
        self.nautical_twilight = TransitTime(
            arc_to_time=timedelta(hours=-2, minutes=-51), 
            transit_time_greenwich=datetime(2024, 6, 21, 2, 0, 0, tzinfo=timezone.utc)
        )
        self.civil_twilight = TransitTime(
            arc_to_time=timedelta(hours=-2, minutes=-51), 
            transit_time_greenwich=datetime(2024, 6, 21, 3, 6, 0, tzinfo=timezone.utc)
        )
        self.sunrise = TransitTime(
            arc_to_time=timedelta(hours=-2, minutes=-51), 
            transit_time_greenwich=datetime(2024, 6, 21, 3, 51, 0, tzinfo=timezone.utc)
        )

        # Example instance of ObservationTime
        self.observation_time = ObservationTime(
            nautical_twilight=self.nautical_twilight, 
            civil_twilight=self.civil_twilight, 
            sunrise=self.sunrise
        )

    def test_observation_start_and_end(self):
        # Expected times for observation start and end
        expected_observation_start = datetime(2024, 6, 21, 5, 24, 0, tzinfo=timezone.utc)
        expected_observation_end = datetime(2024, 6, 21, 6, 19, 30, tzinfo=timezone.utc)

        # Check if the calculated times are correct
        self.assertEqual(self.observation_time.observation_start, expected_observation_start)
        self.assertEqual(self.observation_time.observation_end, expected_observation_end)

    def test_observation_time_str(self):
        # Test the __str__ method for correct output
        expected_output = """
Observation Start: 2024-06-21 05:24:00+00:00
Observation End: 2024-06-21 06:19:30+00:00
        """
        self.assertEqual(str(self.observation_time).strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main()
