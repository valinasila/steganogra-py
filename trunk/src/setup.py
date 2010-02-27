# To build a distribution run this on the command line
# C:\Python26/python.exe setup.py py2exe --includes sip 
from distutils.core import setup
import py2exe

setup(name='Steganogra-py',
      windows=['GUI/Steganogra-py.py'], 
      packages=['Logic', 'GUI'], 
      includes=['GUI/MainWindow'],
      excludes=['_imaging_gif', 'ICCProfile'] )