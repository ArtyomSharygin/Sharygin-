import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
def decimal2binary(num):
    return [int(element) for element in bin(num)[2:].zfill(8)]
GPIO.setup(dac, GPIO.OUT)
try:
    while(1):
        print("Введите число от 0 до 255")
        num = float(input())
        rounded_num = round(num)
        print(decimal2binary(rounded_num))
        GPIO.output(dac, decimal2binary(rounded_num))
        voltage=3,3/256*rounded_num
        print(voltage)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()