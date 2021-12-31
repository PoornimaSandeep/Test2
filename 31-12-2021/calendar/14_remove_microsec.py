print("Write a Python program to drop microseconds from datetime.")
from datetime import datetime, time
dt=datetime.today().replace(microsecond=0)
print(dt)
