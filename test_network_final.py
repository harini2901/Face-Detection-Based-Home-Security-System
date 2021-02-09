

# import the necessary packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import serial
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
orig = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (28, 28))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network
print(" loading network...")
model = load_model(args["model"])

# classify the input image
(notOwner, owner) = model.predict(image)[0]

# build the label
label = "Owner" if owner > notOwner else "Not_Owner"
label1 = "Owner" if owner > notOwner else "Not_Owner"
proba = owner if owner > notOwner else notOwner
label = "{}: {:.2f}%".format(label, proba * 100)

# draw the label on the image
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

output1 = 0

if label1 == "Owner" :
  output1 = 1

arduinoData=serial.Serial('/dev/ttyACM1', 9600)

def led_on():
	arduinoData.write(b'1')

def led_off():
	arduinoData.write(b'0')

datafromOutput=output1

if datafromOutput == '1':
	#print("The detected person is Owner,green light will be glown to indicate this")
	led_on()
elif datafromOutput == '0':
        #print("The detected person is NotOwner,red light will be glown to indicate this")
	led_off()

# show the output image
cv2.imshow("Output", output)
cv2.waitKey(0)
