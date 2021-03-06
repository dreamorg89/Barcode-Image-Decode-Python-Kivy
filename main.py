import sys
import os

import cv2
from pyzbar.pyzbar import decode

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_file("Test.kv")

# Make one method to decode the barcode
class BarcodeScreen(GridLayout):
    def BarcodeReader(self):
        # read the image in numpy array using cv2
        img = cv2.imread('image.jpg')

        # Decode the barcode image
        detectedBarcodes = decode(img)

        # If not detected then print the message
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
        else:
            # Traverse through all the detected barcodes in image
            for barcode in detectedBarcodes:

                # Locate the barcode position in image
                (x, y, w, h) = barcode.rect

                # Put the rectangle in image using
                # cv2 to heighlight the barcode
                cv2.rectangle(img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

                if barcode.data != "":
                    # Print the barcode data
                    print(barcode.data)
                    print(barcode.type)
                    
                    self.ids.my_label.text = "Barcode Data:  "+str(barcode.data)
                    self.ids.my_label2.text = "Barcode Type: "+str(barcode.type)



class Test(App):
    def build(self):
        return BarcodeScreen()


if __name__ == "__main__":
    Test().run()

