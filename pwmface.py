'''Module to allow PWM control of robot car motors using the piface interfaces'''

import piface.pfio as pfio
from time import sleep
import threading

pfio.init()

class Pwm(threading.Thread):
	def __init__(self, pin=3, f=10.0, dc=0.5):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		self.f = f
		self.dc = dc
		self.pin = pin

	def stop(self):
		self._stop.set()

	def stopped(self):
		return self._stop.isSet()

	def set_dc(self,dc=0.5):
		self.dc = dc
	
	def set_f(self,f=10.0):
		self.f = f

		
	def run(self):
		while not self.stopped():
			total_time = 1/self.f
			on_time = total_time * self.dc
			off_time = total_time - on_time
			pin = self.pin
			pfio.digital_write(pin,True)
			sleep(on_time)
			pfio.digital_write(pin,False)
			sleep(off_time)









if __name__ == '__main__':


	drive = Drive()
	drive.start()
	sleep(5)

	drive.stop()




	print 'ended exec'
	drive.join()
	print 'ended program'
















