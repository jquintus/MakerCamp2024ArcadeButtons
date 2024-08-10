This is the project site for a custom keyboard with 4 arcade style buttons and
a volume knob based off of Adafruit's feather boards.

# Hardware and Software dependencies

* [CircuitPython v9.11](https://circuitpython.org/board/adafruit_feather_rp2040/)
* [Adafruit Feather RP2040](https://www.adafruit.com/product/4884)
* [Adafruit I2C Stemma QT Rotary Encoder Breakout with Encoder](https://www.adafruit.com/product/5880) 
* [USB C Round Panel Mount Extension Cable](https://www.adafruit.com/product/4218)
* Arcade Buttons
    * [Green](https://www.adafruit.com/product/3487)
    * [Yellow](https://www.adafruit.com/product/3488)
    * [Red](https://www.adafruit.com/product/3489) 
    * [Blue](https://www.adafruit.com/product/3490) 

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

# Useful Tutorials

* [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/overview) 
* [Adafruit I2C QT Rotary Encoder](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) 
* [Introducing Adafruit Feather RP2040](https://learn.adafruit.com/adafruit-feather-rp2040-pico/overview)
