import requests

# NumVerify API endpoint
api_url = "http://apilayer.net/api/validate"

# NumVerify API access key
access_key = "4ieOVfhiq6Hw9FcqbRnXPdqdKcwCHBhn"

# Phone number to lookup
phone_number = input('Enter phone number:')

# Make a request to the NumVerify API
try:
    response = requests.get(api_url, params={"access_key": access_key, "number": phone_number})
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    sys.exit(1)
except Exception as err:
    print(f"Other error occurred: {err}")
    sys.exit(1)

# Parse the response JSON
response_json = response.json()

# Get the country name and location details from the response
country_name = response_json.get("country_name")
location = response_json.get("location")

# Construct the location details string
location_str = f"Country: {country_name}\nLocation: {location}"

# Print the location details
print(location_str)
