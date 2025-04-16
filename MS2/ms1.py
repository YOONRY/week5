from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [8, 7, 16, 20]]
button = Button(25)

# 버튼 상태에 따라 LED 전체 on/off
def update_leds():
    if button.is_pressed:
        for led in leds:
            led.on()
    else:
        for led in leds:
            led.off()

# 버튼 상태를 지속적으로 감시
button.when_pressed = update_leds
button.when_released = update_leds

pause()
