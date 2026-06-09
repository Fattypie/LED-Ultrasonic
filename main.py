from machine import Pin, time_pulse_us
import time

trig = Pin(15, Pin.OUT)
echo = Pin(16, Pin.IN)
led = Pin(14, Pin.OUT)

def get_distance_cm():
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duration = time_pulse_us(echo, 1, 30000)

    if duration < 0:
        return None

    distance = (duration * 0.0343) / 2
    return distance

while True:
    distance = get_distance_cm()

    if distance is None:
        print("No echo")
        led.value(0)
    else:
        print("Distance:", distance, "cm")

        if distance < 20:
            led.value(1)
        else:
            led.value(0)

    time.sleep(0.5)