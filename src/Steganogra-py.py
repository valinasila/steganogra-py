'''
Copyright (C) 2010 Zachary Varberg
@author: Zachary Varberg

This file is part of Steganogra-py.

Steganogra-py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Steganogra-py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Steganogra-py.  If not, see <http://www.gnu.org/licenses/>.
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import Steganography
#Recompile UI from QT Designer
#from PyQt4 import uic
#tmp = open('MainWindow.py', 'w')
#uic.compileUi('MainWindow.ui', tmp)
#tmp.close()
import MainWindow


class MyGUI(MainWindow.Ui_MainWindow):
    
    def __init__(self):
        self.mw = QMainWindow()
        self.setupUi(self.mw)
        self.mw.show()
        
        self.encode_red_bits = 1
        self.encode_blue_bits = 1
        self.encode_green_bits = 1
        
        self.decode_red_bits = 1
        self.decode_blue_bits = 1
        self.decode_green_bits = 1
        
        self.encode_image_filename = ""
        self.encode_new_image_filename = ""
        self.encode_txt_filename = ""
        
        self.decode_image_filename = ""
        self.decode_txt_filename = ""
        
        # Encode events 
        QObject.connect(self.encode_file_browse_button, SIGNAL("clicked()"),
                        self.on_encode_file_browse_button_press)
        QObject.connect(self.encode_image_browse_button, SIGNAL("clicked()"),
                        self.on_encode_image_browse_button_press)
        QObject.connect(self.encode_new_image_browse_button, SIGNAL("clicked()"),
                        self.on_encode_new_image_browse_button_press)
        QObject.connect(self.encode_new_image_text, SIGNAL("textEdited(QString)"),
                        self.on_encode_new_image_text_change)
        QObject.connect(self.encode_file_text, SIGNAL("textEdited(QString)"),
                        self.on_encode_file_text_change)
        QObject.connect(self.encode_image_text, SIGNAL("textEdited(QString)"),
                        self.on_encode_image_text_change)
        QObject.connect(self.encode_red_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_encode_red_bits_change)
        QObject.connect(self.encode_green_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_encode_green_bits_change)
        QObject.connect(self.encode_blue_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_encode_blue_bits_change)
        QObject.connect(self.encode_button, SIGNAL("clicked()"),
                        self.on_encode_button_press)

        # Decode events
        QObject.connect(self.decode_file_browse_button, SIGNAL("clicked()"),
                        self.on_decode_file_browse_button_press)
        QObject.connect(self.decode_image_browse_button, SIGNAL("clicked()"),
                        self.on_decode_image_browse_button_press)
        QObject.connect(self.decode_file_text, SIGNAL("textEdited(QString)"),
                        self.on_decode_file_text_change)
        QObject.connect(self.decode_image_text, SIGNAL("textEdited(QString)"),
                        self.on_decode_image_text_change)
        QObject.connect(self.decode_red_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_decode_red_bits_change)
        QObject.connect(self.decode_green_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_decode_green_bits_change)
        QObject.connect(self.decode_blue_bits_combo, SIGNAL("currentIndexChanged(int)"),
                        self.on_decode_blue_bits_change)
        QObject.connect(self.decode_button, SIGNAL("clicked()"),
                        self.on_decode_button_press)
        
        
    # Encode event handlers
    def on_encode_file_browse_button_press(self):
        self.encode_txt_filename=str(QFileDialog.getOpenFileName(self.mw, "FileDialog","*.txt"))
        tmp = self.encode_txt_filename.split("/")[-1]
        self.encode_file_text.setText(tmp)

    def on_encode_image_browse_button_press(self):
        self.encode_image_filename=str(QFileDialog.getOpenFileName(self.mw, "FileDialog","*.png"))
        tmp = self.encode_image_filename.split("/")[-1]
        self.encode_image_text.setText(tmp)

    def on_encode_new_image_browse_button_press(self):
        self.encode_new_image_filename=str(QFileDialog.getOpenFileName(self.mw, "FileDialog","*.png"))
        tmp = self.encode_new_image_filename.split("/")[-1]
        self.encode_new_image_text.setText(tmp)
        
    def on_encode_red_bits_change(self, index):
        self.encode_red_bits = (index+1)%9

    def on_encode_green_bits_change(self, index):
        self.encode_green_bits = (index+1)%9
    
    def on_encode_blue_bits_change(self, index):
        self.encode_blue_bits = (index+1)%9

    def on_encode_new_image_text_change(self, myStr):
        self.encode_new_image_filename = str(myStr)

    def on_encode_image_text_change(self, myStr):
        self.encode_image_filename = str(myStr)
    
    def on_encode_file_text_change(self, myStr):
        self.encode_txt_filename = str(myStr)
        
    def on_encode_button_press(self):
        tmp = QErrorMessage(self.mw)
        if (self.encode_image_filename != "" and 
            self.encode_new_image_filename != "" and
            self.encode_txt_filename != ""):
            
        
            try:
                im = Steganography.encode(self.encode_image_filename, self.encode_txt_filename, 
                                          self.encode_red_bits, self.encode_green_bits,
                                          self.encode_blue_bits)
                im.save(self.encode_new_image_filename)
                tmp.showMessage(self.encode_txt_filename.split("/")[-1] + " encoded into " +
                                self.encode_image_filename.split("/")[-1] + " and written to " +
                                self.encode_new_image_filename.split("/")[-1] + ".")
            except Steganography.FileTooLargeException:
                tmp.showMessage(self.encode_txt_filename.split("/")[-1] + 
                                " is to large to be encoded into " +
                                self.encode_image_filename.split("/")[-1])
        else:
            tmp.showMessage("Please specify all filenames.")
            

    # Decode event handlers
    def on_decode_file_browse_button_press(self):
        self.decode_txt_filename=str(QFileDialog.getOpenFileName(self.mw, "FileDialog","*.txt"))
        tmp = self.decode_txt_filename.split("/")[-1]
        self.decode_file_text.setText(tmp)

    def on_decode_image_browse_button_press(self):
        self.decode_image_filename=str(QFileDialog.getOpenFileName(self.mw, "FileDialog","*.png"))
        tmp = self.decode_image_filename.split("/")[-1]
        self.decode_image_text.setText(tmp)
        
    def on_decode_red_bits_change(self, index):
        self.decode_red_bits = (index+1)%9

    def on_decode_green_bits_change(self, index):
        self.decode_green_bits = (index+1)%9
    
    def on_decode_blue_bits_change(self, index):
        self.decode_blue_bits = (index+1)%9

    def on_decode_file_text_change(self, myStr=""):
        self.decode_txt_filename = str(myStr)

    def on_decode_image_text_change(self, myStr=""):
        self.decode_image_filename = str(myStr)
        
    def on_decode_button_press(self):
        tmp = QErrorMessage(self.mw)
        if(self.decode_image_filename != "" and self.decode_txt_filename != ""):
            data = Steganography.decode(self.decode_image_filename, 
                                        self.decode_red_bits, self.decode_green_bits,
                                        self.decode_blue_bits)
            Steganography.save_file(data, self.decode_txt_filename);
            tmp.showMessage(self.decode_image_filename.split("/")[-1] + " decoded and written to " +
                            self.decode_txt_filename.split("/")[-1] + ".")
        else:
            tmp.showMessage("Please specify all filenames.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myg = MyGUI()
    app.exec_()
    
    