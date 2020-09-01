# PythonSerialCommunication

### Simple Example of communicating with a serial port using python, helpful for Arduino programming or embedded software testing

## Installation:
 To get serial communication working with python the way I did, you're going to need to install pyserial with the command
 `python3 -m pip install pyserial`
 
 but if you want to run my example and see it in action, you're gonna also need to install pysimplegui:
 `python3 -m pip install pysimplegui`
 
 note that if you do run my example that my arduino sketch will only run on an arduino that has the lsm9ds1 imu module, in my case the Arduino Nano 33 Ble Sense, but it's super     simple to create a sketch that communicates with a serial port and you can use my sketch as an example
