# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-screen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName(_fromUtf8("frmMain"))
        frmMain.resize(828, 590)
        frmMain.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(frmMain)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblResultingQuery = QtGui.QLabel(frmMain)
        self.lblResultingQuery.setObjectName(_fromUtf8("lblResultingQuery"))
        self.gridLayout.addWidget(self.lblResultingQuery, 6, 0, 1, 3)
        self.lneCharToReplace = QtGui.QLineEdit(frmMain)
        self.lneCharToReplace.setObjectName(_fromUtf8("lneCharToReplace"))
        self.gridLayout.addWidget(self.lneCharToReplace, 4, 2, 1, 1)
        self.txtSQLToChange = QtGui.QTextEdit(frmMain)
        self.txtSQLToChange.setObjectName(_fromUtf8("txtSQLToChange"))
        self.gridLayout.addWidget(self.txtSQLToChange, 1, 0, 1, 7)
        self.txtResultingQuery = QtGui.QTextEdit(frmMain)
        self.txtResultingQuery.setObjectName(_fromUtf8("txtResultingQuery"))
        self.gridLayout.addWidget(self.txtResultingQuery, 7, 0, 1, 7)
        self.btnBrowse = QtGui.QPushButton(frmMain)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 3, 5, 1, 2)
        self.lblEnterSQL = QtGui.QLabel(frmMain)
        self.lblEnterSQL.setObjectName(_fromUtf8("lblEnterSQL"))
        self.gridLayout.addWidget(self.lblEnterSQL, 0, 0, 1, 3)
        self.lblCharReplaceWith = QtGui.QLabel(frmMain)
        self.lblCharReplaceWith.setObjectName(_fromUtf8("lblCharReplaceWith"))
        self.gridLayout.addWidget(self.lblCharReplaceWith, 4, 3, 1, 1)
        self.lneCharReplaceWith = QtGui.QLineEdit(frmMain)
        self.lneCharReplaceWith.setObjectName(_fromUtf8("lneCharReplaceWith"))
        self.gridLayout.addWidget(self.lneCharReplaceWith, 4, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(807, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 7)
        self.lblCharToReplace = QtGui.QLabel(frmMain)
        self.lblCharToReplace.setObjectName(_fromUtf8("lblCharToReplace"))
        self.gridLayout.addWidget(self.lblCharToReplace, 4, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(807, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 7)
        self.btnConvert = QtGui.QPushButton(frmMain)
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))
        self.gridLayout.addWidget(self.btnConvert, 4, 5, 1, 2)
        self.lblSelectBaseTables = QtGui.QLabel(frmMain)
        self.lblSelectBaseTables.setObjectName(_fromUtf8("lblSelectBaseTables"))
        self.gridLayout.addWidget(self.lblSelectBaseTables, 3, 0, 1, 1)
        self.lneBaseTables = QtGui.QLineEdit(frmMain)
        self.lneBaseTables.setObjectName(_fromUtf8("lneBaseTables"))
        self.gridLayout.addWidget(self.lneBaseTables, 3, 1, 1, 4)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)
        frmMain.setTabOrder(self.txtSQLToChange, self.lneBaseTables)
        frmMain.setTabOrder(self.lneBaseTables, self.btnBrowse)
        frmMain.setTabOrder(self.btnBrowse, self.lneCharToReplace)
        frmMain.setTabOrder(self.lneCharToReplace, self.lneCharReplaceWith)
        frmMain.setTabOrder(self.lneCharReplaceWith, self.btnConvert)
        frmMain.setTabOrder(self.btnConvert, self.txtResultingQuery)

    def retranslateUi(self, frmMain):
        frmMain.setWindowTitle(_translate("frmMain", "SQL Find-n-Replace", None))
        self.lblResultingQuery.setText(_translate("frmMain", "<b>Resulting SQL Query:</b>", None))
        self.btnBrowse.setText(_translate("frmMain", "Browse...", None))
        self.lblEnterSQL.setText(_translate("frmMain", "<b>Enter SQL Query:</b>", None))
        self.lblCharReplaceWith.setText(_translate("frmMain", "<b>Character To Replace With:</b>", None))
        self.lblCharToReplace.setText(_translate("frmMain", "<b>Character To Replace:</b>", None))
        self.btnConvert.setText(_translate("frmMain", "Convert", None))
        self.lblSelectBaseTables.setText(_translate("frmMain", "<b>Load Base Tables:</b>", None))

