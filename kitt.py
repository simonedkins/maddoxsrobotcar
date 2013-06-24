'''The simplest Python script in the world to cycle the piface onboard LEDs'''

import piface.pfio as pfio
from time import sleep

pfio.init()

for i in range(1,9):
  pfio.digital_write(i,True)

for i in range(1,9):
  pfio.digital_write(i,False)
  
  


