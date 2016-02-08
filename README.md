# Fluke289

This is a very basic python library to access the current measuerements from your Fluke287/289.

Simple Example
--------------

```python

from Fluke289 import Fluke289

portName = "/dev/ttyUSB2"

f = Fluke289(portName)
print f.id()

while True:
	print f.value()

```

output:

```
FLUKE 289,V1.00,95680259
0.0
-0.0001
-0.0001
0.0
0.0
```


More Advanced
-------------

```python

from Fluke289 import Fluke289
import pprint

portName = "/dev/ttyUSB2"

f = Fluke289(portName)
print f.id()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(f.queryDisplayedData())
```

output:

```python
{   'lightningBolt': 'OFF',
    'minMaxStartTime': 1454897154.393,
    'modes': ['MIN_MAX_AVG'],
    'primaryFunction': 'V_DC',
    'rangeData': {   'autoRangeState': 'AUTO',
                     'baseUnit': 'VDC',
                     'rangeNumber': 5,
                     'unitMultiplier': 0},
    'readings': {   'AVERAGE': {   'baseUnit': 'VDC',
                                   'decimalPlaces': 4,
                                   'displayDigits': 5,
                                   'readingAttribute': 'NONE',
                                   'readingID': 'AVERAGE',
                                   'readingState': 'NORMAL',
                                   'readingValue': -0.0001,
                                   'readingtimeStamp': datetime.datetime(2016, 2, 8, 3, 6, 11, 291000),
                                   'unitMultiplier': 0},
                    'LIVE': {   'baseUnit': 'VDC',
                                'decimalPlaces': 4,
                                'displayDigits': 5,
                                'readingAttribute': 'NONE',
                                'readingID': 'LIVE',
                                'readingState': 'NORMAL',
                                'readingValue': -0.0001,
                                'readingtimeStamp': datetime.datetime(2016, 2, 8, 3, 6, 11, 291000),
                                'unitMultiplier': 0},
                    'MAXIMUM': {   'baseUnit': 'VDC',
                                   'decimalPlaces': 4,
                                   'displayDigits': 5,
                                   'readingAttribute': 'NONE',
                                   'readingID': 'MAXIMUM',
                                   'readingState': 'NORMAL',
                                   'readingValue': 0.0,
                                   'readingtimeStamp': datetime.datetime(2016, 2, 8, 3, 6, 1, 937000),
                                   'unitMultiplier': 0},
                    'MINIMUM': {   'baseUnit': 'VDC',
                                   'decimalPlaces': 4,
                                   'displayDigits': 5,
                                   'readingAttribute': 'NONE',
                                   'readingID': 'MINIMUM',
                                   'readingState': 'NORMAL',
                                   'readingValue': -0.0001,
                                   'readingtimeStamp': datetime.datetime(2016, 2, 8, 3, 5, 54, 393000),
                                   'unitMultiplier': 0},
                    'PRIMARY': {   'baseUnit': 'VDC',
                                   'decimalPlaces': 4,
                                   'displayDigits': 5,
                                   'readingAttribute': 'NONE',
                                   'readingID': 'PRIMARY',
                                   'readingState': 'NORMAL',
                                   'readingValue': -0.0001,
                                   'readingtimeStamp': datetime.datetime(2016, 2, 8, 3, 6, 11, 291000),
                                   'unitMultiplier': 0}},
    'secondaryFunction': 'NONE'}

```