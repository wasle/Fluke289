 
from Fluke289 import Fluke289
import pprint

portName = "/dev/ttyUSB2"

f = Fluke289(portName)
print f.id()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(f.queryDisplayedData())
