import touchphat
import time

@touchphat.on_touch(["Back", "A", "B", "C", "D", "Enter"])
def handle_touch(event):
    print("Button %s pressed!") % event.name


