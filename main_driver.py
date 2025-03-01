'''
This file allows the driver to use both joysticks: 
- Left Joystick: Left wheel 
- Right Joystick: Right wheel
'''

import curses
import RPi.GPIO as GPIO
import os
import time
import pygame

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)

in1A = 23
in2A = 24
enA = 25

in1B = 22
in2B = 27

GPIO.setup(in1A, GPIO.OUT)
GPIO.setup(in2A, GPIO.OUT)

GPIO.setup(in1B, GPIO.OUT)
GPIO.setup(in2B, GPIO.OUT)

GPIO.output(in1A, GPIO.LOW)
GPIO.output(in2A, GPIO.LOW)

GPIO.output(in1B, GPIO.LOW)
GPIO.output(in2B, GPIO.LOW)

#initialize Pygame (joystick handling)
pygame.init()
pygame.joystick.init()

try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Joystick initialized: {}!!!".format(joystick.get_name()))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                axis1 = joystick.get_axis(1)  #left stick, vertical axis (left wheel)
                axis3 = joystick.get_axis(3)  #right stick, vertical axis (right wheel)

                ## Right Wheel Controls 
                #forward
                if axis3 < -0.1:  
                    GPIO.output(in1A, GPIO.HIGH)
                    GPIO.output(in2A, GPIO.LOW)
                #backward
                elif axis3 > 0.1: 
                    GPIO.output(in1A, GPIO.LOW)
                    GPIO.output(in2A, GPIO.HIGH)
                #stop
                else: 
                    GPIO.output(in1A, GPIO.LOW)
                    GPIO.output(in2A, GPIO.LOW)

                ## Left Wheel Controls
                #forward
                if axis1 < -0.1: 
                    GPIO.output(in1B, GPIO.LOW)
                    GPIO.output(in2B, GPIO.HIGH)
                #backward
                elif axis1 > 0.1:  
                    GPIO.output(in1B, GPIO.HIGH)
                    GPIO.output(in2B, GPIO.LOW)
                #stop 
                else:  
                    GPIO.output(in1B, GPIO.LOW)
                    GPIO.output(in2B, GPIO.LOW)

except KeyboardInterrupt:
    print()
    print("interrupt")

finally:
    GPIO.cleanup()
    pygame.quit()
          
