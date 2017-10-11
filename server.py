from bottle import Bottle, route, run, template
from time import sleep # import the time function from the sleep library
#import RPi.GPIO as GPIO # import our GPIO library

app = Bottle()
#GPIO.setmode(GPIO.BCM) # set the board numbering system to BCM

# setup our output pins
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)


@app.get('/')
def index():
    return template('index')

@app.post('/on')
def on():
	print "Turning Lights On"
#	GPIO.output(17,GPIO.LOW)
#	GPIO.output(27,GPIO.LOW)

@app.post('/off')
def off():
	print "Turning Lights Off"
#	GPIO.output(17,GPIO.LOW)
#	GPIO.output(27,GPIO.LOW)

@app.post('/colorWhite')
def colorWhite():
	print "Turning light white"
	# Turn LEDs on
#	GPIO.output(17,GPIO.HIGH)
#	GPIO.output(27,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/colorRed')
def colorRed():
	print "Turning light white"
	# Turn LEDs on
#	GPIO.output(17,GPIO.HIGH)
#	GPIO.output(27,GPIO.HIGH)
	sleep(1) # sleep for 1 second

@app.post('/shutdown')
def shutdown():
	print "Shutdown"
#	GPIO.cleanup() # the clean-up function will reset all the configurations made in this script. This will stop the warnings we got from the tutorial 2.

run(app, host='localhost', port=8080)	