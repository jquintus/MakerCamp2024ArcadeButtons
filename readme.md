This is the project site for a custom keyboard with 4 arcade style buttons and
a volume knob based off of Adafruit's feather boards.

# Hardware and Software dependencies

* [CircuitPython v9.11](https://circuitpython.org/board/adafruit_feather_rp2040/)
* [Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
* [Adafruit I2C Stemma QT Rotary Encoder Breakout with Encoder](https://www.adafruit.com/product/5880)
* [Adafruit LED Arcade Button 1x4 - STEMMA QT I2C Breakout - STEMMA QT / Qwiic](https://www.adafruit.com/product/5296)
* [USB C Round Panel Mount Extension Cable](https://www.adafruit.com/product/4218)
* Arcade Buttons
    * [Green](https://www.adafruit.com/product/3487)
    * [Yellow](https://www.adafruit.com/product/3488)
    * [Red](https://www.adafruit.com/product/3489)
    * [Blue](https://www.adafruit.com/product/3490)

# How to Install
First, install CircuitPython (see below).

## Install via github
1. Plug the board into your computer
2. Delete everything from the device
3. Open up the command prompt and navigate to the CircuitPython drive
4. Clone this repository
5. The board will restart once this is done
6. You can plug the device into any computer (including your cell phone) with a
   USB cable and it should automatically work.

```batch
cd d:\
git init
git remote add origin https://github.com/jquintus/MakerCamp2024ArcadeButtons
git pull origin main
git branch --set-upstream-to=origin/main main
```

This will automatically download and install everything in this github
repository, which includes all dependencies. The board will restart.

# Installing CircuitPython

1. [Install instructions from Adafruit](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
2. [CircuitPython 9.11 for the Feather RP2040](https://circuitpython.org/board/adafruit_feather_rp2040/)
3. Download the .uf2 file from the sie above
4. Plug the board in to your USB drive
5. Wait a second or two for it to fully boot (likely the LED will be changing colors)
6. Hold the `Boot Select` button on the end of the board down while you press and release the `Reset` button by the LED
7. The board will restart quickly
8. You will see a new drive on your computer named `RPI-RP2`
9. Copy the .uf2 file to that drive
10. The device will reboot one more time and you will see another new drive on your computer named `CIRCUITPY`
11. Done.

# Update the Circuit Python Bundles

1. Go to the [CircuitPython](https://circuitpython.org/libraries) Website
2. Download the latest bundle for 9.x
3. Unzip the file
4. Select the libs you need and drop them into the `CIRCUITPY/lib` folder

# Useful Tutorials and Documentation

* [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview)
* [Adafruit I2C QT Rotary Encoder](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython)
* [Adafruit LED Arcade Button 1x4 STEMMA QT](https://learn.adafruit.com/adafruit-led-arcade-button-qt)
* [Introducing Adafruit Feather RP2040](https://learn.adafruit.com/adafruit-feather-rp2040-pico/overview)
* [CircuitPython HID Keyboard and Mouse](https://learn.adafruit.com/adafruit-feather-m0-express-designed-for-circuit-python-circuitpython/circuitpython-hid-keyboard-and-mouse)
    * This is for differnt hardware, but the demo code should work pretty well.
* [Adafruit HID Library](https://docs.circuitpython.org/projects/hid/en/latest/)
    * Useful for Keycodes and ConsumerControlCodes (Play/Pause, volume, etc)
 
# Housing Diagrams
## Data Sheet for Arcade Buttons
![Data Sheet for Arcade Buttons](https://github.com/user-attachments/assets/26038298-0e7b-44b6-8844-da17a81cbcfe)
