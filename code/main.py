from machine import Pin
from machine import TouchPad, Pin
from neopixel import NeoPixel
from time import sleep
import esp32

NUM_PIXELS = const(23)

led_pin = Pin(25, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(led_pin, NUM_PIXELS)   # create NeoPixel driver on GPIO0 for 8 pixels

t1 = TouchPad(Pin(32)) 	     # left  touchpad
t2 = TouchPad(Pin(13))	     # right touchpad

TOUCH_TRSH = const(250)

t1.config(TOUCH_TRSH)               # configure the threshold at which the pin is considered touched
t2.config(TOUCH_TRSH)

#esp32.wake_on_touch(True)
#machine.lightsleep() 

frame = 1
currentAnim = 1
brightness = 100
BRIGHTNESS_SETTINGS = [3,10,30,50,100,150,255]



def anim_off(pixels,brightness,frame):
	for i in range(NUM_PIXELS):
		pixels[i] = (0,0,0)
	pixels.write()
	sleep(0.08)

def anim_rainbowCircle(pixels,brightness,frame):
	pixels[0] = (0,0,0)
	for i in range(1,NUM_PIXELS):
		pixels[i] = hsv_to_rgb((i+frame/20)%NUM_PIXELS/NUM_PIXELS,1,brightness/256)
	pixels.write()
	sleep(0.08)	
def anim_colorRotate(pixels,brightness,frame):
	#pixels[0] = (0,0,0)
	for i in range(NUM_PIXELS):
		pixels[i] = hsv_to_rgb((frame%300/300),1,brightness/256)
	pixels.write()
	sleep(0.08)

anims = [anim_off,anim_colorRotate,anim_rainbowCircle]

def hsv_to_rgb(h, s, v):
	h_i = int((h*6))
	f = h*6 - h_i
	p = v * (1 - s)
	q = v * (1 - f*s)
	t = v * (1 - (1 - f) * s)
	if h_i==0: r, g, b = v, t, p
	if h_i==1: r, g, b = q, v, p
	if h_i==2: r, g, b = p, v, t
	if h_i==3: r, g, b = p, q, v
	if h_i==4: r, g, b = t, p, v
	if h_i==5: r, g, b = v, p, q
	return (int(r*256), int(g*256), int(b*256))

touchdown = False
while(True):
	if t1.read() < TOUCH_TRSH:
		if not touchdown:
			touchdown = True
			currentAnim = (currentAnim+1) % len(anims)
	elif t2.read() < TOUCH_TRSH:
		if not touchdown:
			touchdown = True
			brightness = BRIGHTNESS_SETTINGS[(BRIGHTNESS_SETTINGS.index(brightness)+1)%len(BRIGHTNESS_SETTINGS)]
	else:
		touchdown = False
	print(t1.read(),t2.read(),brightness,currentAnim)

	anims[currentAnim](np,brightness,frame)
	frame=frame+1
	sleep(0.05)
	#r, g, b = np[0]		  # get first pixel colour
