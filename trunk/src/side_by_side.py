'''
Created on Jan 29, 2010

@author: Zachary Varberg
'''
from PyQt4 import uic
tmp = open('side_by_side_ui.py', 'w')
uic.compileUi('side_by_side.ui', tmp)
tmp.close()
import side_by_side_ui
import sys
from PyQt4.QtGui import *



class SideBySideDialog(side_by_side_ui.Ui_Dialog):
    '''
    classdocs
    '''


    def __init__(self, parent, im1_filename, im2_filename):
        '''
        Constructor
        '''
        self.qd = QDialog(parent)
        self.setupUi(self.qd)
        self.qd.show()

        self.left_image_label.setPixmap(QPixmap(im1_filename))
        self.right_image_label.setPixmap(QPixmap(im2_filename))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = QMainWindow()
    myg = SideBySideDialog(tmp, 'lena.png','lena.png')
    app.exec_()


        