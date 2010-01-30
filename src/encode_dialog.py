'''
Created on Jan 29, 2010

@author: varzac
'''

from PyQt4.QtGui import *
#from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
#from PyQt4 import uic
#tmp = open('encode_dialog_ui.py', 'w')
#uic.compileUi('encode_dialog.ui', tmp)
#tmp.close()
import encode_dialog_ui
import Image

class EncodeDialog(encode_dialog_ui.Ui_EncodeDialog):
    '''
    classdocs
    '''


    def __init__(self, parent, in_org_im, txt_file, in_enc_im):
        '''
        Constructor
        '''
        self.qd = QDialog(parent)
        self.setupUi(self.qd)
        self.qd.show()
        self.message = (txt_file.split("/")[-1] + " encoded into " + 
        in_org_im.split("/")[-1] + " and written to " + in_enc_im.split("/")[-1] + ".")


        
        print in_org_im
#        tmp = Image.open(in_org_im)
#        tmp.show()
        self.org_im = in_org_im
        print in_enc_im
        self.enc_im = in_enc_im
        
#        self.encoded_label.setPixmap(QtGui.QPixmap(in_enc_im))
        self.encoded_label.setText(self.message)       
        QtCore.QObject.connect(self.view_image_button, QtCore.SIGNAL("clicked()"),
                        self.on_view_image_button_press)

    def on_view_image_button_press(self):
        print "hello world"
        Image.open(self.enc_im,'r').show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = QMainWindow()
    myg = EncodeDialog(tmp,'a.png','b','C:/users/varzac/Projects/Python/Steganogra-py//src/c.png')
    app.exec_()

        