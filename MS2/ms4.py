from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [8, 7, 16, 20]]  # LSB → MSB
button = Button(25)
counter = {'value': 0}

def update_leds():
    val = counter['value']
    for i in range(4):
        leds[i].value = (val >> i) & 1

def increment():
    counter['value'] = (counter['value'] + 1) % 16
    update_leds()

button.when_pressed = increment

pause()
