import requests

def load_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        ip_list = file.read().splitlines()
    return ip_list

file_path = 'ips.txt'
ip_list = load_ip_addresses(file_path)

for i in ip_list:
    ip_address = "129.0.6.{0}".format(i)
    url = "http://{0}:18081/?Action=Restart".format(ip_address)
    try:
        response = requests.get(url)
        print("GET request to {0} returned status code {1}".format(ip_address, response.status_code))
    except requests.exceptions.RequestException as e:
        print("GET request to {0} failed: {1}".format(ip_address, e))
