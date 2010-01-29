# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decode_dialog.ui'
#
# Created: Fri Jan 29 19:36:08 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DecodeDialog(object):
    def setupUi(self, DecodeDialog):
        DecodeDialog.setObjectName("DecodeDialog")
        DecodeDialog.resize(385, 234)
        DecodeDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayoutWidget = QtGui.QWidget(DecodeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 233))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.decode_view_text_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.decode_view_text_button.setMinimumSize(QtCore.QSize(121, 23))
        self.decode_view_text_button.setObjectName("decode_view_text_button")
        self.horizontalLayout.addWidget(self.decode_view_text_button)
        self.decode_done_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.decode_done_button.setMinimumSize(QtCore.QSize(121, 23))
        self.decode_done_button.setObjectName("decode_done_button")
        self.horizontalLayout.addWidget(self.decode_done_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DecodeDialog)
        QtCore.QObject.connect(self.decode_done_button, QtCore.SIGNAL("clicked()"), DecodeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(DecodeDialog)

    def retranslateUi(self, DecodeDialog):
        DecodeDialog.setWindowTitle(QtGui.QApplication.translate("DecodeDialog", "Decode Success!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DecodeDialog", "This is default text.  If you see this, something is wrong", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_view_text_button.setText(QtGui.QApplication.translate("DecodeDialog", "View Text File", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_done_button.setText(QtGui.QApplication.translate("DecodeDialog", "Done", None, QtGui.QApplication.UnicodeUTF8))

