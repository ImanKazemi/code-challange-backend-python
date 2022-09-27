import geopy.distance


class DistanceUtils:

    """ Distance calculation methods """

    @staticmethod
    def calc_distance_geo(origin_latitude, origin_longitude, distination_latitude, distination_longitude):
        """Calculate distance between geo location in KM"""

        origin = (origin_latitude, origin_longitude)
        distination = (distination_latitude, distination_longitude)

        return geopy.distance(origin, distination).km

    @staticmethod
    def calc_distance_to_origin(distination_latitude, distination_longitude):
        """Calculate distance between customer's geo location and office in Dublin in KM"""

        origin = (53.339428, -6.257664)
        distination = (distination_latitude, distination_longitude)

        distance = geopy.distance.geodesic(origin, distination).km
        return distance
