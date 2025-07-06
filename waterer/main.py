# main.py

import config
from pump_controller import PumpController
from scheduler import should_run_now
from pyb import delay

def main():
    controller = PumpController(config.PUMP_PINS)
    last_run_date = None

    while True:
        run_now, today = should_run_now(config.RUN_HOUR, config.RUN_MINUTE, last_run_date)
        if run_now:
            controller.run_all(config.PUMP_DURATIONS)
            last_run_date = today
        delay(60000)  # check every 60 seconds

main()

