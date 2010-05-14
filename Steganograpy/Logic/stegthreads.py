'''
Created on Feb 6, 2010

@author: Zachary Varberg
'''

from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, SIGNAL
import steganography
import time

class EncodeWorker(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.image_filename = ""
        self.txt_filename = ""
        self.new_image_filename = ""
        
    def setup(self, in_im_file, txt_file, out_im_file, bits=[1, 1, 1]):
        self.image_filename = in_im_file
        self.txt_filename = txt_file
        self.new_image_filename = out_im_file
        self.red_bits = bits[0]
        self.green_bits = bits[1]
        self.blue_bits = bits[2]
        self.start()
        
    def run(self):
        try:
            im = steganography.encode(self.image_filename, self.txt_filename, 
                                      [self.red_bits, self.green_bits,
                                      self.blue_bits])
            im.save(self.new_image_filename)
            self.emit(SIGNAL("complete()"))
        except steganography.FileTooLargeException:
            self.emit(SIGNAL("error()"))



class DecodeWorker(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.image_filename = ""
        self.txt_filename = ""
        
    def setup(self, im_file, txt_file, bits=[1,1,1]):
        self.image_filename = im_file
        self.txt_filename = txt_file
        self.red_bits = bits[0]
        self.green_bits = bits[1]
        self.blue_bits = bits[2]
        self.start()
        
    def run(self):
        data = steganography.decode(self.image_filename, 
                                    [self.red_bits, self.green_bits,
                                    self.blue_bits])
        steganography.save_file(data, self.txt_filename);
        self.emit(SIGNAL("complete()"))
        
class ProgressWorker(QThread):
    
    def __init__(self, progDia, parent = None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.progress_dialog = progDia
        
    def run(self):
        while(not self.exiting):
            self.progress_dialog.increment()
            time.sleep(.01)
            
    def end(self):
        self.exiting = True
        
    def __del__(self):
        self.exiting = True
        self.wait()