# pump_controller.py

from pyb import Pin
import time

class PumpController:
    def __init__(self, pump_pins):
        self.pumps = [Pin(pin, Pin.OUT_PP) for pin in pump_pins]

    def run_pump(self, index, duration):
        print(f"Running pump {index} for {duration}s")
        self.pumps[index].high()
        time.sleep(duration)
        self.pumps[index].low()
        print(f"Pump {index} stopped")

    def run_all(self, durations):
        for i, duration in enumerate(durations):
            self.run_pump(i, duration)

