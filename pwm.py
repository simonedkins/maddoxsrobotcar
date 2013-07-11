import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)







class Wheel():
	def __init__(self, epin, fpin, bpin):
		self.epin = epin
		self.fpin = fpin
		self.bpin = bpin
		self.fq = 10
		self.speed = 100
		
		GPIO.setup(epin,GPIO.OUT)
		GPIO.setup(fpin,GPIO.OUT)
		GPIO.setup(bpin,GPIO.OUT)

	def forwards(self):	
		GPIO.output(self.epin,True)
		self.turn = GPIO.PWM(self.fpin, self.fq)
		self.turn.start(self.speed)
	
	def backwards(self):	
		GPIO.output(self.epin,True)
		self.turn = GPIO.PWM(self.bpin, self.fq)
		self.turn.start(self.speed)

	def stop(self):
		try:
			self.turn.stop()
		except AttributeError:
			pass
		GPIO.output(self.epin,False)

	def set_speed(self, speed):
		self.speed = speed
		self.turn.changeDutyCycle(self.speed)



class RobotCar():
	def __init__(self):
		self.left = Wheel(12,10,8)
		self.right = Wheel(22,24,26)
		self.speed = 50

	def forwards(self):
		self.stop()
		self.left.forwards()
		self.right.forwards()

	def stop(self):
		self.left.stop()
		self.right.stop()

	def turn_left(self):
		self.stop()
		self.right.forwards()

	def turn_right(self):
		self.stop()
		self.left.forwards()


robot_car = RobotCar()

robot_car.forwards()
sleep(5)
robot_car.turn_left()
sleep(3)
robot_car.turn_right()
sleep(3)
robot_car.forwards()
sleep(5)
robot_car.turn_right()
sleep(3)
robot_car.forwards()
sleep(5)
robot_car.stop()




	













