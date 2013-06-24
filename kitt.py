'''The simplest Python script in the world to cycle the piface onboard LEDs'''

import piface.pfio as pfio
from time import sleep

pfio.init()

while True:
	for i in range(1,9):
		pfio.digital_write(i,True)
		sleep(0.2)

	for i in range(1,9):
		pfio.digital_write(i,False)
		sleep(0.2)
  
  


