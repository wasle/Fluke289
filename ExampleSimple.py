 
from Fluke289 import Fluke289

portName = "/dev/ttyUSB2"

f = Fluke289(portName)
print f.id()

while True:
	print f.value()
