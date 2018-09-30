[![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-c-plus-plus.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Northern Lights
*controlling LEDs via RaspberryPi &amp; Arduino*

## Raspberry Pi
	- Python Flask server hosting...
		- Basic UI for controlling the lights
		- API to accept commands and communicate with Arduino via Serial communication

## Arduino
	- Will receive commands from our server and control the LEDs accordingly

## Communication Schema (Raspberry Pi <---> Arduino)
The Pi and Arduino will communicate via 8-bit commands which, if applicable, will be directly followed by a message containing any relevant parameters.

### Commands
	- **_HELLO_** - Command sent by the Pi to request a connection to the Arduino
	- **_HELLO_ACK_** - Command sent by the Arduino to signal that a connection has been accepted
	- **_CONNECTED_** - Command sent by the Arduino to signal a connection is already established
	- **_ACK_** - Command sent by the Arduino to acknowledge the receipt of any non-HELLO command
	- **_DISCONNECT_** - Command sent by the Pi in order to close a connection
	- **_OFF - Command sent by the Pi to turn off all LEDs
	- **_CLEAR_** - Command sent by the Pi to have the Arduino clear it's stored pixel colors
	- **_PIXEL_** - Command sent by the Pi to set a specific LED's color (the LED will not be physically changed until a RELIGHT command is sent)
	- **_RELIGHT_** - Command sent by the Pi to signal that the Arduino should physical LEDs to their current saved states

### Command Parameters
	- **_PIXEL_** -> 32-bit message with bytes representing... pixelIndex | redValue | greenValue | blueValue

