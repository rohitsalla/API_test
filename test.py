import requests

geoapify_api_key = "your_geoapify_api_key"
geoapify_base_url = "https://api.geoapify.com/v2/place-details"

def get_location_details(lat, lon):
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "apiKey": geoapify_api_key,
        }
        response = requests.get(geoapify_base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location details: {e}")
        return None

def display_merchant_details(location_data):
    if location_data:
        for feature in location_data.get("features", []):
            properties = feature.get("properties", {})
            name = properties.get("name", "N/A")
            category = properties.get("categories", ["N/A"])
            address = properties.get("address_line1", "N/A")
            print(f"Name: {name}")
            print(f"Category: {', '.join(category)}")
            print(f"Address: {address}")
            print("-" * 40)
    else:
        print("No data available.")

if __name__ == "__main__":
    latitude = 23.56260165936459
    longitude = 120.47521510189569

    location_data = get_location_details(latitude, longitude)
    if location_data:
        print("Location and Merchant Details:")
        display_merchant_details(location_data)
    else:
        print("Failed to fetch location details.")
