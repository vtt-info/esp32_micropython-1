# ESP32 proyects with Micropython

This repository features several proyects implemented on an ESP32 board using micropython firmware.

## Micropython installation on ESP32 board

For the installation of Micropython on your ESP32 board see: [Micropython: Getting Started](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

## Running programs on ESP32 board with ampy

In order to easily edit, run and push files from your computer to your ESP32 board I recommend using [Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) by Adafruit. Edit: Adafruit no longer supports Ampy, however I had no problems following their [latest guide](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) and using Ampy to push code to my ESP32 board.

Once you have installed the firmware on your board, as well as Ampy on your computer, you can clone this repository and proceed to run the included programs on your board and begin experimenting!

To run a program on your board, without actually saving the corresponging code to your board's memory, simply execute `make run` from a terminal on the desired program's directory. This is especially usefull when experimenting with your code. 

Once you are happy with the results and want to save your program to the board's memory to be executed everytime it boots up, execute `make push`.