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

import sys

from PyQt4.QtGui import *
##from PyQt4 import uic
#tmp = open('UI_progress_dialog.py', 'w')
#uic.compileUi('progress_dialog.ui', tmp)
#tmp.close()

import UI_progress_dialog

class ProgressDialog(UI_progress_dialog.Ui_Dialog):
    """ 
    This is a dialog that will scroll a progress bar as the application is working.
    The bar percentage is not related to the percent of the action completed.  It 
    scrolls continuously to notify the user that the application is working.
    """ 
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