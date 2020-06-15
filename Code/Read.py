#Libraries
from mfrc522 import SimpleMFRC522
from PIL import Image

import tkinter
import RPi.GPIO as GPIO
import time
import datetime
import argparse
import cv2
import cv2 as cv

#Create window for the program
#window = tkinter.Tk()
#window.title("NFC")

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type = str, default = "NFC.csv")
args = vars(ap.parse_args())

reader = SimpleMFRC522()

#Open output csv file to see found card ID overview
csv = open(args["output"], "a")
found=set()

#Loop for scanning NFC tags and cards
while True:
	print("Scan card or tag")
	#Information from scanning the card/tag
	id, text = reader.read()
	print("Card ID:", id)
	print("Message: ", text)
	print(" ")
	cardId = id
	textId = text
	#Opening image for the scanned card
	if id == 729242360579:
		img = cv.imread("/home/pi/Pictures/Card.jpg")
		imgS = cv.resize(img, (540, 360))
		cv.imshow("Card image", imgS)
		cv.waitKey(5000)
		cv.destroyAllWindows()
	if id == 576154740089:
		img = cv.imread("/home/pi/Pictures/Tag.jpg")
		imgS = cv.resize(img, (540, 360))
		cv.imshow("Tag image", imgS)
		cv.waitKey(5000)
		cv.destroyAllWindows()
	#If cardId is not in CSV file, write timestamp + cardId
	if cardId not in found:
		csv.write("{}. {}\n".format(datetime.datetime.now(), id))
		csv.flush()
		found.add(cardId)
	#Small delay before scanning next card (testing purpose)
	#time.sleep(5)
	#User input for next step
	step = input("Type 's' for another scan or 'e' to exit program: ")
	if step == "e":
		break
#Close output CSV file
csv.close()
print("Program stopped")
GPIO.cleanup()
#Test purpose
#else:
#	print("Oh no, limit scans for now are made...")
#	GPIO.cleanup()
