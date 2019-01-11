import scrollphathd as sphd
import time
import math

runAnimation = 1;

while runAnimation == 1:
    t = time.time() * 10
    for x in range(17):
        for y in range(7):
            b = math.sin(x + y + t) + math.cos(x + y + t)
            b = (b + 2) / 4
            sphd.set_pixel(x, y, b)
    sphd.show()
