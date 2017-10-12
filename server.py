from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM

# setup our output pins
GPIO.setup(8,GPIO.OUT) #
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

GPIO.cleanup() # in case we failed without cleaning up!

@app.get('/')
def index():
    return template('index')

@app.post('/on')
def on():
	print "Turning Lights On"
	

@app.post('/off')
def off():
	print "Turning Lights Off"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)

@app.post('/colorWhite')
def colorWhite():
	print "Turning light white"
	# Turn LEDs on
	GPIO.output(8,True)
	GPIO.output(10,True)
	GPIO.output(12,True)
	sleep(1) # sleep for 1 second

@app.post('/colorRed')
def colorRed():
	print "Turning light Red"
	# Turn LEDs on
	GPIO.output(8,True)
#	GPIO.output(27,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/colorBlue')
def colorRed():
	print "Turning light Blue"
	# Turn LEDs on
	GPIO.output(10,True)
	sleep(1) # sleep for 1 second

@app.post('/colorGreen')
def colorRed():
	print "Turning light Green"
	# Turn LEDs on
	GPIO.output(12,True)
	sleep(1) # sleep for 1 second

@app.post('/shutdown')
def shutdown():
	print "Shutdown"
	GPIO.output(8,False)
	GPIO.output(10,False)
	GPIO.output(12,False)
	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.

run(app, host='192.168.0.35', port=8080)	