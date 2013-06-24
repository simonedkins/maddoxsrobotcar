'''The simplest Python script in the world to cycle the piface onboard LEDs'''

import piface.pfio as pfio
from time import sleep
from espeak import espeak


pfio.init()


try:
	while True:
		espeak.synth("Turning the lights on")
		for i in range(1,9):
			pfio.digital_write(i,True)
			sleep(0.2)

		sleep(1)
		espeak.synth("Turning the lights off")
		for i in range(1,9):
			pfio.digital_write(i,False)
			sleep(0.2)
		sleep(1)

except KeyboardInterrupt:
	print 'Bye...' 


