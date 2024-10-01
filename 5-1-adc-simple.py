import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
element=len(dac)
lv=2**element
mVoltage=3.3
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(num):
    return [int(element) for element in bin(num)[2:].zfill(element)]
def num2adc(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
try:
    while True:
        for value in range(256):
            time.sleep(0.001)
            signal = num2adc(value)
            voltage = value/lv*mVoltage
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 1 and voltage!=0: 
                print('adc value = {:^3} -> {}, input voltage = {:.2f}'.format(value, signal, voltage))
                break
except KeyboardInterrupt:
    print('stop')
    
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)