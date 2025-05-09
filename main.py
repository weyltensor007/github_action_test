import random
from datetime import datetime
import pandas
import requests
import pytz

tz_taiwan = pytz.timezone('Asia/Taipei')

n = random.randint(0,100)

outstr = f"{datetime.now(tz_taiwan)}__random:{n}"

with open("log.txt", 'a') as f:
    f.write(outstr+"\n")
    
print(outstr)