import unittest
from utils.DistanceUtils import DistanceUtils


class test_distance_utils(unittest.TestCase):
    """test cases for test distance utils"""

    def test_geo_distance(self):
        origin_latitude = "53.339428"
        origin_longitude = "-6.257664"
        distination_latitude="52.986375"
        distination_longitude="-6.043701"
        distance = DistanceUtils.calc_distance_geo(origin_latitude, origin_longitude, distination_latitude, distination_longitude)
        self.assertEqual(distance,41.81601095296908)