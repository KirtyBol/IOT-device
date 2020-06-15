# IOT-device
IOT-device for Graduate internship at Capgemini

## Hardware
* [Raspberry Pi 4b](https://www.kiwi-electronics.nl/raspberry-pi-4/raspberry-pi-4-model-b-4gb "Kiwi Electronics")
* [7" Touschreen Display](https://www.element14.com/community/docs/DOC-78156/l/raspberry-pi-7-touchscreen-display "Element14")
* [Raspberry Pi Camera Board V2](https://www.kiwi-electronics.nl/raspberry-pi-camera-board-v2-8mp?lang=en "Kiwi Elctronics")
* [RFID MFRC522](https://www.tinytronics.nl/shop/nl/communicatie/rfid-kit-mfrc522-s50-mifare-met-kaart-en-key-tag "Tiny Tronics")

## Used Libraries
* [Tkinter](https://docs.python.org/3/library/tk.html): Used to build the GUI
* [OpenCV](https://opencv.org): Computer Vision Library, used to create windows and resize images
* [Zbar](https://pypi.org/project/zbar/): Used to decode QR-codes realtime
* [Imutils](https://pypi.org/project/imutils/): Used for image processing and creating borders around QR-codes in the LiveStream
* [Pillow](https://python-pillow.org): Making sure that the program can open different kinds of content
* [SimpleMFRC522](https://pypi.org/project/mfrc522/): To be able to read and write NFC-tags

## Setup
The setup of the device will be divided in two parts, first the hardware and second the installing of all the libraries on the Raspberry Pi.

### Setup Hardware
1. The Raspberry Pi will be the core of the device, so all the hardware will be connected to this one. You can look up the [Datasheet](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2711/rpi_DATA_2711_1p0_preliminary.pdf) or the [Specs](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/) to find an overview of the location of the ports.
2. Start with connecting the 7" Touchscreen Display, you will need the Display port of the Pi and 4 jumpers to connect to the header pins.
3. Connect the camera using the Camera port on the Pi.
4. You will need 7 jumpers to connect the RFID-reader, click [here](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/) for the Raspberry Pi GPIO Header Guide

| RC522 pin | Raspberry Pi Pin|
|:---------:|:---------------:|
| 3.3V      | Pin 1           |
| RST       | Pin 22          |
| GND       | Pin 6           |
| IRQ       | Unused          |
| MISO      | Pin 21          |
| MOSI      | Pin 19          |
| SCK       | Pin 23          |
| SDA       | Pin 24          |

### Setup Software
1. Update the Raaspberry Pi and the available libraries with: `sudo apt-get update` and `sudo apt-get upgrade`

2. Begin with the RPi.GPIO library, this one is mostly already installed and otherwise use `sudo apt-get install rpi.gpio` 

3. Install the library to beable to use the RFID-reader: `sudo pip3 install mfrc522` (pip3 only if there is python 3 on the Pi)

4. We need to install the OpenCV library to make windows and to be able for example to resize images: `sudo apt-get install python-opencv`

5. For the videostream, install the imutils library: `sudo pip3 install imutils`

6. To be able to decode the QR-codes, install Zbar: `sudo apt-get install libzbar0` and `sudo pip3 install pyzbar`

7. Tkinter is used for the GUI, so the library needs to be installed in order for the program to work and look as aspected: `sudo apt-get install python-tk`

8. Since there will be different types of content and we want to open them all, we will use Pillow: `sudo pip3 install Pillow`

9. Once all the libraries are installed, reboot the Pi: `sudo reboot'

10. Import the this github repository on the Raspberry with `git clone https://github.com/KirtyBol/IOT-device`

11. Navigate into the directory `cd IOT-device\code` and run `python3 DeviceGUI.py`



