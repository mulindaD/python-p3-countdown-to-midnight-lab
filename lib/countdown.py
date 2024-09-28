# your code goes here!
import time

def countdown(int):
    count = int
    while count >= 1:
        print (f'{count} SECOND(S)!')
        count -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    count = int
    while count >= 1:
        time.sleep(1)
        print (f'{count} SECOND(S)!')
        count -= 1
    print("HAPPY NEW YEAR!")