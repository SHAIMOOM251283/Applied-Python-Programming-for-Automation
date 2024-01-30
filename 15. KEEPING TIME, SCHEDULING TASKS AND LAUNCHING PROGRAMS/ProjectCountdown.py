#! python3
# countdown.py - A simple countdown script.
#import time, subprocess
#timeLeft = 10
#while timeLeft > 0:
#    print(timeLeft, end='')
#    time.sleep(1)
#    timeLeft = timeLeft - 1
# At the end of the countdown, play a sound file.
#subprocess.Popen(['start', 'alarm.wav'], shell=True)

#! python3
# countdown.py - A simple countdown script.

import time
import pygame

def play_sound(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
play_sound('alarm.wav')
