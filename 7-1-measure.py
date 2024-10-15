import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
GPIO.setmode(GPIO.BCM)
sp=[]
sp1=[]
led=[9, 10, 22, 27, 17, 4, 3, 2]
dac = [6, 12, 5, 0, 1, 7, 11, 8]
comp = 14
troyka = 13
element=len(dac)
lv=2**element
mVoltage=3.3
GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
def decimal2binary(num):
    return [int(element) for element in bin(num)[2:].zfill(8)]
def num2adc(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal
def Experiment():
    while True:
        for value in range(256):
            time.sleep(0.001)
            signal = num2adc(value)
            voltage = value/lv*mVoltage
            comparatorValue = GPIO.input(comp)
            if comparatorValue == 1 and voltage!=0: 
                print('adc value = {:^3} -> {}, input voltage = {:.2f}'.format(value, signal, voltage))
                break
            return voltage
try:
    GPIO.otput(troyka, 1)
    for i in range(1000):
        time1=time.time()
        voltage=Experiment()
        sp.append(voltage)
        time2=time.time()
        dt=time2-time1
        sp1.append(dt)
    with open("experiment 1(1).txt","w") as outfile:
        outfile.write("\n".join(map(str,sp)))
    with open("experiment 2(1).txt","w") as outfile:
        outfile.write("\n".join(map(str,sp1)))
    for i in range(1000):
        time3=time.time()
        GPIO.output(troyka, 0)
        voltage=Experiment()
        sp.append(voltage)
        time4=time.time()
        dt=time4-time3
        sp1.append(dt)
    with open("experiment 1(1).txt","w") as outfile:
        outfile.write("\n".join(map(str,sp)))
    with open("experiment 2(1).txt","w") as outfile:
        outfile.write("\n".join(map(str,sp1)))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
