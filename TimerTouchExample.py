import sys
import time
import touchphat
import scrollphathd as sphd
from envirophat import weather

stopped = True
runtime = 0

@touchphat.on_touch("Enter")
def start_stop():
    global start
    global stopped
    global runtime
    if stopped:
        start = time.time()
        stopped = False
    else:
        stopped = True
        runtime += (time.time() - start)

@touchphat.on_touch("Back")
def reset():
    global runtime
    runtime = 0


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

try:
    while True:
        if stopped and runtime > 0:
            sphd.clear()
            sphd.write_string('Timer stopped: ' + str(int(runtime)), brightness=0.25)
            length = sphd.get_buffer_shape()[0] - 17
            for x in range(length):
                sphd.show()
                sphd.scroll(1)
                time.sleep(0.05)
        elif stopped:
            sphd.clear()
            sphd.write_string(' Press enter to start timer ', brightness=0.25)
        else:
            sphd.clear()
            sphd.write_string(str(int(runtime)), brightness=0.25)
            sphd.show()
        time.sleep(0.1)
except KeyboardInterrupt():
    sys.exit()
