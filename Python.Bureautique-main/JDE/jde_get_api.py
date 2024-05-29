import requests

# Extraction des données de l'api : https://datausa.io/api/data?drilldowns=Nation&measures=Population
url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the data as needed
else:
    print("Failed to retrieve data from the API")