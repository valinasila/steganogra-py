# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'side_by_side.ui'
#
# Created: Fri Jan 29 16:30:32 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(715, 549)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_image_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.left_image_label.setMinimumSize(QtCore.QSize(0, 500))
        self.left_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.left_image_label.setObjectName("left_image_label")
        self.horizontalLayout_2.addWidget(self.left_image_label)
        self.right_image_label = QtGui.QLabel(self.verticalLayoutWidget)
        self.right_image_label.setMinimumSize(QtCore.QSize(0, 500))
        self.right_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.right_image_label.setObjectName("right_image_label")
        self.horizontalLayout_2.addWidget(self.right_image_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "View Images", None, QtGui.QApplication.UnicodeUTF8))
        self.left_image_label.setText(QtGui.QApplication.translate("Dialog", "Default Text", None, QtGui.QApplication.UnicodeUTF8))
        self.right_image_label.setText(QtGui.QApplication.translate("Dialog", "Default Text", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

