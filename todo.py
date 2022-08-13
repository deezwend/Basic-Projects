from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3 as sql
from tkinter.messagebox import *
from clipboard import copy
from os import listdir

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(811, 480)
        Form.setMinimumSize(QtCore.QSize(811, 480))
        Form.setMaximumSize(QtCore.QSize(811, 480))
        Form.setStyleSheet("QWidget[objectName=\"Form\"]{\n"
"    background: rgb(255, 203, 219);\n"
"}")
        self.partsofprogram = QtWidgets.QTabWidget(Form)
        self.partsofprogram.setGeometry(QtCore.QRect(0, 0, 841, 481))
        self.partsofprogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.partsofprogram.setStyleSheet("QTabWidget::pane{\n"
"border: 1px solid rgb(255, 203, 219);\n"
"background-color:rgb(255, 203, 219);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    background-color: green;\n"
"    border-bottom: 2px solid black;\n"
"    border-bottom-color: black;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    margin-right: 5px;\n"
"    margin-bottom: 3px;\n"
"    color: white;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: blue;\n"
"    color: white;\n"
"    border: none;\n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: black;\n"
"}\n"
"")
        self.partsofprogram.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.partsofprogram.setObjectName("partsofprogram")
        self.tabwCreateNewToDo = QtWidgets.QWidget()
        self.tabwCreateNewToDo.setMinimumSize(QtCore.QSize(939, 0))
        self.tabwCreateNewToDo.setMaximumSize(QtCore.QSize(939, 16777215))
        self.tabwCreateNewToDo.setObjectName("tabwCreateNewToDo")
        self.lblthingtodo = QtWidgets.QLabel(self.tabwCreateNewToDo)
        self.lblthingtodo.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblthingtodo.setFont(font)
        self.lblthingtodo.setStyleSheet("background: 00FFFFFF;\n"
"color: #355C7D;\n"
"")
        self.lblthingtodo.setObjectName("lblthingtodo")
        self.lnetoDoText = QtWidgets.QLineEdit(self.tabwCreateNewToDo)
        self.lnetoDoText.setGeometry(QtCore.QRect(20, 50, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lnetoDoText.setFont(font)
        self.lnetoDoText.setStyleSheet("QLineEdit{\n"
"background-color: white;\n"
"color: red;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  background:#f5f5f5;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.lnetoDoText.setObjectName("lnetoDoText")
        self.lbluntil = QtWidgets.QLabel(self.tabwCreateNewToDo)
        self.lbluntil.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbluntil.setFont(font)
        self.lbluntil.setStyleSheet("background: 00FFFFFF;\n"
"color: #355C7D;")
        self.lbluntil.setObjectName("lbluntil")
        self.clnDate = QtWidgets.QCalendarWidget(self.tabwCreateNewToDo)
        self.clnDate.setGeometry(QtCore.QRect(20, 140, 331, 211))
        self.clnDate.setStyleSheet("QCalendarWidget QWidget\n"
"{\n"
"    alternate-background-color: gray;\n"
"}\n"
"\n"
"QCalendarWidget #qt_calendar_navigationbar{\n"
"    background-color: rgb(255, 203, 219);\n"
"    border: 2px solid blue;\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth,\n"
"#qt_calendar_nextmonth\n"
"{\n"
"    border:none;\n"
"    qproperty-icon: none;\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    \n"
"}\n"
"\n"
"#qt_calendar_prevmonth\n"
"{\n"
"    image: url(:/icons/icons/left-arrow.png);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover\n"
"{\n"
"    background-color: rgb(129, 109, 134);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth\n"
"{\n"
"    image: url(:/icons/icons/right-arrow.png);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:hover\n"
"{\n"
"    background-color: rgb(129, 109, 134);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton\n"
"{\n"
"    color: blue;\n"
"    padding: 0 10px;\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"    font-size:13px;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton\n"
"{\n"
"    width: 100px;\n"
"    color: blue;\n"
"    font-size: 13px;\n"
"    margin: 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover,\n"
"#qt_calendar_monthbutton:hover\n"
"{\n"
"    color: rgb(87, 168, 255);\n"
"}\n"
"")
        self.clnDate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.clnDate.setObjectName("clnDate")
        self.cmbAbout = QtWidgets.QComboBox(self.tabwCreateNewToDo)
        self.cmbAbout.setGeometry(QtCore.QRect(90, 370, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cmbAbout.setFont(font)
        self.cmbAbout.setStyleSheet("QComboBox{\n"
"    border-top-right-radius: 11px;\n"
"    border-bottom-left-radius: 11px;\n"
"    border: 1px solid black;\n"
"    background-color: rgb(255, 203, 219);\n"
"    color: #355C7D;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  background:rgb(191, 152, 165);\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-radius: 15px;\n"
"    image: url(:/icons/icons/down-arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-radius: 15px;\n"
"}")
        self.cmbAbout.setIconSize(QtCore.QSize(22, 22))
        self.cmbAbout.setObjectName("cmbAbout")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/graduation-cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/globe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/shopping-cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/cooking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/coding-language.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/meeting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/working.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/sports.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmbAbout.addItem(icon8, "")
        self.lblabout = QtWidgets.QLabel(self.tabwCreateNewToDo)
        self.lblabout.setGeometry(QtCore.QRect(20, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblabout.setFont(font)
        self.lblabout.setStyleSheet("background: 00FFFFFF;\n"
"color: #355C7D;")
        self.lblabout.setObjectName("lblabout")
        self.lneDetails = QtWidgets.QTextEdit(self.tabwCreateNewToDo)
        self.lneDetails.setGeometry(QtCore.QRect(400, 40, 401, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lneDetails.setFont(font)
        self.lneDetails.setStyleSheet("QTextEdit{\n"
"background-color: white;\n"
"color: red;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  background:#f5f5f5;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.lneDetails.setObjectName("lneDetails")
        self.btnSave = QtWidgets.QPushButton(self.tabwCreateNewToDo)
        self.btnSave.setGeometry(QtCore.QRect(690, 370, 101, 31))
        self.btnSave.setStyleSheet("QPushButton{\n"
"background-color: rgb(129, 109, 134);\n"
"border: 1px solid blue;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"  background-color: rgb(161, 136, 167);\n"
"  text-decoration: none;\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../Desktop/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon9)
        self.btnSave.setIconSize(QtCore.QSize(27, 27))
        self.btnSave.setObjectName("btnSave")
        self.lbldetails = QtWidgets.QLabel(self.tabwCreateNewToDo)
        self.lbldetails.setGeometry(QtCore.QRect(400, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbldetails.setFont(font)
        self.lbldetails.setStyleSheet("background: 00FFFFFF;\n"
"color: #355C7D;")
        self.lbldetails.setObjectName("lbldetails")
        self.partsofprogram.addTab(self.tabwCreateNewToDo, "")
        self.tabwShowToDo = QtWidgets.QWidget()
        self.tabwShowToDo.setStyleSheet("")
        self.tabwShowToDo.setObjectName("tabwShowToDo")
        self.lstwToDos = QtWidgets.QListWidget(self.tabwShowToDo)
        self.lstwToDos.setGeometry(QtCore.QRect(0, 0, 561, 431))
        self.lstwToDos.setStyleSheet("#lstwToDos\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid gray;;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"    color: black;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#lstwToDos::item\n"
"{\n"
"    margin-top: 5.5px;\n"
"    font-family: sans;\n"
"}\n"
"\n"
"\n"
"#lstwToDos::item:hover\n"
"{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(245, 245, 245);\n"
"    color: black;\n"
"}\n"
"\n"
"#lstwToDos::item:selected\n"
"{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(174, 247, 255);\n"
"    color: rgb(102, 0, 153);\n"
"}\n"
"\n"
"#lstwToDos::item:pressed\n"
"{\n"
"    border-radius: 15px;\n"
"    background-color: yellow;\n"
"    color: white;\n"
"}")
        self.lstwToDos.setObjectName("lstwToDos")
        self.rdbtEditAll = QtWidgets.QRadioButton(self.tabwShowToDo)
        self.rdbtEditAll.setGeometry(QtCore.QRect(570, 80, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbtEditAll.setFont(font)
        self.rdbtEditAll.setToolTip("")
        self.rdbtEditAll.setStyleSheet("QRadioButton:hover\n"
"{\n"
"    color: red;\n"
"}\n"
"\n"
"QRadioButton:checked\n"
"{\n"
"    color: red;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    image: url(:/icons/icons/check.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/icons/icons/close.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"    image: url(:/icons/icons/close.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/icons/icons/check.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}")
        self.rdbtEditAll.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.rdbtEditAll.setObjectName("rdbtEditAll")
        self.btnCircleEdit = QtWidgets.QPushButton(self.tabwShowToDo)
        self.btnCircleEdit.setGeometry(QtCore.QRect(570, 150, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnCircleEdit.setFont(font)
        self.btnCircleEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCircleEdit.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(58, 58, 58);\n"
"    border: 3px solid rgb(41, 255, 8);\n"
"    border-radius: 35px;\n"
"    color:red;\n"
"    font: 10pt;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(125, 125, 125);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.btnCircleEdit.setObjectName("btnCircleEdit")
        self.rdbtEditOne = QtWidgets.QRadioButton(self.tabwShowToDo)
        self.rdbtEditOne.setGeometry(QtCore.QRect(570, 110, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbtEditOne.setFont(font)
        self.rdbtEditOne.setToolTip("")
        self.rdbtEditOne.setStyleSheet("QRadioButton:hover\n"
"{\n"
"    color: red;\n"
"}\n"
"\n"
"QRadioButton:checked\n"
"{\n"
"    color: red;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    image: url(:/icons/icons/check.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/icons/icons/close.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked\n"
"{\n"
"    image: url(:/icons/icons/close.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover\n"
"{\n"
"    image: url(:/icons/icons/check.png);\n"
"    width: 16px;\n"
"    height: 16px;    \n"
"}")
        self.rdbtEditOne.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.rdbtEditOne.setObjectName("rdbtEditOne")
        self.btnCircleSave = QtWidgets.QPushButton(self.tabwShowToDo)
        self.btnCircleSave.setGeometry(QtCore.QRect(700, 240, 71, 71))
        self.btnCircleSave.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(58, 58, 58);\n"
"    border: 3px solid rgb(41, 255, 8);\n"
"    border-radius: 35px;\n"
"    color:red;\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(125, 125, 125);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.btnCircleSave.setObjectName("btnCircleSave")
        self.btnDelete_ToDo = QtWidgets.QPushButton(self.tabwShowToDo)
        self.btnDelete_ToDo.setGeometry(QtCore.QRect(570, 240, 71, 71))
        self.btnDelete_ToDo.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(58, 58, 58);\n"
"    border: 3px solid rgb(41, 255, 8);\n"
"    border-radius: 35px;\n"
"    color:red;\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(125, 125, 125);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.btnDelete_ToDo.setObjectName("btnDelete_ToDo")
        self.btnCircleEditOthers = QtWidgets.QPushButton(self.tabwShowToDo)
        self.btnCircleEditOthers.setGeometry(QtCore.QRect(700, 150, 71, 71))
        self.btnCircleEditOthers.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(58, 58, 58);\n"
"    border: 3px solid rgb(41, 255, 8);\n"
"    border-radius: 35px;\n"
"    color:red;\n"
"    font: 12pt;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(125, 125, 125);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.btnCircleEditOthers.setObjectName("btnCircleEditOthers")
        self.partsofprogram.addTab(self.tabwShowToDo, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.chboxeditothersThingsToDo = QtWidgets.QCheckBox(self.tab)
        self.chboxeditothersThingsToDo.setGeometry(QtCore.QRect(20, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chboxeditothersThingsToDo.setFont(font)
        self.chboxeditothersThingsToDo.setStyleSheet("QCheckBox::indicator\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox:checked\n"
"{\n"
"    border: none;\n"
"    color: blue;\n"
"}")
        self.chboxeditothersThingsToDo.setObjectName("chboxeditothersThingsToDo")
        self.chboxeditothersDetails = QtWidgets.QCheckBox(self.tab)
        self.chboxeditothersDetails.setGeometry(QtCore.QRect(20, 60, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chboxeditothersDetails.setFont(font)
        self.chboxeditothersDetails.setStyleSheet("QCheckBox::indicator\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox:checked\n"
"{\n"
"    border: none;\n"
"    color: blue;\n"
"}")
        self.chboxeditothersDetails.setObjectName("chboxeditothersDetails")
        self.chboxeditothersUntilThatTime = QtWidgets.QCheckBox(self.tab)
        self.chboxeditothersUntilThatTime.setGeometry(QtCore.QRect(20, 250, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chboxeditothersUntilThatTime.setFont(font)
        self.chboxeditothersUntilThatTime.setStyleSheet("QCheckBox::indicator\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox:checked\n"
"{\n"
"    border: none;\n"
"    color: blue;\n"
"}")
        self.chboxeditothersUntilThatTime.setObjectName("chboxeditothersUntilThatTime")
        self.chboxeditothersEditAbout = QtWidgets.QCheckBox(self.tab)
        self.chboxeditothersEditAbout.setGeometry(QtCore.QRect(20, 420, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chboxeditothersEditAbout.setFont(font)
        self.chboxeditothersEditAbout.setStyleSheet("QCheckBox::indicator\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: none;\n"
"    image:url(:/icons/icons/check.png);\n"
"}\n"
"\n"
"QCheckBox:checked\n"
"{\n"
"    border: none;\n"
"    color: blue;\n"
"}")
        self.chboxeditothersEditAbout.setObjectName("chboxeditothersEditAbout")
        self.anothereditothersDetailsBox = QtWidgets.QTextEdit(self.tab)
        self.anothereditothersDetailsBox.setGeometry(QtCore.QRect(130, 60, 261, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.anothereditothersDetailsBox.setFont(font)
        self.anothereditothersDetailsBox.setStyleSheet("QTextEdit{\n"
"background-color: white;\n"
"color: red;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  background:#f5f5f5;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.anothereditothersDetailsBox.setObjectName("anothereditothersDetailsBox")
        self.anothereditotherswhattodo = QtWidgets.QLineEdit(self.tab)
        self.anothereditotherswhattodo.setGeometry(QtCore.QRect(170, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anothereditotherswhattodo.setFont(font)
        self.anothereditotherswhattodo.setStyleSheet("QLineEdit{\n"
"background-color: white;\n"
"color: red;\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  background:#f5f5f5;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border-radius: 0px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}")
        self.anothereditotherswhattodo.setObjectName("anothereditotherswhattodo")
        self.anothereditothersClnWidget = QtWidgets.QCalendarWidget(self.tab)
        self.anothereditothersClnWidget.setGeometry(QtCore.QRect(180, 250, 271, 151))
        self.anothereditothersClnWidget.setStyleSheet("QCalendarWidget QWidget\n"
"{\n"
"    alternate-background-color: gray;\n"
"}\n"
"\n"
"QCalendarWidget #qt_calendar_navigationbar{\n"
"    background-color: rgb(255, 203, 219);\n"
"    border: 2px solid blue;\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"\n"
"}\n"
"\n"
"#qt_calendar_prevmonth,\n"
"#qt_calendar_nextmonth\n"
"{\n"
"    border:none;\n"
"    qproperty-icon: none;\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    \n"
"}\n"
"\n"
"#qt_calendar_prevmonth\n"
"{\n"
"    image: url(:/icons/icons/left-arrow.png);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover\n"
"{\n"
"    background-color: rgb(129, 109, 134);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth\n"
"{\n"
"    image: url(:/icons/icons/right-arrow.png);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth:hover\n"
"{\n"
"    background-color: rgb(129, 109, 134);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton\n"
"{\n"
"    color: blue;\n"
"    padding: 0 10px;\n"
"    border-radius: 5px;\n"
"    margin: 5px;\n"
"    font-size:13px;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton\n"
"{\n"
"    width: 100px;\n"
"    color: blue;\n"
"    font-size: 13px;\n"
"    margin: 5px 0;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover,\n"
"#qt_calendar_monthbutton:hover\n"
"{\n"
"    color: rgb(87, 168, 255);\n"
"}\n"
"")
        self.anothereditothersClnWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.anothereditothersClnWidget.setObjectName("anothereditothersClnWidget")
        self.anothereditothersAboutBox = QtWidgets.QComboBox(self.tab)
        self.anothereditothersAboutBox.setGeometry(QtCore.QRect(140, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.anothereditothersAboutBox.setFont(font)
        self.anothereditothersAboutBox.setStyleSheet("QComboBox{\n"
"    border-top-right-radius: 11px;\n"
"    border-bottom-left-radius: 11px;\n"
"    border: 1px solid black;\n"
"    background-color: rgb(255, 203, 219);\n"
"    color: #355C7D;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"  background:rgb(191, 152, 165);\n"
"}\n"
"\n"
"QComboBox QListView\n"
"{\n"
"    background-color: gray;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    border-radius: 15px;\n"
"    image: url(:/icons/icons/down-arrow.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    border-radius: 15px;\n"
"}")
        self.anothereditothersAboutBox.setIconSize(QtCore.QSize(22, 22))
        self.anothereditothersAboutBox.setObjectName("anothereditothersAboutBox")
        self.anothereditothersAboutBox.addItem(icon, "")
        self.anothereditothersAboutBox.addItem(icon1, "")
        self.anothereditothersAboutBox.addItem(icon2, "")
        self.anothereditothersAboutBox.addItem(icon3, "")
        self.anothereditothersAboutBox.addItem(icon4, "")
        self.anothereditothersAboutBox.addItem(icon5, "")
        self.anothereditothersAboutBox.addItem(icon6, "")
        self.anothereditothersAboutBox.addItem(icon7, "")
        self.anothereditothersAboutBox.addItem(icon8, "")
        self.anothereditothersSave = QtWidgets.QPushButton(self.tab)
        self.anothereditothersSave.setGeometry(QtCore.QRect(640, 330, 151, 41))
        self.anothereditothersSave.setStyleSheet("QPushButton{\n"
"background-color: rgb(129, 109, 134);\n"
"border: 1px solid blue;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"  background-color: rgb(161, 136, 167);\n"
"  text-decoration: none;\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.anothereditothersSave.setIcon(icon9)
        self.anothereditothersSave.setIconSize(QtCore.QSize(27, 27))
        self.anothereditothersSave.setObjectName("anothereditothersSave")
        self.anothereditothersGoBack = QtWidgets.QPushButton(self.tab)
        self.anothereditothersGoBack.setGeometry(QtCore.QRect(640, 400, 151, 41))
        self.anothereditothersGoBack.setStyleSheet("QPushButton{\n"
"background-color: rgb(129, 109, 134);\n"
"border: 1px solid blue;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  \n"
"  background-color: rgb(161, 136, 167);\n"
"  text-decoration: none;\n"
"    border-bottom-right-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.anothereditothersGoBack.setIcon(icon9)
        self.anothereditothersGoBack.setIconSize(QtCore.QSize(27, 27))
        self.anothereditothersGoBack.setObjectName("anothereditothersGoBack")
        self.partsofprogram.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.partsofprogram.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Things to Do"))
        self.lblthingtodo.setText(_translate("Form", "The Thing to Do:"))
        self.lnetoDoText.setWhatsThis(_translate("Form", "<html><head/><body><p>qwe</p></body></html>"))
        self.lbluntil.setText(_translate("Form", "Until That Day:"))
        self.cmbAbout.setItemText(0, _translate("Form", "Education"))
        self.cmbAbout.setItemText(1, _translate("Form", "Travel"))
        self.cmbAbout.setItemText(2, _translate("Form", "Shopping"))
        self.cmbAbout.setItemText(3, _translate("Form", "Video"))
        self.cmbAbout.setItemText(4, _translate("Form", "Cooking"))
        self.cmbAbout.setItemText(5, _translate("Form", "Programming"))
        self.cmbAbout.setItemText(6, _translate("Form", "Meeting"))
        self.cmbAbout.setItemText(7, _translate("Form", "Working"))
        self.cmbAbout.setItemText(8, _translate("Form", "Sport"))
        self.lblabout.setText(_translate("Form", "About:"))
        self.btnSave.setText(_translate("Form", "Save"))
        self.lbldetails.setText(_translate("Form", "Details:"))
        self.partsofprogram.setTabText(self.partsofprogram.indexOf(self.tabwCreateNewToDo), _translate("Form", "Create a new ToDo"))
        self.rdbtEditAll.setText(_translate("Form", "I want to select multiple items"))
        self.btnCircleEdit.setText(_translate("Form", "Edit\n"
"Completed"))
        self.rdbtEditOne.setText(_translate("Form", "I want to select only one item"))
        self.btnCircleSave.setText(_translate("Form", "Save"))
        self.btnDelete_ToDo.setText(_translate("Form", "Delete\n"
"ToDo"))
        self.btnCircleEditOthers.setText(_translate("Form", "Edit\n"
"Others"))
        self.partsofprogram.setTabText(self.partsofprogram.indexOf(self.tabwShowToDo), _translate("Form", "Show ToDos"))
        self.chboxeditothersThingsToDo.setText(_translate("Form", "Edit Things to Do"))
        self.chboxeditothersDetails.setText(_translate("Form", "Edit Details"))
        self.chboxeditothersUntilThatTime.setText(_translate("Form", "Edit Until That Time"))
        self.chboxeditothersEditAbout.setText(_translate("Form", "Edit About"))
        self.anothereditotherswhattodo.setWhatsThis(_translate("Form", "<html><head/><body><p>qwe</p></body></html>"))
        self.anothereditothersAboutBox.setItemText(0, _translate("Form", "Education"))
        self.anothereditothersAboutBox.setItemText(1, _translate("Form", "Travel"))
        self.anothereditothersAboutBox.setItemText(2, _translate("Form", "Shopping"))
        self.anothereditothersAboutBox.setItemText(3, _translate("Form", "Video"))
        self.anothereditothersAboutBox.setItemText(4, _translate("Form", "Cooking"))
        self.anothereditothersAboutBox.setItemText(5, _translate("Form", "Programming"))
        self.anothereditothersAboutBox.setItemText(6, _translate("Form", "Meeting"))
        self.anothereditothersAboutBox.setItemText(7, _translate("Form", "Working"))
        self.anothereditothersAboutBox.setItemText(8, _translate("Form", "Sport"))
        self.anothereditothersSave.setText(_translate("Form", "Save"))
        self.anothereditothersGoBack.setText(_translate("Form", "Go Back"))
        self.partsofprogram.setTabText(self.partsofprogram.indexOf(self.tab), _translate("Form", "Edit Others"))
import iconns_rc


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(628, 359)
        Form2.setMinimumSize(QtCore.QSize(628, 359))
        Form2.setMaximumSize(QtCore.QSize(628, 359))
        Form2.setMouseTracking(True)
        Form2.setWindowTitle("")
        Form2.setStyleSheet("#Form2{\n"
"background-color: black;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: red;\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel:hover\n"
"{\n"
"    color: rgb(35, 255, 11);\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLabel:pressed\n"
"{\n"
"    color: rgb(255, 236, 16);\n"
"    \n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.____todo____ = QtWidgets.QLabel(Form2)
        self.____todo____.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.____todo____.setObjectName("____todo____")
        self.details = QtWidgets.QLabel(Form2)
        self.details.setGeometry(QtCore.QRect(20, 50, 71, 51))
        self.details.setObjectName("details")
        self.untilthattime = QtWidgets.QLabel(Form2)
        self.untilthattime.setGeometry(QtCore.QRect(20, 210, 131, 31))
        self.untilthattime.setObjectName("untilthattime")
        self.completed = QtWidgets.QLabel(Form2)
        self.completed.setGeometry(QtCore.QRect(20, 240, 581, 31))
        self.completed.setObjectName("completed")
        self.labeltodo = QtWidgets.QLabel(Form2)
        self.labeltodo.setGeometry(QtCore.QRect(80, 20, 521, 31))
        self.labeltodo.setText("")
        self.labeltodo.setObjectName("labeltodo")
        self.untilthattime_2 = QtWidgets.QLabel(Form2)
        self.untilthattime_2.setGeometry(QtCore.QRect(160, 210, 451, 31))
        self.untilthattime_2.setText("")
        self.untilthattime_2.setObjectName("untilthattime_2")
        self.completed_2 = QtWidgets.QLabel(Form2)
        self.completed_2.setGeometry(QtCore.QRect(130, 240, 131, 31))
        self.completed_2.setText("")
        self.completed_2.setObjectName("completed_2")
        self.textEdit = QtWidgets.QTextEdit(Form2)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(80, 60, 521, 141))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"background-color:black;\n"
"color: red;\n"
"border: none;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"#textEdit:hover{\n"
"    color:yellow;\n"
"}")
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.about = QtWidgets.QLabel(Form2)
        self.about.setGeometry(QtCore.QRect(20, 270, 71, 31))
        self.about.setObjectName("about")
        self.about_2 = QtWidgets.QLabel(Form2)
        self.about_2.setGeometry(QtCore.QRect(80, 270, 521, 31))
        self.about_2.setText("")
        self.about_2.setObjectName("about_2")
        self.copyDetails = QtWidgets.QPushButton(Form2)
        self.copyDetails.setGeometry(QtCore.QRect(490, 310, 101, 31))
        self.copyDetails.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: rgb(76, 255, 0);\n"
"    color: blue;\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(61, 158, 1);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.copyDetails.setObjectName("copyDetails")

        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        self.____todo____.setText(_translate("Form2", "To Do:"))
        self.details.setText(_translate("Form2", "Details:"))
        self.untilthattime.setText(_translate("Form2", "Until That Time:"))
        self.completed.setText(_translate("Form2", "Completed:"))
        self.about.setText(_translate("Form2", "About:"))
        self.copyDetails.setText(_translate("Form2", "Copy Details"))

sqlconnect = sql.connect("todo.db")
cursor = sqlconnect.cursor()
commit = sqlconnect.commit
sqlconnect.execute("""
CREATE TABLE IF NOT EXISTS todo(
    todoid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    about TEXT NOT NULL,
    whattodo TEXT NOT NULL,
    details TEXT NOT NULL,
    untilthattime TEXT NOT NULL,
    completed TEXT NOT NULL
)""")
__whattodo__ = cursor.execute("SELECT whattodo FROM todo").fetchall
class ToDo(QtWidgets.QWidget):
    def __init__(self) :
        super().__init__()
        try:
            self.ui = Ui_Form()
            global ui
            ui = self.ui
            ui.setupUi(self)
            self.ui2 = Ui_Form2()
            self.window2 = QtWidgets.QWidget()
            self.ui2.setupUi(self.window2)
            self.show()
            ui.btnSave.clicked.connect(self.save)
            self.listselecteditems = ui.lstwToDos.selectedItems
            self.todotext = ui.lnetoDoText.text
            self.detailstext = ui.lneDetails.toPlainText
            ui.lneDetails.textChanged.connect(self.controller)
            self.window2.setWindowTitle(" ")
            self.ui.partsofprogram.setTabVisible(2, False)
            self.ui.anothereditothersAboutBox.setVisible(False)
            self.ui.anothereditothersClnWidget.setVisible(False)
            self.ui.anothereditothersDetailsBox.setVisible(False)
            self.ui.anothereditotherswhattodo.setVisible(False)
            self.langlist = ["Python","C++","C#","HTML","Java","JavaScript","CSS","Lua","Ruby","node.js","PHP"]
            with open("countries.txt","r",encoding="utf-8") as f:
                self.countrieslist = "".join(f.readlines()).split("\n")
            self.educationlist = ["University","High School","Middle School","School", "Math","Chemistry","Physics"]
            self.videolist = ["YouTube","Video"]
            self.listplans()
            ui.lstwToDos.itemDoubleClicked.connect(self.openplanninginfs)
            ui.lstwToDos.itemClicked.connect(self.additems)
            ui.btnCircleSave.clicked.connect(self.savecurs)
            ui.btnCircleEdit.clicked.connect(self.editselecteds)
            ui.btnDelete_ToDo.clicked.connect(self.deleteselected)
            ui.btnCircleEditOthers.clicked.connect(self.editothers)
            ui.anothereditothersGoBack.clicked.connect(self.goback)
            ui.chboxeditothersEditAbout.toggled.connect(ui.anothereditothersAboutBox.setVisible) 
            ui.chboxeditothersUntilThatTime.toggled.connect(ui.anothereditothersClnWidget.setVisible)
            ui.chboxeditothersDetails.toggled.connect(ui.anothereditothersDetailsBox.setVisible)
            ui.chboxeditothersThingsToDo.toggled.connect(ui.anothereditotherswhattodo.setVisible)
            self.ui2.copyDetails.clicked.connect(self.copydetails)
            ui.anothereditothersSave.clicked.connect(self.SaveTheOnesToEdit)
        except sql.OperationalError:
            pass
        
        
    def listplans(self):
        __whattodo__ = cursor.execute("SELECT whattodo FROM todo").fetchall()
        self.ui.lstwToDos.clear()
        for i in __whattodo__:
            ui.lstwToDos.addItem(str(i[0]))
        
    def save(self):
        if (self.todotext() == "" or self.detailstext() == ""):
            showerror(message="Nothing is specified.")
        else:
            self.todotext2 = ui.lnetoDoText.text().replace('"',"").replace("'","").title()
            self.detailstext2 = ui.lneDetails.toPlainText().replace('"',"").replace("'","")
            # sqlconnect.execute(create_table)
            sqlconnect.execute("INSERT INTO todo (about, whattodo, details, untilthattime, completed) VALUES (?,?,?,?,?)", (ui.cmbAbout.currentText(),self.todotext2, self.detailstext2, str(ui.clnDate.selectedDate().toString()), "Not Completed"))
            newitemid = cursor.execute(f"SELECT todoid FROM todo WHERE details='{str(self.detailstext2)}'").fetchone()[0]
            commit()
            __whattodo__ = cursor.execute("SELECT whattodo FROM todo").fetchall()
            self.ui.lstwToDos.clear()
            for i in __whattodo__:
                ui.lstwToDos.addItem(str(i[0]))
            showinfo(message="Your plan was saved!")
            return newitemid
        
    def controller(self):
        if any((i.lower() in self.detailstext() for i in self.langlist)) or any((i.upper() in self.detailstext() for i in self.langlist)) or any((i.capitalize() in self.detailstext() for i in self.langlist)):
            ui.cmbAbout.setCurrentIndex(5)
        if any((i.lower() in self.detailstext() for i in self.countrieslist)) or any((i.upper() in self.detailstext() for i in self.countrieslist)) or any((i.capitalize() in self.detailstext() for i in self.countrieslist)) or any((i.title() in self.detailstext() for i in self.countrieslist)):
            ui.cmbAbout.setCurrentIndex(1)
        if any((i.lower() in self.detailstext() for i in self.educationlist)) or any((i.upper() in self.detailstext() for i in self.educationlist)) or any((i.capitalize() in self.detailstext() for i in self.educationlist)):
            ui.cmbAbout.setCurrentIndex(0)
        if any((i.lower() in self.detailstext() for i in self.videolist)) or any((i.upper() in self.detailstext() for i in self.videolist)) or any((i.capitalize() in self.detailstext() for i in self.videolist)):
            ui.cmbAbout.setCurrentIndex(3)
    
    def openplanninginfs(self):
        if len(self.listselecteditems()) > 1:
            showerror(message="You cannot open more than 1 selected item information.")
            return None
        else:
            self.selecteditemname = ui.lstwToDos.currentItem().text()
            try:
                self.whattodoplan = cursor.execute(rf"SELECT whattodo FROM todo WHERE whattodo='{self.selecteditemname}'").fetchone()[0]
            except:
                showerror(message="An unknown error has occurred. You need to restart the program by saving the edited informations.")
                return None
            self.details = cursor.execute(rf"SELECT details FROM todo WHERE whattodo='{self.selecteditemname}'").fetchone()[0]
            self.untilthattime = cursor.execute(rf"SELECT untilthattime FROM todo WHERE whattodo='{self.selecteditemname}'").fetchone()[0]
            self.completed__ = cursor.execute(rf"SELECT completed FROM todo WHERE whattodo='{self.selecteditemname}'").fetchone()[0]
            self.about = cursor.execute(rf"SELECT about FROM todo WHERE whattodo='{self.selecteditemname}'").fetchone()[0]
            self.window2.show()
            self.ui2.labeltodo.setText(self.whattodoplan)
            self.ui2.textEdit.setPlainText(self.details)
            self.ui2.untilthattime_2.setText(self.untilthattime)
            self.ui2.completed_2.setText(self.completed__)
            self.ui2.about_2.setText(self.about)
            
    def copydetails(self):
        try:
            copy(str(self.ui2.textEdit.toPlainText()))
            showinfo(message="The details have been copied!")
        except:
            showerror(message="The details couldn't be copied.")
            return None
   
    def editselecteds(self):
        warnuser = False
        if self.ui.rdbtEditAll.isChecked():
            if bool(ui.lstwToDos.selectedItems()) == False: 
                showerror(message="You did not select any plans from the list.")
                return None
            else:
                try:
                    print(self.__planlist__)
                    for i in self.__planlist__:
                        self.statuscompleted = cursor.execute(fr"SELECT completed FROM todo WHERE whattodo='{self.ui.lstwToDos.item(i).text()}'").fetchone()[0]
                        if self.statuscompleted == "Not Completed":
                            cursor.execute(fr"UPDATE todo SET completed='Completed' WHERE whattodo='{self.ui.lstwToDos.item(i).text()}'")
                        elif self.statuscompleted == "Completed":
                            if not warnuser:
                                warnuser = True
                                showwarning(message="Status of completed of selected plans will be updated from Completed to Not Completed.")
                            cursor.execute(fr"UPDATE todo SET completed='Not Completed' WHERE whattodo='{self.ui.lstwToDos.item(i).text()}'")
                    
                    
                    showinfo(message="Statuses of completeds of selected plans have been updated!")
                except Exception as e:
                    showerror(message="Statuses of completeds of selected plans couldn't be updated.")
        #----------------------------------------------------------------------------------------------------
        elif self.ui.rdbtEditOne.isChecked():
            if bool(ui.lstwToDos.currentItem()) == False:
                showerror(message="You did not select any plan from the list.")
                return None
            else:
                try:
                    if cursor.execute(fr"SELECT completed FROM todo WHERE whattodo='{self.ui.lstwToDos.currentItem().text()}'").fetchone()[0] == "Not Completed":
                            cursor.execute(fr"UPDATE todo SET completed='Completed' WHERE whattodo='{self.ui.lstwToDos.currentItem().text()}'")
                    else:
                        if not warnuser:
                            warnuser = True
                            showwarning(message="Status of completed of selected items will be updated from Completed to Not Completed.")
                            cursor.execute(fr"UPDATE todo SET completed='Not Completed' WHERE whattodo='{self.ui.lstwToDos.currentItem().text()}'")
                    showinfo(message="Status of completed of selected item has been updated!")
                except Exception as e:
                    showerror(message="Status of completed of selected item couldn't be updated.")
        else:
            showerror(message="You did not select any options above.")
        
    def savecurs(self):
        try:
            commit()
            ui.lstwToDos.clear()
            self.listplans()
            showinfo(message="All of Changes you've done have been saved!")
        except:
            showerror(message="Changes couldn't be saved.")
        
    def additems(self):
        if self.ui.rdbtEditAll.isChecked():
            self.ui.lstwToDos.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.__planlist__ = []
            for i in range(len(self.listselecteditems())):
                self.__planlist__.append(self.ui.lstwToDos.selectedIndexes()[i].row())
                self.__planlist__.sort(reverse=False)
        elif self.ui.rdbtEditOne.isChecked():
            self.ui.lstwToDos.setSelectionMode(QAbstractItemView.SingleSelection)
            self.planstr = self.ui.lstwToDos.currentItem().text()
        
    def deleteselected(self):
        if ui.rdbtEditAll.isChecked():
            if bool(ui.lstwToDos.selectedItems())  == False:
                showerror(message="You did not select any plans from the list.")
                return None
            else:
                ask = askyesno(message="You sure you want to delete the selected plans?")
                if ask:
                    try:
                        for i in self.__planlist__:
                            cursor.execute(fr"DELETE FROM todo WHERE whattodo='{ui.lstwToDos.item(i).text()}'")
                        self.listplans()
                        showinfo(message="The plans you selected have been deleted!")
                    except Exception as e:
                        showerror(message="The plans you selected couldn't be deleted.")
                        print(e)
                        return None
                #---------------------------------------------------------------------------------------------------
        elif ui.rdbtEditOne.isChecked():
            if bool(ui.lstwToDos.currentItem())  == False:
                showerror(message="You did not select any plan from the list.")
                return None
            else:
                ask = askyesno(message="You sure you want to delete the selected plan?")
                if ask:
                    try:
                        cursor.execute(fr"DELETE FROM todo WHERE whattodo='{ui.lstwToDos.currentItem().text()}'")
                        self.listplans()
                        showinfo(message="The plan you selected has been deleted!")
                    except Exception as e:
                        showerror(message="The plan you selected couldn't be deleted.")
                        print(e)
                        return None
        else:
            showerror(message="You did not select any options above.")
                    
    def editothers(self):
        if bool(ui.lstwToDos.currentItem()) == False:
            showerror(message="Please select a plan to edit from the list.")
            return None
        else:
            
            if ui.rdbtEditAll.isChecked():
                ui.rdbtEditAll.setChecked(False)
                ui.rdbtEditOne.setChecked(True)    
                showwarning(message="You can edit only 1 plan from the list.\n\nThat's why 'I want to edit select only one plan has been selected.'")
                ui.lstwToDos.setCurrentItem(None)
            elif ui.rdbtEditOne.isChecked():
                self.theaplantoedit = ui.lstwToDos.currentItem().text()
                self.ui.partsofprogram.setTabVisible(0, False)
                self.ui.partsofprogram.setTabVisible(1, False)
                self.ui.partsofprogram.setTabVisible(2, True)
            else:
                showerror(message="You did not select any options above.")
                return None
     
    def visiblesettings(self):
        self.ui.partsofprogram.setTabVisible(0, True)
        self.ui.partsofprogram.setTabVisible(1, True)
        self.ui.partsofprogram.setTabVisible(2, False)
        self.ui.partsofprogram.setCurrentIndex(1)
        ui.anothereditothersAboutBox.setVisible(False)
        ui.anothereditothersClnWidget.setVisible(False)
        ui.anothereditothersDetailsBox.setVisible(False)
        ui.anothereditotherswhattodo.setVisible(False)           
        ui.chboxeditothersDetails.setChecked(False)
        ui.chboxeditothersEditAbout.setChecked(False) 
        ui.chboxeditothersThingsToDo.setChecked(False) 
        ui.chboxeditothersUntilThatTime.setChecked(False)
        ui.anothereditothersDetailsBox.setPlainText(None)
        ui.anothereditotherswhattodo.setText(None)
        ui.anothereditothersAboutBox.setCurrentIndex(0)
         
    def goback(self):
        if "todo.db-journal" not in listdir():
            ask = askyesno(message="You sure you wanna go back to the other pages without any changing?")    
            if ask:
                self.visiblesettings()
        else:
            self.visiblesettings()
            
        return 0

    def SaveTheOnesToEdit(self):
        self.onestoedit = {}
        if ui.chboxeditothersDetails.isChecked():
            if ui.anothereditothersDetailsBox.toPlainText() == "":
                pass
            else:
                self.onestoedit["details"] = ui.anothereditothersDetailsBox.toPlainText().replace("'","").replace('"',"")
        
        if ui.chboxeditothersUntilThatTime.isChecked():
            if str(ui.clnDate.selectedDate().toString()) == "":
                pass
            else:
                self.onestoedit["untilthattime"] = str(ui.anothereditothersClnWidget.selectedDate().toString()).replace("'","").replace('"',"")
                print(self.onestoedit['untilthattime'])
        if ui.chboxeditothersEditAbout.isChecked():
            if ui.anothereditothersAboutBox.currentText() == "":
                pass
            else:
                self.onestoedit["about"] = ui.anothereditothersAboutBox.currentText().replace("'","").replace('"',"")
                
        if ui.chboxeditothersThingsToDo.isChecked():
            if ui.anothereditotherswhattodo.text() == "":
                pass
            else:
                self.onestoedit["whattodo"] = ui.anothereditotherswhattodo.text().replace("'","").replace('"',"")
        dictkeylist = list(self.onestoedit.keys())
        dictvaluelist = list(self.onestoedit.values())
        
        if self.onestoedit:
            try:
                for k, v in zip(dictkeylist, dictvaluelist):
                    cursor.execute(fr"UPDATE todo SET {k}='{v}' WHERE whattodo='{self.theaplantoedit}'")
                showinfo(message="Successful! All of the options you selected have been changed!")
                ui.lstwToDos.clear()
                self.listplans()
                self.visiblesettings()
                return 0
            except Exception as e:
                print(e)
        else:
            showerror(message="You did not specify any change.")
            return 0



if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = ToDo()
    exit(app.exec_())
    
"""TODO
    //1. 2.bir arayüz oluşturulacak//                                                                             XXX
    //2. 2.arayüzün CSS'i ayarlanacak//                                                                           XXX
    //3. tamamlandı kısmını güncelleme ayarlanacak//                                                              XXX
    //4. Programa giriş yapıldığında önceden eklenen bütün şeylere erişim sağlamayı sağlayan bir arayüz çıkacak// XXX
    //5.ayarlanan plandan istenen kısım güncellenebilecek//                                                       XXX
    
"""