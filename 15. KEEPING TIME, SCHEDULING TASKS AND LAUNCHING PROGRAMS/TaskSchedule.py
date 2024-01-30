import schedule
import time

def my_task():
    print("Task is running...")

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(my_task)

# You can also use other schedule options like minutes, hours, etc.
# For example, to run the task every 2 hours:
# schedule.every(2).hours.do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)
