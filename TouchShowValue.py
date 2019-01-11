import time
import touchphat
import scrollphathd as sphd
from envirophat import weather



@touchphat.on_touch("A")
def show_temp():
    sphd.clear()
    temperature = (' Temp: '+ str(round(weather.temperature(), 1)))
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

@touchphat.on_touch("Enter")
def start_timer():
    sphd.clear()
    sphd.write_string('Timer started', brightness=0.25)
    length = sphd.get_buffer_shape()[0] - 17
    for x in range(length):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)
    time.sleep(1)
    sphd.clear()
    sphd.show()
    touchphat.all_off()
