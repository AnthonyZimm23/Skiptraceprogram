import requests
import json

def skip_trace(api_key, name, address=None, phone=None):
    """
    Function to perform a skip trace lookup using an API.
    :param api_key: Your API key for the skip trace service
    :param name: The name of the person you are trying to trace
    :param address: (Optional) The address of the person
    :param phone: (Optional) The phone number of the person
    :return: Parsed JSON data containing trace results
    """
    url = "https://api.skiptraceexample.com/trace"  # Replace with your actual skip trace API URL
    headers = {
        'Authorization': f'Bearer {api_key}',  # Assuming API uses Bearer authentication
        'Content-Type': 'application/json'
    }

    # Prepare the data payload
    data = {
        "name": name,
        "address": address,
        "phone": phone
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Skip trace results for {name}:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        print(f"Response: {response.text}")

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your real API key
    name = "John Doe"
    address = "123 Main St, Springfield, IL"
    phone = "555-555-5555"
    skip_trace(api_key, name, address, phone)
