# To build a distribution run this on the command line
# C:\Python26/python.exe setup.py py2exe --includes sip 
from distutils.core import setup
import py2exe

setup(name='Steganogra-py',
      windows=[{'script':'GUI/Steganogra-py.py','icon_resources':[(1,'Resources/stegosaurus.ico')]}], 
      packages=['Logic', 'GUI'], 
      includes=['GUI/MainWindow'],
      excludes=['_imaging_gif', 'ICCProfile'])