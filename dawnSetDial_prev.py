import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://gml.noaa.gov/grad/solcalc/table.php?lat=38.88&lon=-77.03&year=2024'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element containing sunrise data (you may need to inspect the webpage's HTML structure)
    sunrise = soup.find('div', class_='pull-right', style='margin-top: 10px')

    # Extract the text or attributes you need
    table_element = sunrise.find(class_='table, table-bordered')
    
    # Check if the table is found
    if table_element:
        # Process the table data as needed
        # For example, you can iterate through rows and cells:
        for row in table_element.find_all('tr'):
                for cell in row.find_all('td'):
                    print(cell.text.strip())  # Print or process cell dat
    
    # Print or use the extracted data as needed
    print(f'Sunrise time: {sunrise_time}')
else:
    print('Failed to retrieve data. Status code:', response.status_code)
