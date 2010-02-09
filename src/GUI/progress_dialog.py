'''
Created on Feb 8, 2010

@author: Zachary Varberg
'''
#from PyQt4 import uic
#tmp = open('UI_progress_dialog.py', 'w')
#uic.compileUi('progress_dialog.ui', tmp)
#tmp.close()
import UI_progress_dialog
from PyQt4.QtGui import *
import sys
import time


class ProgressDialog(UI_progress_dialog.Ui_Dialog):
    def __init__(self, parent=None):
        self.qd = QDialog(parent)
        self.setupUi(self.qd)
        self.val = 0
        self.progressBar.setValue(0)
        
    def increment(self):
        self.val += 1
        self.progressBar.setValue(self.val%100)
        
    def show(self):
        self.qd.show()
    
    def hide(self):
        self.qd.setVisible(False)
        self.val = 0
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tmp = QMainWindow()
    myg = ProgressDialog(tmp)
    myg.run()
    app.exec_()