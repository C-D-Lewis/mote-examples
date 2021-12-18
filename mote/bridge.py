# python3 bridge.py

import time
import leds

ON = [0, 64, 128]
OFF = [0, 0, 0]

# Do the animation
def animate():
  index = 0

  while True:
    leds.set_pixel(index, OFF)
    leds.set_pixel(index + 1, ON)
    leds.update()

    time.sleep(0.1)
    index = (index + 1) % leds.NUM_PIXELS

# The main function
def main():
  leds.init()
  animate()

if '__main__' in __name__:
  main()
