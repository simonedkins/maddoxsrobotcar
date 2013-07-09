'''Module to allow PWM control of robot car motors using the piface interfaces'''

import piface.pfio as pfio
from time import sleep
import threading

pfio.init()

class Pwm(threading.Thread):
	def __init__(self, pin, f, dc):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		self._pause = threading.Event()
		self.f = f
		self.dc = dc
		self.pin = pin

	def stop(self):
		self._stop.set()

	def pause(self):
		self._pause.set()

	def unpause(self):
		self._pause.clear()

	def paused(self):
		return self._pause.isSet()

	def stopped(self):
		return self._stop.isSet()

	def set_dc(self,dc):
		self.dc = dc
	
	def set_f(self,f):
		self.f = f

		
	def run(self):
		while not self.stopped():
			if not self.paused():
				total_time = 1/self.f
				on_time = total_time * self.dc
				off_time = total_time - on_time
				pin = self.pin
				pfio.digital_write(pin,True)
				sleep(on_time)
				pfio.digital_write(pin,False)
				sleep(off_time)



class Wheel():
	def __init__(self, side, enable_pin, forwards_pin, backwards_pin):
		self.side = side
		self.enable_pin = enable_pin
		self.forwards_pin = forwards_pin
		self.backwards_pin = backwards_pin
		self._speed = 0.5
		self.f = 5.0
		
		pfio.digital_write(self.enable_pin, True)
	
	def forwards(self, speed):
		self.stop()
		self._speed = speed
		pfio.digital_write(self.enable_pin, True)
		self.d = Pwm(pin=self.forwards_pin, f=self.f, dc=self._speed)	
		self.d.start()

	def backwards(self, speed):
		self.stop()
		self._speed = speed
		pfio.digital_write(self.enable_pin, True)
		self.d = Pwm(pin=self.backwards_pin, f=self.f, dc=self._speed)	
		self.d.start()

	def speed(self, speed):
		self._speed = speed
		self.d.set_dc(self._speed)	


	def stop(self):
		try:	
			self.d.stop()
			self.d = None
		except AttributeError:
			pass
	
		pfio.digital_write(self.enable_pin, False)
		pfio.digital_write(self.forwards_pin, False)
		pfio.digital_write(self.backwards_pin, False)



	
















if __name__ == '__main__':


	x = Wheel('left',1,3,7)
	y = Wheel('right',2,4,8)
	x.forwards(1.0)
	y.forwards(0.8)
	sleep(5)
	x.speed(0.2)
	y.speed(0.5)
	sleep(5)
	x.backwards(0.8)
	y.backwards(1.0)
	sleep(5)
	x.speed(1.0)
	x.speed(0.5)
	sleep(5)
	x.stop()
	y.stop()










