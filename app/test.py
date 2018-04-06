import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
pin = machine.Signal(2, invert=True)

def toggle(p):
    p.value(not p.value())

