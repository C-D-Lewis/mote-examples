# python3 weather_mood.py

import leds
import requests
import time

# OpenWeatherMap API key
API_KEY = '6fdf8b1f9b3c4b3916e57166631c363d'
# Current latitude
LATITUDE = 51.577392
# Current longitude
LONGITUDE = 0.179766
# Update interval
INTERVAL = 1000 * 60 * 15

# Get a color suited to the current conditions string
#
# conditions - Weather conditions string from the API
def get_weather_color(conditions):
  text = conditions.lower()
  print('conditions: {}'.format(text))

  if 'sun' in text or 'clear' in text:
    return [255, 184, 10]
  if 'rain' in text or 'shower' in text or 'drizzle' in text:
    return [100, 149, 237]
  if 'ice' in text or 'frost' in text or 'snow' in text:
    return [255, 255, 255]
  if 'cloud' in text or 'overcast' in text:
    return [128, 128, 128]

  print('Unknown conditions case')
  return [64, 64, 64]

# Fetch current weather conditions
def fetch_weather_conditions():
  url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(LATITUDE, LONGITUDE, API_KEY)
  json = requests.get(url).json()

  # Use main weather description as conditions
  conditions = json['weather'][0]['description']
  return conditions

# The main function
def main():
  leds.init()

  leds.set_all([0, 0, 0])
  leds.update()

  while True:
    # Fetch conditions
    conditions = fetch_weather_conditions()

    # Update LEDs
    new_color = get_weather_color(conditions)
    leds.fade_to(new_color)

    # Wait for next check
    time.sleep(INTERVAL)

if '__main__' in __name__:
  main()
