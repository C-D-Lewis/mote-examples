# Helper file to make mote animation scripts easier - just 'import leds'

import motephat as mote

# Number of mote sticks connected
NUM_CHANNELS = 2
# Number of LEDs per stick
NUM_PIXELS = 16

# Initialise library if on Pi
#
# stay_on - True if LEDs should stay on after program exits, False otherwise
def init(stay_on = False):
  mote.set_clear_on_exit(not stay_on)

  for c in range(NUM_CHANNELS):
    mote.configure_channel(c + 1, NUM_PIXELS, True)

# Clear all pixels
def clear():
  mote.set_all(0, 0, 0)

# Set a pixel color
#
# i     - Pixel index from the cable end
# color - Array of r, g, b values
def set_pixel(i, color):
  for c in range(NUM_CHANNELS):
    mote.set_pixel(c + 1, i, color[0], color[1], color[2])

# Set all pixels to a color
#
# color - Array of r, g, b values
def set_all(color):
  mote.set_all(color[0], color[1], color[3])

# Show pixel changes
def update():
  mote.show()
