from dataclasses import dataclass
from utils.DistanceUtils import DistanceUtils
import json

@dataclass
class Customer:
    """ data class for customer data"""

    user_id: int
    name: str
    longitude: str
    latitude: str
    distance: int

    @classmethod
    def parse_customer(cls, data: dict) -> "Customer":
        """ Convert customer dictionary to customer data class"""

        return cls(
            user_id = int(data["user_id"]),
            name=data["name"],
            latitude = data["latitude"],
            longitude = data["longitude"],
            distance = DistanceUtils.calc_distance_to_origin(data["latitude"],data["longitude"])
        )

    @classmethod
    def parse_customer_list(cls, customer_data: dict) -> "Customer":
        """ Convert cutsomer json data to customer list """

        customer_list = []

        for customer_dict in customer_data:
            customer_list.append(cls.parse_customer(json.loads(customer_dict)))

        return customer_list
