import RPi.GPIO as GPIO   #import the GPIO library
import time #import the time library
import sys
 
buzzer_pin = 22                   
GPIO.setmode(GPIO.BCM)#Use the Broadcom method for naming the GPIO pins
GPIO.setup(buzzer_pin, GPIO.OUT) 
 
def buzz(pitch, duration):   #create the function "buzz" and feed it the pitch and duration)
 period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
 delay = period / 2     #calcuate the time for half of the wave
 cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency
 
 for i in range(cycles):    #start a loop from 0 to the variable "cycles" calculated above
   GPIO.output(buzzer_pin, True)   
   time.sleep(delay)    
   GPIO.output(buzzer_pin, False)    
   time.sleep(delay)  
 
pitch_s = sys.argv[1]
pitch = float(pitch_s)    
duration_s = sys.argv[2]
duration = float(duration_s) 
buzz(pitch, duration)  #feed the pitch and duration to the function, "buzz"