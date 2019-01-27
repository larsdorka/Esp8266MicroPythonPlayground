import machine
import time

from modules import *


def main():
    wifiConnector.run()

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
