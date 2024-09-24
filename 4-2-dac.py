import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
def decimal2binary(num):
    return [int(element) for element in bin(num)[2:].zfill(8)]
GPIO.setup(dac, GPIO.OUT)
try:
    print("Введите период")
    Period = float(input())
    while(True):
        for i in range(0, 255, 1):
            num = i
            GPIO.output(dac, decimal2binary(num))
            time.sleep(Period/510)
        for i in range(255, 0, -1):
            num = i
            GPIO.output(dac, decimal2binary(num))
            time.sleep(Period/510)
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()