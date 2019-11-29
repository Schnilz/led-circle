# Led Circle
In this repository you can find the design files (created with [FreeCAD](https://www.freecadweb.org/)) and the code needed to build a small circle which can create some nice looking lighting effects.
I integrated 2 pads made out of copper tape for capacitive touch buttons (using the integrated hardware of the ESP32) to controll the light.


The choosen programming language is [Micropython](https://micropython.org/).

![Rainbow Animation](images/rainbowanim.png?raw=true)


## BOM
- ~50g Filament (white)
- 1x NodeMCU 32S Microcontroller (ESP32)
- 23x WS2812B adressable RGB LEDs
- 1x Sheet of A4 Paper
- 5x small wire pices (i sacrificed a borken usb cable)
- ~2x5cm copper tape / aluminium foil (for the capacitive touch pads)
- hot glue
- 4x screws (and 4x nuts when you dont want to only srew in the printed part)

## Building Instructions
The building time depends mostly on you soldering skills and how clean you want the wiring to look like but should not take long either way.

- After printing both parts you glue the LEDs to the walls of the top part. I put them roughly 1cm below the top edge. The closer the LEDs are to the top the individual lights get more visible, putting them further away make the lights mix more.
- glue the conductive foil to the outside of the top part.
- solder everything up to the ESP32 (3 wires for the LEDs + 2 for either capacitive touch pad)
- put the sheet of paper flat on a (clean) table and put the printed top part on top of it. Then use the hot glue gun on the inside of the part to secure the paper to the top part.
- after the glue is cold place the ESP32 in the bottom part and screw everything together.
- connect everything to the computer and put code on the ESP32. To use wifi you need to create a file called "wifi-credentials" with the ssid in the first line and the password in the secound line. To use the webrepl you have to set it up first using `import webrepl_setup`.

Feel free to open up an issue here on github if you have questions :)

## Licence
The design and code for this project is licenced under GPLv3
