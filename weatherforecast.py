import requests

# Asks for city 
try:
    city = input('Where in the world are you? ')

    c = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')

except requests.exceptions.ConnectionError:
    print('Yaikes! Couldn\'t connect to server. Please see if the network is up.')


f = c.json()

woeid = (f[0]['woeid'])

r = requests.get(f'https://www.metaweather.com/api/location/{woeid}/')

d = r.json()

print(f'Weather for {city}:')
for i in d['consolidated_weather']:
    date = i['applicable_date']
    weather_state = i['weather_state_name']
    low = i['min_temp']
    high = i['max_temp']
    print(f'{date}  {weather_state}  {low:.1f}  {high:.1f}')


