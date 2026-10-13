import requests
from pprint import pprint

# 서울 위경도
lat = 37.56
lon = 126.97
apikey = 'YOUR_OPENWEATHER_API_KEY'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}'
response = requests.get(url).json()
pprint(response)