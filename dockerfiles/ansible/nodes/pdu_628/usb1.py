#!/usr/bin/python

import time
import serial
import re

ser = serial.Serial('/dev/ttyUSB1', 19200, timeout=1)

print "opened ttyUSB1"

b = 1;

while (b):
	ser.write("attn -D")
	ser.write("\n")
	time.sleep(1)
	c = ser.inWaiting()
	sn = ser.read(c)
	print sn
	if (c > 0):
		(serial, unit) = sn[2:c].split(" ")
		b = 0
	else:
		print "try again.."
		time.sleep(2)

print "serial %s, unit %d\n" % ( serial, int(unit))
print "node is awake"

settings = [
	"stty 19200\n\n",
	"attn -p1\n\n",
	"attn -W1234\n\n",
	"stty -M1\n\n",
	"stty -W1234\n\n",
	"exit\n"
]

a = "attn -S%s -5lEvElbAl\n" % (serial)

print "a = %s" % a

b = 1
ser.write(a)
ser.write("\n")
time.sleep(0.5)
c = ser.inWaiting()
sn = ser.read(c)
print sn

while (b):
	ser.write("\n")
	time.sleep(0.5)
	c = ser.inWaiting()
	prompt = ser.read(c)
	print "!%s!" % prompt[2:5]
	if (prompt[2:5] == "CIP"):
		b = 0

for item in settings:
	b = 1
	while (b):
		print "sending item %s" % item,
		ser.write(item)
		time.sleep(0.1)
		c = 1
		while(c):
			prompt = ser.read(c)
			print prompt,
			if ((prompt == "#") | (prompt == "/")):
				b = 0
				c = 0
