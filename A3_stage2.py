from microbit import *
import neopixel
import music

display.show(Image.HAPPY)

sleep(1000)

display.clear()

num_pixels = 30
np = neopixel.NeoPixel(pin1, num_pixels)

def range_map(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


off = (0, 0, 0)
led = num_pixels - 1

while True:
    start_signal = accelerometer.current_gesture()
    np.clear()

    if start_signal == "shake":
        for pixel_id in range(num_pixels):
            np[pixel_id] = (0, 255, 0)
            np.show()
            sleep(100)

        sleep(10000)


        # make a loop using counter to reduce each light

        while led > 0:
            np[led] = off
            np.show()
            sleep(1000)
            led -= 1

        music.play(music.POWER_DOWN)

        threshold = 0   # threshold for trigger LEDs
        led_num = 0
        mapped_red = range_map(led_num, 0, 30, 255, 0)
        mapped_green = range_map(led_num, 0, 30, 100, 255)

        while True:

            gesture = accelerometer.current_gesture()

            if led_num < 30:
                if gesture == "shake":
                    threshold += 1
                    if threshold == 10:
                        np[led_num] = (int(mapped_red), int(mapped_green), 0)
                        np.show()
                        threshold = 0
                        led_num += 1
                        sleep(100)

                elif gesture == "freefall":
                   # threshold += 1
                    #if threshold == 10:
                    np[led_num] = (int(mapped_red), int(mapped_green), 0)
                    np.show()
                    led_num += 1
                    sleep(500)

            else:
                music.play(music.POWER_UP)
                break
    else:
        sleep(1000)
        continue
