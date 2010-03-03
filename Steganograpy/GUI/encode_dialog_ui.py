# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encode_dialog.ui'
#
# Created: Fri Jan 29 19:46:26 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EncodeDialog(object):
    def setupUi(self, EncodeDialog):
        EncodeDialog.setObjectName("EncodeDialog")
        EncodeDialog.resize(385, 234)
        self.verticalLayoutWidget = QtGui.QWidget(EncodeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 381, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encoded_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.encoded_label.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.encoded_label.setFont(font)
        self.encoded_label.setAlignment(QtCore.Qt.AlignCenter)
        self.encoded_label.setWordWrap(True)
        self.encoded_label.setObjectName("encoded_label")
        self.verticalLayout.addWidget(self.encoded_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.view_image_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.view_image_button.setObjectName("view_image_button")
        self.horizontalLayout.addWidget(self.view_image_button)
        self.side_by_side_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.side_by_side_button.setObjectName("side_by_side_button")
        self.horizontalLayout.addWidget(self.side_by_side_button)
        self.done_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.done_button.setObjectName("done_button")
        self.horizontalLayout.addWidget(self.done_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(EncodeDialog)
        QtCore.QObject.connect(self.done_button, QtCore.SIGNAL("clicked()"), EncodeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(EncodeDialog)

    def retranslateUi(self, EncodeDialog):
        EncodeDialog.setWindowTitle(QtGui.QApplication.translate("EncodeDialog", "Encode Success!", None, QtGui.QApplication.UnicodeUTF8))
        self.encoded_label.setText(QtGui.QApplication.translate("EncodeDialog", "This is default text.  If you see this, there is something wrong.", None, QtGui.QApplication.UnicodeUTF8))
        self.view_image_button.setToolTip(QtGui.QApplication.translate("EncodeDialog", "View the newly encoded image.", None, QtGui.QApplication.UnicodeUTF8))
        self.view_image_button.setText(QtGui.QApplication.translate("EncodeDialog", "View Image", None, QtGui.QApplication.UnicodeUTF8))
        self.side_by_side_button.setToolTip(QtGui.QApplication.translate("EncodeDialog", "View the original image and the newly encoded image side by side.", None, QtGui.QApplication.UnicodeUTF8))
        self.side_by_side_button.setText(QtGui.QApplication.translate("EncodeDialog", "View side by side", None, QtGui.QApplication.UnicodeUTF8))
        self.done_button.setText(QtGui.QApplication.translate("EncodeDialog", "Done", None, QtGui.QApplication.UnicodeUTF8))

