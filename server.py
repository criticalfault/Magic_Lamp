from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
GPIO.setmode(GPIO.BOARD) # set the board numbering system to BCM


GPIO.cleanup() # in case we failed without cleaning up!

# setup our output pins
GPIO.setup(8,GPIO.OUT) #
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

@app.get('/')
def index():
    return template('index')

@app.post('/on')
def on():
	print "Turning Lights On"
	

@app.post('/off')
def off():
	print "Turning Lights Off"
	GPIO.output(8,GPIO.LOW)
	GPIO.output(10,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	GPIO.cleanup()

@app.post('/colorWhite')
def colorWhite():
	print "Turning light white"
	# Turn LEDs on
	GPIO.output(8,GPIO.HIGH)
	GPIO.output(10,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/colorRed')
def colorRed():
	print "Turning light Red"
	# Turn LEDs on
	GPIO.output(8,GPIO.HIGH)
#	GPIO.output(27,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/colorBlue')
def colorRed():
	print "Turning light Blue"
	# Turn LEDs on
	GPIO.output(10,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/colorGreen')
def colorRed():
	print "Turning light Green"
	# Turn LEDs on
	GPIO.output(12,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/shutdown')
def shutdown():
	print "Shutdown"
	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.

run(app, host='localhost', port=8080)	