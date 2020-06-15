from imutils.video import VideoStream
from pyzbar import pyzbar
from tkinter import *

import argparse
import datetime
import imutils
import time
import cv2
import sys
import os

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv", help="Path to output CSV file containig barcodes")
args=vars(ap.parse_args())

master = Tk()
master.geometry("500x500")

#def startStream():
	#initialize videostream
print("[INFO] Starting video stream..")

vs=VideoStream(usePiCamera=True).start()
time.sleep(2.0)

	#Open output CSV file to see barcodes found
csv = open(args["output"], "a")
found=set()

	#Loop over the frames
while True:
	frame=vs.read()
	frame=imutils.resize(frame, width=400)

	#Find the barcodes
	barcodes=pyzbar.decode(frame)

	#Loop over found barcodes
	for barcode in barcodes:
		(x, y, w, h)=barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		#Barcode data from bytes to string
		barcodeData=barcode.data.decode("utf-8")
		barcodeType=barcode.type
			#Draw barcode data and type on the image
		text="{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		#If data is not in CSV, write timestamp + barcode
		if barcodeData not in found:
			csv.write("{}. {}\n".format(datetime.datetime.now(), barcodeData))
			csv.flush()
			found.add(barcodeData)
	#show output frame
	cv2.imshow("Barcode scanner", frame)
	key=cv2.waitKey(1) & 0xFF
	#If 'q' is pressed, exit loop
	if key == ord("q"):
		break

#def stopStream():
#Close output CSV file
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()

#b = Button(master, text = "Start", command = startStream)
#b.pack()

#c = Button(master, text = "Stop", command = stopStream)
#c.pack()

'''
menubar = Menu(master)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Start Stream", command = startStream)
filemenu.add_command(label = "Open CSV", command = doNothing)

master.config(menu = menubar)
master.mainloop
'''
