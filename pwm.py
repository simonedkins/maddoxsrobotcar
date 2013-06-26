import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

GPIO.output(12,True)

p = GPIO.PWM(8,20)
q = GPIO.PWM(10,20)

speeds = (25,50,75,100)

while True:
	p.start(0)
	for speed in speeds:
		p.ChangeDutyCycle(speed)
		sleep(5)
	p.stop()

	sleep(3)
	q.start(0)
	for speed in speeds:
		q.ChangeDutyCycle(speed)
		sleep(5)
	q.stop()
	sleep(3)















