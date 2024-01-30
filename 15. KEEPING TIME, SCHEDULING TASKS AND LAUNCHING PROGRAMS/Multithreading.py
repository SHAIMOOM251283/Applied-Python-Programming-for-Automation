import time, datetime

startTime = datetime.datetime(2024, 1, 11, 0, 32, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Event 2024')