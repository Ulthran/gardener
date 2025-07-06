# Waterer Hardware Setup

This module runs on a PyBoard controlling a handful of small DC pumps. Below is a minimal wiring guide:

1. Use a MOSFET or driver board for each pump and connect its gate to the pins
   defined in `config.py`.
2. Wire the pumps' positive terminals to the driver outputs and tie all grounds
   together with the PyBoard ground.
3. Provide an appropriate power supply for the pumps (often 5V) separate from
   the PyBoard's USB power.
4. Copy the files in this directory onto the PyBoard and run `main.py` to start
   the daily watering schedule.
