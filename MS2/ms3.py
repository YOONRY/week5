from gpiozero import LED, Button
from time import sleep
from signal import pause

leds = [LED(pin) for pin in [8, 7, 16, 20]]
button = Button(25)

def domino():
    for led in leds:
        led.on()
        sleep(0.2)
    for led in leds:
        led.off()
        sleep(0.2)

button.when_pressed = domino

pause()
