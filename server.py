from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM

@app.get('/')
def index():
	GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM

	# setup our output pins
	GPIO.setup(8,GPIO.OUT) #
	GPIO.setup(10,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	return template('index')

@app.post('/off')
def off():
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
	print "Turning light Red"
	GPIO.output(8,True)
	sleep(1) # sleep for 1 second
	return {'light': True}

@app.post('/colorBlue')
def colorRed():
	print "Turning light Blue"
	GPIO.output(10,True)
	sleep(1) # sleep for 1 second
	return {'light': True}

@app.post('/colorGreen')
def colorRed():
	print "Turning light Green"
	# Turn LEDs on
	GPIO.output(12,True)
	sleep(1) # sleep for 1 second
	return {'light': True}

@app.post('/shutdown')
def shutdown():
	print "Shutdown"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.
	return {'Shutdown': True}

run(app, host='192.168.0.35', port=8080)	