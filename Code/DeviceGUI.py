#Libraries
from tkinter import *
import sys
import os

# Size of the main window
master = Tk()
master.geometry("500x500") 

# Command definitions
def donothing():
	x = 0
def callback():
	print("click!")
def camera():
	os.system('python3 barcode_scanner_video.py')
def tag():
	os.system('python3 Read.py')

# Create seperate window for QR-code or NFC scanning 
def createWindowQR():
	newWindow = Toplevel()
	msg = Message(newWindow, text = "Open QR code stream")
	msg.grid()
	QR = Button(newWindow, text = "Start stream", command = camera)
	QR.grid()
	QCSV = Button(newWindow, text = "Open CSV", command = donothing)
	QCSV.grid()
	gaNFC = Button(newWindow, text = "NFC tag", command = createWindowNFC)
	gaNFC.grid()

	def close_window():
		newWindow.destroy()
		newWindow.update()

	Terug = Button(newWindow, text = "Startscherm", command = close_window)
	Terug.grid()

def createWindowNFC():
	newWindow = Toplevel()
	msg = Message(newWindow, text = "Start scanning")
	msg.grid()
	NFC = Button(newWindow, text = "Start scannning", command = tag)
	NFC.grid()
	NCSV = Button(newWindow, text = "Open CSV", command = donothing)
	NCSV.grid()

	def close_window():
		newWindow.destroy()
		newWindow.update()

	gaQR = Button(newWindow, text = "QR-code", command = createWindowQR)
	gaQR.grid()
	Terug = Button(newWindow, text = "Startscherm", command = close_window)
	Terug.grid()

# Button declarations
b = Button(master, text = "OK", command = callback)
b.pack()

c = Button(master, text = "QR-codes", command = createWindowQR)
c.pack()

n = Button(master, text = "NFC tags", command = createWindowNFC)
n.pack()

# Menu for choosing what to scan
menubar = Menu(master)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "QR-code", command = createWindowQR)
filemenu.add_command(label = "NFC tag", command = createWindowNFC)
filemenu.add_separator()

# Exit butoon to close the window
filemenu.add_command(label = "Exit", command = master.quit)
menubar.add_cascade(label = "Product", menu = filemenu)

# Help menu to get information about the device
# Some buttons still need a command
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help Index", command = donothing)
helpmenu.add_command(label = "About", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)

master.config(menu = menubar)
master.mainloop()

#mainloop()
