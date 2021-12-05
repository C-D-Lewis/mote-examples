# Helper file to make mote animation scripts easier - just 'import leds'

import motephat as mote

# Number of mote sticks connected
NUM_CHANNELS = 2
# Number of LEDs per stick
NUM_PIXELS = 16
# Fade interval
INTERVAL = 0.01
# Fade step size
STEP = 5

state = []
for i in range(0, NUM_PIXELS):
  state.append([0, 0, 0])

# Reset the internal pixel state
#
# value - Optional new color to use for all pixels in the state
def reset_state(value = [0, 0, 0]):
  for i in range(0, NUM_PIXELS):
    state[i] = [0, 0, 0]

# Initialise library if on Pi
#
# stay_on - True if LEDs should stay on after program exits, False otherwise
def init(stay_on = False):
  mote.set_clear_on_exit(not stay_on)
  reset_state()

  for c in range(NUM_CHANNELS):
    mote.configure_channel(c + 1, NUM_PIXELS, True)

# Clear all pixels
def clear():
  reset_state()
  mote.set_all(0, 0, 0)

# Set a pixel color
#
# i     - Pixel index from the cable end
# color - Array of r, g, b values
def set_pixel(i, color):
  state[i] = color
  for c in range(NUM_CHANNELS):
    mote.set_pixel(c + 1, i, color[0], color[1], color[2])

# Set all pixels to a color
#
# color - Array of r, g, b values
def set_all(color):
  reset_state(value = color)
  mote.set_all(color[0], color[1], color[2])

# Show pixel changes
def update():
  mote.show()

# Slowly fade to a given color
#
# target - Array of r, g, b values to fade to
def fade_to(target):
  # Assume all colors are the same
  current = state.copy()[0]

  while current != target:
    set_all(current)
    update()

    diff = abs(current[0] - target[0])
    current[0] += (STEP if diff > STEP else diff) * (-1 if current[0] > target[0] else 1)
    diff = abs(current[1] - target[1])
    current[1] += (STEP if diff > STEP else diff) * (-1 if current[1] > target[1] else 1)
    diff = abs(current[2] - target[2])
    current[2] += (STEP if diff > STEP else diff) * (-1 if current[2] > target[2] else 1)
    time.sleep(INTERVAL)
