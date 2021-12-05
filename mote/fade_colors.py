# python3 fade_colors.py

import time
import leds
import random

# Time between color changes
INTERVAL = 10
# Available colors
COLORS = [
  [255, 0, 0],    # Red
  [255, 127, 0],  # Orange
  [255, 255, 0],  # Yellow
  [127, 255, 0],  # Lime green
  [0, 255, 0],    # Green
  [0, 255, 127],  # Pastel green
  [0, 255, 255],  # Cyan
  [0, 127, 255],  # Sky blue
  [0, 0, 255],    # Blue
  [127, 0, 255],  # Purple
  [255, 0, 255],  # Pink
  [255, 0, 127]   # Hot pink
]

# Do the animation
def animate():
  index = 0
  last_index = 0

  while True:
    # Pick a random next color, not the same as the last
    index = random.randint(0, len(COLORS)) 
    while index is last_index:
      index = random.randint(0, len(COLORS)) 

    # Fade to that new color
    leds.fade_to(COLORS[index])

    # Wait a while
    time.sleep(INTERVAL)

# The main function
def main():
  leds.init()
  animate()

if '__main__' in __name__:
  main()
