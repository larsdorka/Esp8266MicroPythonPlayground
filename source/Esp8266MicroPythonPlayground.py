import machine
import time

from modules import *


def main():
    wifiConnector.run()

    i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)
    display.text("MicroPython on", 0, 0)
    display.text("an ESP8266 with an", 0, 10)
    display.text("attached SSD1306", 0, 20)
    display.text("OLED display", 0, 30)
    display.show()

    state = True
    led = machine.Pin(2, machine.Pin.OUT)
    while True:
        if state:
            led.off()
        else:
            led.on()
        state = not state
        time.sleep(0.5)


if __name__ == '__main__':
    main()
