from machine import Pin
import time

# define LED color constants
LED_RED = 1
LED_GREEN = 2
LED_BLUE = 3


def task1():
    Pin(LED_BLUE, Pin.OUT).toggle()
    time.sleep(1)
    print(LED_BLUE)

def task2():
    Pin(LED_GREEN, Pin.OUT).toggle()
    time.sleep(1)
    print(LED_GREEN)

def task3():
    Pin(LED_RED, Pin.OUT).toggle()
    time.sleep(1)
    print(LED_RED)


############################################################
#
# Start script execution ...
#
############################################################
# Setup the MCU and application code to starting conditions
# All LED's off from beginning
Pin(LED_BLUE).off()
Pin(LED_GREEN).off()
Pin(LED_RED).off()

# Main application loop
while True:
    # Run the first task
    task1()

    # Run the second task
    task2()

    # Run the thirt task
    task3()
    