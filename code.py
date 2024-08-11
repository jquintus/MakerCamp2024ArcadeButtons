"""Main entry point for all CircuitPython Code. This script will enable a
Feather RP2040 to act like a keyboard with 4 buttons and a volume knob."""

import time
import board
import usb_hid
import digitalio as board_digitalio

from adafruit_seesaw import seesaw, rotaryio, digitalio
from adafruit_seesaw.pwmout import PWMOut
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl


def init_i2c():
    print("Initializing I2C...")
    i2c = board.I2C()  # uses board.SCL and board.SDA
    return i2c

def init_rotary_encoder(i2c):
    print("Initializing rotary encoder...")
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

def init_button(arcade_qt, pin):
    print("Initializing button...")
    button = digitalio.DigitalIO(arcade_qt, pin)
    button.direction = board_digitalio.Direction.INPUT
    button.pull = board_digitalio.Pull.UP

    return button

def init_buttons(i2c):
    print("Initializing leds and buttons...")
    arcade_qt = seesaw.Seesaw(i2c, addr=0x3A)

    print("Initializing leds...")
    led1 = digitalio.DigitalIO(arcade_qt, 12)
    led2 = digitalio.DigitalIO(arcade_qt, 13)
    led3 = digitalio.DigitalIO(arcade_qt, 0)
    led4 = digitalio.DigitalIO(arcade_qt, 1)

    print("Initializing buttons...")
    button1 = init_button(arcade_qt, 18)
    button2 = init_button(arcade_qt, 19)
    button3 = init_button(arcade_qt, 20)
    button4 = init_button(arcade_qt, 2)

    return ((led1, led2, led3, led4), (button1, button2, button3, button4))

def init_hid():
    print("Initializing HID...")
    cc = ConsumerControl(usb_hid.devices)
    return cc

i2c = init_i2c()
cc = init_hid()
(encoder, button) = init_rotary_encoder(i2c)
((led1, led2, led3, led4), (button1, button2, button3, button4)) = init_buttons(i2c)

BUTTON_HELD = False
LAST_POSITION = encoder.position

button1_held = False
button2_held = False
button3_held = False
button4_held = False

print("Ready to start")
while True:
    position = encoder.position
    position_delta = LAST_POSITION - position

    if (position_delta < 0):
        LAST_POSITION = position
        cmd = ConsumerControlCode.VOLUME_INCREMENT
        cc.send(cmd)
        print("Up")

    elif (position_delta > 0):
        LAST_POSITION = position
        cmd = ConsumerControlCode.VOLUME_DECREMENT
        cc.send(cmd)
        print("down")

    if not button.value and not BUTTON_HELD:
        BUTTON_HELD = True
        #cmd = ConsumerControlCode.BRIGHTNESS_DECREMENT         # Decrease the monitor brightness
        #cmd = ConsumerControlCode.BRIGHTNESS_INCREMENT         # Increase the monitor brightness
        #cmd = ConsumerControlCode.EJECT                        # No impact when using Spotify
        #cmd = ConsumerControlCode.FAST_FORWARD                 # Jump ahead 5 seconds
        #cmd = ConsumerControlCode.MUTE                         # Mute/unmue audio
        cmd = ConsumerControlCode.PLAY_PAUSE                   # Play or Pause
        #cmd = ConsumerControlCode.RECORD                       # No impact when using Spotify
        #cmd = ConsumerControlCode.REWIND                       # No impact when using Spotify
        #cmd = ConsumerControlCode.SCAN_NEXT_TRACK              # Skip to Next Track
        #cmd = ConsumerControlCode.SCAN_PREVIOUS_TRACK          # Go to previous track
        #cmd = ConsumerControlCode.STOP                         # Stop. Unlike Pause, this will not start playing again if pressed a second time
        cc.send(cmd)

    if button.value and BUTTON_HELD:
        BUTTON_HELD = False

    # Button 1
    if not button1.value and not button1_held:
        button1_held = True
        led1.value = True

    if button1.value and button1_held:
        button1_held = False
        led1.value = False

    # Button 2
    if not button2.value and not button2_held:
        button2_held = True
        led2.value = True

    if button2.value and button2_held:
        button2_held = False
        led2.value = False

    # Button 3
    if not button3.value and not button3_held:
        button3_held = True
        led3.value = True

    if button3.value and button3_held:
        button3_held = False
        led3.value = False

    # Button 4
    if not button4.value and not button4_held:
        button4_held = True
        led4.value = True

    if button4.value and button4_held:
        button4_held = False
        led4.value = False
