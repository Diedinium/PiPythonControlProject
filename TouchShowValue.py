import time
import datetime
import touchphat
import scrollphathd as sphd
from envirophat import weather
from envirophat import light
from speechoutput import say_value
from news import get_headline

@touchphat.on_touch("A")
def show_temp():
    sphd.clear()
    degrees = round(weather.temperature(), 1)
    
    speaktemp = ("The temperature is currently " + str(degrees) + " degrees celcius")
    print(speaktemp)
    say_value(x=speaktemp)
    
    temperature = (' Temp: ' + str(degrees) + 'C')
    sphd.write_string(temperature, brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

@touchphat.on_touch("B")
def show_light():
    sphd.clear()
    lightvalue = light.light()

    speaklight = ("The current light level is " + str(lightvalue))
    print(speaklight)
    say_value(x=speaklight)
    
    lightoutput = (" Light: " + str(lightvalue))
    sphd.write_string(lightoutput, brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()
    
@touchphat.on_touch("C")
def show_pressure():
    sphd.clear()
    pressurevalue = (weather.pressure())

    speakpressure = ("The current pressure is " + str(round(pressurevalue / 1000, 1)) + " kilopascals")
    print(speakpressure)
    say_value(x=speakpressure)
    
    sphd.write_string("Pressure: " + str(round(pressurevalue / 1000, 1)) + " kPa", brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

@touchphat.on_touch("D")
def show_altitude():
    sphd.clear()
    altitudevalue = weather.altitude(qnh=1020)

    if (altitudevalue <= 0):
        sealevel = " meters below sea level"
    elif (altitudevalue >= 1):
        sealevel = " meters above sea level"

    speakaltitude = ("You are roughly " + str(int(altitudevalue)) + sealevel)
    print(speakaltitude)
    say_value(x=speakaltitude)
    
    sphd.write_string("Altitude: " + str(int(altitudevalue)) + "m", brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

@touchphat.on_touch("Back")
def show_datetime():
    sphd.clear()
    currentDT = datetime.datetime.now()
    print (currentDT.strftime("%I:%M %p"))

    speaktime = ("It is currently " + str(currentDT.strftime("%I:%M %p")))
    print(speaktime)
    say_value(x=speaktime)
    
    sphd.write_string("Time: " + str(currentDT.strftime("%I:%M %p")), brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.03)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

#Runs on an "Enter press
@touchphat.on_touch("Enter")
def show_news():
    sphd.clear()
    content = get_headline()
    currentDT = datetime.datetime.now()

    introvoice = ('The current BBC news headline as of ' + str(currentDT.strftime("%I:%M %p")))
    say_value(introvoice)

    speaknewstitle = (content['articles'][0]['title'])
    print(speaknewstitle)
    say_value(speaknewstitle)

    speaknewsdesc = (content['articles'][0]['description'])
    print(speaknewsdesc)
    say_value(speaknewsdesc)
    touchphat.all_off()
