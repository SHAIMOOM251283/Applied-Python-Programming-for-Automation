import time
import pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1
lap_records = []

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        # Prettify the output using rjust() and ljust()
        output_str = 'Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime)
        output_str = output_str.replace('#', '# ').ljust(30)

        print(output_str, end='')

        # Copy the lap output to the clipboard
        pyperclip.copy(output_str)

        lap_records.append(output_str)  # Store lap output for later

        lapNum += 1
        lastTime = time.time()  # reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')

    # Concatenate all lap records into a single string
    full_output = '\n'.join(lap_records)

    # Copy the entire output to the clipboard
    pyperclip.copy(full_output)
      