# import leds

import motephat as mote

NUM_CHANNELS = 2
NUM_PIXELS = 16

# Initialise library if on Pi
def init():
  for c in range(NUM_CHANNELS):
    mote.configure_channel(c + 1, NUM_PIXELS, True)

# Clear all pixels
def clear():
  mote.set_all(0, 0, 0)

# Set a pixel color
def set_pixel(i, color):
  for c in range(NUM_CHANNELS):
    mote.set_pixel(c + 1, i, color[0], color[1], color[2])

# Set all pixels to a color
def set_all(color):
  mote.set_all(r, g, b)

# Show pixel changes
def update():
  mote.show()
