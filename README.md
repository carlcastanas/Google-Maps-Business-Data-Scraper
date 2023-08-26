# Google Maps Business Data Scraper

This Python script allows you to scrape business information from Google Maps using the Google Maps Places API. The script retrieves business names, contact information, and logo URLs within a specified radius of a given location.

## Getting Started

### Prerequisites

- Python 3.x installed
- `requests` library installed (`pip install requests`)

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/google-maps-business-scraper.git
   cd google-maps-business-scraper

1. Replace 'YOUR_API_KEY' in scrap.py with your Google Maps API key.

2. Modify the location and radius variables in scrap.py to define your desired search area.

   ```bash
   python3 scrap.py
This will scrape business data and save it to a CSV file named businesses.csv.

3. Review the output CSV file to find business names, contact information, and logo URLs.