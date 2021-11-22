from credentials import username, password
from gervasio import Gervasio
import sys
import time

minutes_of_sleep = int(sys.argv[-1])
seconds_of_sleep = 60 * minutes_of_sleep

print(f"Sleeping for {minutes_of_sleep} minutes before launch...")
time.sleep(seconds_of_sleep)

Gervasio(username, password)
