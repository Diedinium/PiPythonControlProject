import time
import datetime
import touchphat
import scrollphathd as sphd
from envirophat import weather
from envirophat import light
from speechtest import say_value

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
        time.sleep(0.05)
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
        time.sleep(0.05)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()
    
@touchphat.on_touch("C")
def show_pressure():
    sphd.clear()
    pressureValue = (' Pressure: ' + str(int(weather.pressure())) + 'hPa')
    sphd.write_string(pressureValue, brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

@touchphat.on_touch("D")
def show_altitude():
    sphd.clear()
    AltitudeValue = (' Altitude: ' + str(int(weather.altitude(qnh=1018))) + 'm')
    sphd.write_string(AltitudeValue, brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()

@touchphat.on_touch("Back")
def show_datetime():
    sphd.clear()
    currentDT = ('DateTime: ' + str(datetime.datetime.now()))
    sphd.write_string(currentDT, brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()
