'''The simplest Python script in the world to cycle the piface onboard LEDs'''

import piface.pfio as pfio
from time import sleep
from espeak import espeak


pfio.init()


try:

	espeak.synth('Hello Maddox, this is your robot car brain speaking. I just wanted to say goodnight and I hope my wheels arrive soon. Bye bye from your robot brain')
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


