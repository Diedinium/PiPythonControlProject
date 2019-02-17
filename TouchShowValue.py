# Designed to work with Python 2.7
# Made by Jake Hall

# Uses the following pHAT components
#   Scroll pHAT HD
#   Enviro pHAT
#   Touch pHAT
#   pHAT stack

# Runs on system boot via lxterminal
# Used to assign functions to button presses from the touchphat

# Imports
import time
import datetime
import touchphat
import scrollphathd as sphd
from envirophat import weather
from envirophat import light
from speechoutput import say_value
from news import get_headline

# Runs "show_temp" on button "A" being pressed
@touchphat.on_touch("A")
def show_temp():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # Declares local variable "degrees", fetches value form weather module and rounds to 1 decimal place
    degrees = round(weather.temperature(), 1)

    # Section that controls speach output
    # "speaktemp" string is set
    speaktemp = ("The temperature is currently " + str(degrees) + " degrees celcius")
    print(speaktemp)
    # "speaktemp" is passed into say_value() function
    say_value(speaktemp)

    # Section taht controls scrollphat output
    # "temperature" string is set
    temperature = (' Temp: ' + str(degrees) + 'C')
    # "temperature" string is written to sphd buffer
    sphd.write_string(temperature, brightness=0.25)
    # Length of buffer is calculated
    length = sphd.get_buffer_shape()[0] - 17
    # Scrolls for the total length value
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    # Sleeps for 1 second once complete
    time.sleep(1)
    # Clears buffer and runs show() to clear display
    sphd.clear()
    sphd.show()
    # Makes sure all button LED's are turned off
    touchphat.all_off()

# Runs "show_light" on button "B" being pressed
@touchphat.on_touch("B")
def show_light():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # variable is set to be the current light value
    lightvalue = light.light()

    # Uses say_value() to speak the current light level
    speaklight = ("The current light level is " + str(lightvalue))
    print(speaklight)
    say_value(x=speaklight)

    # Light value is stored in scrollphat buffer
    lightoutput = (" Light: " + str(lightvalue))
    sphd.write_string(lightoutput, brightness=0.25)
    # Length of buffer is calculated
    length = sphd.get_buffer_shape()[0] - 17
    # Scrolls for the total length value
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    # Sleeps for 1 second once complete
    time.sleep(1)
    # Clears buffer and runs show() to clear display
    sphd.clear()
    sphd.show()
    # Makes sure all button LED's are turned off
    touchphat.all_off()
    
@touchphat.on_touch("C")
def show_pressure():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # Pressure value is fetched from weather module
    pressurevalue = (weather.pressure())

    # Uses say_value() to speak the current pressure value
    speakpressure = ("The current pressure is " + str(round(pressurevalue / 1000, 1)) + " kilopascals")
    print(speakpressure)
    say_value(x=speakpressure)
    
    # Writes the currnet pressure value to scrollphat buffer
    sphd.write_string("Pressure: " + str(round(pressurevalue / 1000, 1)) + " kPa", brightness=0.25)
    # Length of buffer is calculated
    length = sphd.get_buffer_shape()[0] - 17
    # Scrolls for the total length value
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    # Sleeps for 1 second once complete
    time.sleep(1)
    # Clears buffer and runs show() to clear display
    sphd.clear()
    sphd.show()
    # Makes sure all button LED's are turned off
    touchphat.all_off()

# Runs "show_altitude" on button "D" being pressed
@touchphat.on_touch("D")
def show_altitude():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # Altitude value is fetched from weather module
    altitudevalue = weather.altitude()

    # If statement controls if speach output will say "below" or "above" sea level
    if (altitudevalue <= 0):
        sealevel = " meters below sea level"
    elif (altitudevalue >= 1):
        sealevel = " meters above sea level"

    # Uses say_value() to speak the current atititude
    speakaltitude = ("You are roughly " + str(int(altitudevalue)) + sealevel)
    print(speakaltitude) 
    say_value(x=speakaltitude)

    # Writes the current
    sphd.write_string("Altitude: " + str(int(altitudevalue)) + "m", brightness=0.25)
    # Length of buffer is calculated
    length = sphd.get_buffer_shape()[0] - 17
    # Scrolls for the total length value
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    # Sleeps for 1 second once complete
    time.sleep(1)
    # Clears buffer and runs show() to clear display
    sphd.clear()
    sphd.show()
    # Makes sure all button LED's are turned off
    touchphat.all_off()

# Runs "show_datetime" on button "Back" being pressed
@touchphat.on_touch("Back")
def show_datetime():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # Current date/time is stored in "currentDT" variable
    currentDT = datetime.datetime.now()
    # Prints the current time value
    print (currentDT.strftime("%I:%M %p"))

    # Uses say_value() to speak the current time
    speaktime = ("It is currently " + str(currentDT.strftime("%I:%M %p")))
    print(speaktime)
    say_value(speaktime)
    
    sphd.write_string("Time: " + str(currentDT.strftime("%I:%M %p")), brightness=0.25)
    # Length of buffer is calculated
    length = sphd.get_buffer_shape()[0] - 17
    # Scrolls for the total length value
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    # Sleeps for 1 second once complete
    time.sleep(1)
    # Clears buffer and runs show() to clear display
    sphd.clear()
    sphd.show()
    # Makes sure all button LED's are turned off
    touchphat.all_off()

# Runs "show_news" on button "Enter" being pressed
@touchphat.on_touch("Enter")
def show_news():
    # Makes sure scrollphat buffer is clear
    sphd.clear()
    # Uses get_headline() to fetch the NewsAPI JSON document
    content = get_headline()
    # Current date/time is stored in "currentDT" variable
    currentDT = datetime.datetime.now()

    # Below voice output is split into three parts to ensure gaps in speech
    
    # Uses say_value() to say an intro line that includes current time
    introvoice = ('The current BBC news headline as of ' + str(currentDT.strftime("%I:%M %p")))
    say_value(introvoice)

    # Uses say_value() to speak the title from first article in the JSON file
    speaknewstitle = (content['articles'][0]['title'])
    print(speaknewstitle)
    say_value(speaknewstitle)

    # Uses say_value() to speak the description from first article in the JSON file
    speaknewsdesc = (content['articles'][0]['description'])
    print(speaknewsdesc)
    say_value(speaknewsdesc)
    # Makes sure all button LED's are turned off
    touchphat.all_off()
