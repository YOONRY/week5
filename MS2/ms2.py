from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [8, 7, 16, 20]]
button = Button(25)
state = {'on': False}

def toggle_all():
    state['on'] = not state['on']
    for led in leds:
        led.value = state['on']

button.when_pressed = toggle_all

pause()
