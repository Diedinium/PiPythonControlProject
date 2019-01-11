import scrollphathd as sphd
import time
import math
from envirophat import weather

sphd.clear()

print(weather.temperature())

temperature = (' Temp: '+ str(round(weather.temperature(), 1)))

print(temperature)

sphd.write_string(temperature, brightness=0.25)

length = sphd.get_buffer_shape()[0] - 12
print(length)

for x in range(length):
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)

time.sleep(1)
sphd.clear()
sphd.show()
