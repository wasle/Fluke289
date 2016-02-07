 
from Fluke289 import Fluke289

portName = "/dev/ttyUSB2"



f = Fluke289(portName)
f.id()
#f.defaultSetup()
print f.queryPrimaryMeasurement()
print f.value()

while True:
	print f.value()
