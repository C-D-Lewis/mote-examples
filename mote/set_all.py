# python3 set_all.py <r> <g> <b>

import sys
import leds

r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

# The main function
def main():
  leds.init(stay_on = True)

  leds.set_all([r, g, b])
  leds.update()

if '__main__' in __name__:
  main()
