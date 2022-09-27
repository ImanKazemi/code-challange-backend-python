from domain.Customer import Customer
import json
import sys
from utils.FileUtils import FileUtils


def main(customer_file_path):
    """main method to read customer text file and return customers with distance less than 100 KM"""

    customers_raw_data = FileUtils.load_txt_file_from_path(customer_file_path)

    customers = Customer.parse_customer_list(customers_raw_data)

    
    nearby_customers = [{"user_id": customer.user_id, "name": customer.name}
                        for customer in customers if customer.distance < 100]
    nearby_customers.sort(key=lambda x: x["user_id"])

    output = json.dumps(nearby_customers)

    return output


if __name__ == '__main__':
    customer_file_path = './Data/customers.txt'#sys.argv[0]
    response = main(customer_file_path)
    print(response)
