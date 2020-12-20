# from datetime import datetime
import time

# st = datetime.now()
st = time.time()
i = 0
while i < 10000000:
    i += 1
print(f'time to run = {(time.time() - st)} seconds')
