# PiPythonControlProject
An experimental Pi python code project for a college control systems project.

## General info
Uses 5 different hardware compoents:
* Raspberry Pi 3B+
* Enviro pHAT
* Scroll pHAT HD
* Touch pHAT
* pHAT stack

Operates though presses of buttons on the Touch pHAT - these presses activate event handlers which run a function. 
These functions will then scroll a message on the Scroll pHAT HD while via the GCP Text to speech API there will be voice output as well.
All the pHAT components are connected to the Pi via the pHAT stack, which provides the capacity for up to 5 different pHAT's all connected to 
one device.

## Code libraries/API's used

Raspberry Pi is running Raspbian.

Enviro pHAT code library:

https://github.com/pimoroni/enviro-phat

Scroll pHAT HD code library:

https://github.com/pimoroni/scroll-phat-hd

Touch pHAT code library:

https://github.com/pimoroni/touch-phat

Using Google Cloud Platform text to speech API for custom voice responses:

https://cloud.google.com/

Using NewsAPI for current news headline retrieval:

https://newsapi.org/docs/get-started
