import requests
from pprint import pprint

# "Tokyp, JP", "New York, US"
cityname = "seoul"
apikey = 'YOUR_OPENWEATHER_API_KEY'

lat = 0
lon = 0
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
response = requests.get(url).json()
pprint(response)