"""Main entry point for all CircuitPython Code. This script will enable a
Feather RP2040 to act like a keyboard with 4 buttons and a volume knob."""


import board
from adafruit_seesaw import seesaw, rotaryio, digitalio

def init_rotary_encoder():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    seesawBoard = seesaw.Seesaw(i2c, addr=0x36)

    seesaw_product = (seesawBoard.get_version() >> 16) & 0xFFFF
    print(f"Found product {seesaw_product}")
    if seesaw_product != 4991:
        print("Wrong firmware loaded?  Expected 4991")

    # Configure seesaw pin used to read knob button presses
    # The internal pull up is enabled to prevent floating input
    seesawBoard.pin_mode(24, seesawBoard.INPUT_PULLUP)
    button = digitalio.DigitalIO(seesawBoard, 24)
    encoder = rotaryio.IncrementalEncoder(seesawBoard)

    return encoder, button

(encoder, button) = init_rotary_encoder()
BUTTON_HELD = False
LAST_POSITION = encoder.position

while True:
    # negate the position to make clockwise rotation positive
    position = encoder.position
    position_delta = LAST_POSITION - position

    if (position_delta < 0):
        LAST_POSITION = position
        print("Up")
    elif (position_delta > 0):
        LAST_POSITION = position
        print("down")

    if not button.value and not BUTTON_HELD:
        BUTTON_HELD = True
        print("Button pressed")

    if button.value and BUTTON_HELD:
        BUTTON_HELD = False
        print("Button released")
