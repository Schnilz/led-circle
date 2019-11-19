# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network
import webrepl

webrepl.start()


sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)

#load wifi credentials from file
with open("wifi-credentials","r") as f:
	ssid = f.readline().replace("\n","")
	password = f.readline().replace("\n","")

sta_if.connect(ssid,password)

def printBootFile():
	with open("boot.py") as f:
		for l in f:
			print(l)

