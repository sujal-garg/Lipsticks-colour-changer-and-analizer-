
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
import os
import dlib
import pyshine as ps
def savePhoto(self):
	""" This function will save the image"""
	rgb=self.lipstick_RGB
	image = self.tmp
	text  =  self.color_selected_text
	image = ps.putBText(image,text,text_offset_x=10,text_offset_y=10,font_scale=0.6,background_RGB=rgb,text_RGB=(255,255,255))
	filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
	cv2.imwrite(filename,image)
	print('Image saved as:',filename)


def retranslateUi(self, MainWindow):
	_translate = QtCore.QCoreApplication.translate
	MainWindow.setWindowTitle(_translate("MainWindow", "PyShine video process"))
	self.pushButton_2.setText(_translate("MainWindow", "Start"))
	self.label_2.setText(_translate("MainWindow", "Brightness"))
	self.label_3.setText(_translate("MainWindow", "Blur"))
	self.pushButton.setText(_translate("MainWindow", "Take picture"))
	
if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
