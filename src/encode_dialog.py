'''
Created on Jan 29, 2010

@author: varzac
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from PyQt4 import QtGui
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

        QObject.connect(self.view_image_button, SIGNAL("clicked()"),
                        self.on_view_image_button_press)

        self.org_im = in_org_im
        self.enc_im = in_enc_im
        
        self.encoded_label.setText(self.message)       

    def on_view_image_button_press(self):
        tmp = open('test123.txt','w')
        tmp.write('Hello World')
        tmp.close()
#        print "hello world"
 #       Image.open(self.enc_im,'r').show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = QMainWindow()
    myg = EncodeDialog(tmp,'flower2.png','b','flower.png')
    app.exec_()

        