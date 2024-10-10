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

def init_buttons(i2c, addr):
    print("Initializing leds and buttons...")
    arcade_qt = seesaw.Seesaw(i2c, addr)

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
(encoder, encoder_button) = init_rotary_encoder(i2c)
((led1, led2, led3, led4), (button1, button2, button3, button4)) = init_buttons(i2c, addr=0x3A)
((red_led, green_led, yellow_led, blue_led), (red_button, green_button, yellow_button, blue_button)) = init_buttons(i2c, 0x3A)

encoder_button_held = False
LAST_POSITION = encoder.position

red_button_held = False
green_button_held = False
yellow_button_held = False
blue_button_held = False

button5_held = False
button6_held = False
button7_held = False
button8_held = False

print("Ready to start")

def flash_the_lights(value):
    green_led.value = value
    time.sleep(0.1)

    blue_led.value = value
    time.sleep(0.1)

    yellow_led.value = value
    time.sleep(0.1)

    red_led.value = value


flash_the_lights(True)
time.sleep(0.1)
flash_the_lights(False)



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

    if not encoder_button.value and not encoder_button_held:
        encoder_button_held = True
        #cmd = ConsumerControlCode.BRIGHTNESS_DECREMENT         # Decrease the monitor brightness
        #cmd = ConsumerControlCode.BRIGHTNESS_INCREMENT         # Increase the monitor brightness
        #cmd = ConsumerControlCode.EJECT                        # No impact when using Spotify
        #cmd = ConsumerControlCode.FAST_FORWARD                 # Jump ahead 5 seconds
        cmd = ConsumerControlCode.MUTE                         # Mute/unmue audio
        #cmd = ConsumerControlCode.PLAY_PAUSE                   # Play or Pause
        #cmd = ConsumerControlCode.RECORD                       # No impact when using Spotify
        #cmd = ConsumerControlCode.REWIND                       # No impact when using Spotify
        #cmd = ConsumerControlCode.SCAN_NEXT_TRACK              # Skip to Next Track
        #cmd = ConsumerControlCode.SCAN_PREVIOUS_TRACK          # Go to previous track
        #cmd = ConsumerControlCode.STOP                         # Stop. Unlike Pause, this will not start playing again if pressed a second time
        cc.send(cmd)
        print ("Button 0 pressed - Mute")

    if encoder_button.value and encoder_button_held:
        encoder_button_held = False

    # Red Button
    if not red_button.value and not red_button_held:
        red_button_held = True
        red_led.value = True

        cmd = ConsumerControlCode.SCAN_PREVIOUS_TRACK          # Go to previous track
        cc.send(cmd)
        print ("Red button pressed - Previous Track")

    if red_button.value and red_button_held:
        red_button_held = False
        red_led.value = False
        print ("Red button released")

    # Green button
    if not green_button.value and not green_button_held:
        green_button_held = True
        green_led.value = True

        cmd = ConsumerControlCode.PLAY_PAUSE                   # Play or Pause
        cc.send(cmd)
        print ("Green button pressed - Play/Pause")

    if green_button.value and green_button_held:
        green_button_held = False
        green_led.value = False
        print ("Green button released")

    # Button Yellow
    if not yellow_button.value and not yellow_button_held:
        yellow_button_held = True
        yellow_led.value = True

        cmd = ConsumerControlCode.SCAN_NEXT_TRACK              # Skip to Next Track
        cc.send(cmd)
        print ("Yellow button pressed - Skip Track")

    if yellow_button.value and yellow_button_held:
        yellow_button_held = False
        yellow_led.value = False
        print ("Yellow button released")

    # Blue button
    if not blue_button.value and not blue_button_held:
        blue_button_held = True
        blue_led.value = True

        cmd = ConsumerControlCode.MUTE                         # Mute/unmue audio
        cc.send(cmd)
        print ("Blue Button pressed - Mute")

    if blue_button.value and blue_button_held:
        blue_button_held = False
        blue_led.value = False
        print ("Blue button released")
