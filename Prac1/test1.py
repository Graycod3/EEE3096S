#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Blessing Ngorima>
Student Number: <NGRBLE001>
Prac: <Prac One>
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    output_pins = [3,5,7]
    input_pins = [13,15]
    GPIO.setup(output_pins, GPIO.OUT)
    GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   
def my_callback1(pin):
    GPIO.output([3,5,7],[1,0,1])
    time.sleep(1)
    GPIO.output([3,5,7],[0,0,0])
    time.sleep(1)
# Only run the functions if 
if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    output_pins = [3,5,7]
    input_pins = [13,15]
    
    # Make sure the GPIO is stopped correctly
    GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(13, GPIO.RISING,callback=my_callback1)
    #GPIO.add_event_detect(15, GPIO.FALLING,callback=my_callback2,bouncetime=300)
    try:
        main()
        time.sleep(1000)
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
