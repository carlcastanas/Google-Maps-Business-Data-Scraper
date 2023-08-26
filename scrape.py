import requests
import csv

API_KEY = 'YOUR_API_KEY'
location = 'YOUR_LOCATION_COORDINATES'  # Location coordinates
radius = 1000  # Define the search radius in meters

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&key={API_KEY}'

response = requests.get(url)
data = response.json()

businesses = []

for place in data.get('results', []):
    place_id = place['place_id']
    details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_phone_number,website&key={API_KEY}'
    details_response = requests.get(details_url)
    details_data = details_response.json()
    
    business_name = details_data.get('result', {}).get('name', 'N/A')
    contact_info = details_data.get('result', {}).get('formatted_phone_number', 'N/A')
    email = details_data.get('result', {}).get('website', 'N/A')
    
    businesses.append({'Business Name': business_name, 'Contact Info': contact_info, 'Email': email})

# Save data to CSV file
csv_filename = 'businesses.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Business Name', 'Contact Info', 'Email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for business in businesses:
        writer.writerow(business)

print(f'Data saved to {csv_filename}')