# scheduler.py

from pyb import RTC
import time

def should_run_now(run_hour, run_minute, last_run_date):
    now = RTC().datetime()
    year, month, day, _, hour, minute, *_ = now

    if (hour, minute) >= (run_hour, run_minute):
        today = (year, month, day)
        return last_run_date != today, today
    return False, last_run_date

