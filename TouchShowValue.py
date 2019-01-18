import time
import touchphat
import scrollphathd as sphd
from envirophat import weather
from envirophat import light


@touchphat.on_touch("A")
def show_temp():
    sphd.clear()
    temperature = (' Temp: ' + str(round(weather.temperature(), 1)) + 'C')
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
    lightLevel = (' Light: ' + str(light.light()))
    sphd.write_string(lightLevel, brightness=0.25)
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
def show_light():
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
