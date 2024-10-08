from machine import Pin, Timer

# Define the LED and button pins
led = Pin(16, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Define a flag to track the button state
button_pressed = False

# Interrupt handler function
def handle_interrupt(pin):
    global button_pressed
    button_pressed = not button_pressed
    led.value(button_pressed)

# Attach the interrupt to the button pin
button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# Timer to simulate round-robin scheduling
def round_robin(timer):
    # Here you can switch between tasks
    print("Switching tasks...")

# Setup a timer to trigger the round-robin scheduler
timer = Timer()
timer.init(freq=1, mode=Timer.PERIODIC, callback=round_robin)

while True:
    # Main loop can perform other tasks
    pass