from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM

redLight = 0
blueLight = 0
greenLight = 0

@app.get('/')
def index():
	GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM
	# setup our output pins
	GPIO.setup(8,GPIO.OUT) #
	GPIO.setup(10,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	global redLight
	global blueLight
	global greenLight
	redLight = 0
	blueLight = 0
	greenLight = 0
	return template('index')

@app.post('/off')
def off():
	global redLight
	global blueLight
	global greenLight
	redLight = 0
	blueLight = 0
	greenLight = 0
	print "Turning Lights Off"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	return {"Off" : True}

@app.post('/colorWhite')
def colorWhite():
	print "Turning light white"
	# Turn LEDs on
	GPIO.output(8,True)
	GPIO.output(10,True)
	GPIO.output(12,True)
	sleep(1) # sleep for 1 second
	return {'light': True}

@app.post('/colorRed')
def colorRed():
	global redLight
	if redLight == 0:
		print "Turning light Red on"
		GPIO.output(8,True)
		redLight = 1
		sleep(1) # sleep for 1 second
		return {'light': True}
	else:
		print "Turning light Red off"
		GPIO.output(8,False)
		redLight = 0
		sleep(1) # sleep for 1 second
		return {'light': False}

@app.post('/colorBlue')
def colorBlue():
	global blueLight
	if blueLight == 0:
		print "Turning light Blue on"
		GPIO.output(10,True)
		sleep(1) # sleep for 1 second
		blueLight = 1
		return {'light': True}
	else:
		print "Turning light Blue off"
		GPIO.output(10,False)
		sleep(1) # sleep for 1 second
		blueLight = 0
		return {'light': False}

@app.post('/colorGreen')
def colorGreen():
	global greenLight
	if greenLight == 0:
		print "Turning light Green on"
		# Turn LEDs on
		GPIO.output(12,True)
		greenLight = 1
		sleep(1) # sleep for 1 second
		return {'light': True}
	else:
		print "Turning light Green off"
		# Turn LEDs on
		GPIO.output(12,False)
		greenLight = 0
		sleep(1) # sleep for 1 second
		return {'light': False}


@app.post('/shutdown')
def shutdown():
	print "Shutdown"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.
	return {'Shutdown': True}

run(app, host='192.168.0.35', port=8080)	