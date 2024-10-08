import tasks
import button_h

from machine import Pin

buttonPin = Pin(0, Pin.IN, Pin.PULL_UP)
buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=button_h.button_handler)

arrTasks = [tasks.task1, tasks.task2, tasks.task3]


while True:
    for task in arrTasks:
        task()
