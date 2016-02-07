import serial

class FlukeException(Exception):
    pass


class Fluke289:
	def __init__(self,port):
		self.port = serial.Serial(port,115200)
		self.port.timeout = 0.1
		if not self.port.isOpen():
			raise Exception("Failed to open Port" + self.port)

	def _command(self,name):
		self.port.write("{}\r".format(name))
		response = self.port.readall()
		data = response.split("\r")
		ack = data[0]
		if ack == "0":
			pass
		elif ack == "1":
			raise FlukeException("Syntax Error")
		elif ack == "2":
			raise FlukeException("Execution error")
		elif ack == "5":
			raise FlukeException("No data available")
		else:
			raise FlukeException("Invalid Response")
		
		if len(data) > 2:
			return data[1]

	def id(self):
		return self._command("ID") 
		
	def defaultSetup(self):
		self._command("DS")
		
	def resetInstrument(self):
		self._command("RI")
		
	def resetMeterProperties(self):
		self._command("RMP")
		
	def queryPrimaryMeasurement(self):
		response = self._command("QM").split(",")
		value = float(response[0].strip())
		unit = response[1]
		state = response[2]
		return {
			"value":value,
			"unit":unit,
			"state":state
			}
	
	def value(self):
		return self.queryPrimaryMeasurement()["value"]
		

