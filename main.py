import random
from datetime import datetime
import pandas
import requests

n = random.randint(0,100)

outstr = f"{datetime.now()}__random:{n}"

with open("log.txt", 'a') as f:
    f.write(outstr+"\n")
    
print(outstr)