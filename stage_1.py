y# A micro:bit sports recharge
# By Yizun Zhang

from microbit import *
from ultrasonic import *
import neopixel
import music

def range_map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

rf = Rangefinder(pin0)
i = 0
dist_list = [0.1] # Add an initial value to the list.
threshold = 0 # threshold for trigger LEDs
led_num = 1

np = neopixel.NeoPixel(pin1, 30)
np[0] = (255, 0, 0)
np.show()

while True:
    dist = rf.distance_cm()
    dist_list.append(dist)
    val = abs(dist - dist_list[i]) # Absolute value of difference of two distance

    #mapped R&G value on 30 leds strip to achieve gradient color from red to green
    mapped_red = range_map(led_num, 1, 30, 255, 0)
    mapped_green = range_map(led_num, 1, 30, 100, 255)

    # Compare absolute value of difference with value 1 to estimate whether move or not.
    if  val > 1:
        threshold += 1
        if threshold == 10:
            np[led_num] = (int(mapped_red), int(mapped_green), 0)
            np.show()
            threshold = 0
            led_num += 1
            music.play(music.JUMP_UP)

        elif led_num == 30:
            music.play(music.POWER_UP)

    else:
        threshold -= 1
        if threshold == -20:
            np.clear()
            sleep(100)
            np[0] = (255, 0, 0)
            np.show()
            led_num = 1
            music.play(music.POWER_DOWN)

    i += 1
    sleep(200)