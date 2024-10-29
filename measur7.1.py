import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
GPIO.setmode(GPIO.BCM)
led=[9, 10, 22, 27, 17, 4, 3, 2]
dac = [6, 12, 5, 0, 1, 7, 11, 8]
comp = 14
troyka = 13
measured_data=[0]*100000
number_of_measur=0
fl=0
GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 0)
def decimal2binary(num):
    return [int(element) for element in bin(num)[2:].zfill(8)]
t=0.0
Time=0.0
def adc(T):
    global Time
    cc=128
    for i in range(0, 8):
        GPIO.output(dac, decimal2binary(int(cc)))
        time.sleep(0.01)
        T+=0.01
        if(GPIO.input(comp)==0):
            cc+=128/(2**(i+1))
        else:
            cc-=128/(2**(i+1))
    Time+=T
    oc=3.3/256*cc
    return oc, T, int(cc)
try:
    if(input()=='s'):
        GPIO.output(troyka, 1)
        T1=0
        while(1):
            measured_data[number_of_measur]=adc(t)[2]
            if(measured_data[number_of_measur]>=187 and fl==0):
                T1=Time
                break
            number_of_measur+=1
        GPIO.output(troyka, 0)
        while(1):
            measured_data[number_of_measur]=adc(t)[2]
            if(measured_data[number_of_measur]<=20 and fl==0):
                print("time1(время зарядки):", T1, "time2(время эксперимента):", Time-T1)
                break
            number_of_measur+=1
        plt.plot(measured_data[:number_of_measur])
        measured_data_str=[str(item) for item in measured_data[:number_of_measur]]
        with open("exper.txt","w") as outfile:
            outfile.write("\n".join(measured_data_str))
        with open("exper|time.txt","w") as outfile1:
            outfile1.write("Средняя частота дискретизаци:")
            outfile1.write(str(number_of_measur/Time))
            outfile1.write('\n')
            outfile1.write('Шаг квантования АЦП:')
            outfile1.write(str(3.3/255))
        plt.show()
        print('')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()