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

# Logic that you write
global lst_1 , index
lst_1 = list(itertools.product(range(2), repeat=3))
index = 0

def my_callback1(channel):
    global index
    index1 = 0
    index =index1 + 1 + index
    if index  ==8:
        index = 0
    GPIO.output([3,5,7], lst_1[index])
    print('This is a edge event callback function one! counting up')
    
    print(lst_1[index])
    
def my_callback2(channel):
    global index
    index1 = 0
    index =index1 + index-1
    if index < 0:
        index = 7
    GPIO.output([3,5,7], lst_1[index])
    
    print('This is a edge event callback function two counting down!')
    print(lst_1[index])


def main():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)
    output_pins = [3,5,7]
    input_pins = [13,15]
    
    GPIO.setup(output_pins, GPIO.OUT)
    GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.setup(iput_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    #if GPIO.input(3):
   #     print('Input was HIGH')
    #else:
      #  print('Input was LOW')
        
    #GPIO.add_event_detect(13, GPIO.RISING)
    #GPIO.add_event_detect(15, GPIO.FALLING, bouncetime=300)
    
    
    #for j in lst_1:
     #   GPIO.output(output_pins, j)
      #  time.sleep(0.5)
       # GPIO.output(output_pins, j)
        #time.sleep(0.5)

    print("write your logic here")
    #p_array = [j]
    #print(p_array)
    
   # for j in range(4):
    #    GPIO.output(output_pins, 1)
     #   time.sleep(2)
      #  GPIO.output(output_pins, 0)
       # time.sleep(2)
    
  #  print("write your logic here")


# Only run the functions if 
if __name__ == "__main__":
    
    # Make sure the GPIO is stopped correctly
    GPIO.setmode(GPIO.BOARD)
    input_pins = [13,15]
    GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(13, GPIO.RISING,callback=my_callback1)
    GPIO.add_event_detect(15, GPIO.FALLING,callback=my_callback2,bouncetime=300)
    try:
        main()
        time.sleep(2000)
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
