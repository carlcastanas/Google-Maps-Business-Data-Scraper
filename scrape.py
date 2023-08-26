import requests
import csv

API_KEY = 'YOUR_API_KEY'
location = 'LOCATION_RADIUS'  # Location coordinates
radius = 1000  # Define the search radius in meters

url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&key={API_KEY}'

response = requests.get(url)
data = response.json()

businesses = []

for place in data.get('results', []):
    business_name = place.get('name', 'N/A')
    contact_info = place.get('formatted_phone_number', 'N/A')
    logo_url = place.get('icon', 'N/A')  # Assuming the 'icon' field contains the logo URL
    businesses.append({'Business Name': business_name, 'Contact Info': contact_info, 'Logo URL': logo_url})

# Save data to CSV file
csv_filename = 'businesses.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Business Name', 'Contact Info', 'Logo URL']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for business in businesses:
        writer.writerow(business)

print(f'Data saved to {csv_filename}')
