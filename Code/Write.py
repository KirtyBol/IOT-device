# Libraries
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Reader simplification
reader = SimpleMFRC522()

# To test if it works
try:
	# Type data to write on the tag/card
	text = input('New data: ')
	print("Hold tag at reader")
	reader.write(text)
	# Confirmation it worked
	print("Written")

finally:
	GPIO.cleanup()
