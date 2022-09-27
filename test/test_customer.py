import unittest
from domain.Customer import Customer


class test_file_utils(unittest.TestCase):
    """test cases for test customer data"""

    def test_customer_parser(self):

        first_customer = Customer.parse_customer(
            {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"})
        second_customer = Customer(
            12, "Christina McArdle", "-6.043701", "52.986375", 41.81601095296908)

        self.assertEqual(first_customer, second_customer)

    def test_customer_list_parser(self):
        first_customer_list = Customer.parse_customer_list(['{"latitude": "54.080556", "user_id": 23, "name": "Eoin Gallagher", "longitude": "-6.361944"}\n', '{"latitude": "52.833502", "user_id": 25, "name": "David Behan", "longitude": "-8.522366"}'])

        alpha_customer = Customer(
            23, "Eoin Gallagher", "-6.361944", "54.080556", 82.77410789481068)
        beta_customer = Customer(
            25, "David Behan", "-8.522366", "52.833502", 161.8419409412132)

        second_customer_list = [alpha_customer, beta_customer]

        self.assertEqual(first_customer_list, second_customer_list)
