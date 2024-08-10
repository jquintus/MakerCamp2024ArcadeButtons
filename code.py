"""Main entry point for all CircuitPython Code. This script will enable a
Feather RP2040 to act like a keyboard with 4 buttons and a volume knob."""

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio

import usb_hid
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl

def init_rotary_encoder():
    i2c = board.I2C()  # uses board.SCL and board.SDA
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

def init_hid():
    cc = ConsumerControl(usb_hid.devices)
    return cc

(encoder, button) = init_rotary_encoder()
cc = init_hid()
BUTTON_HELD = False
LAST_POSITION = encoder.position

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
