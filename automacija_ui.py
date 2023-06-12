# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'automacija.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(899, 500)
        MainWindow.setMinimumSize(QSize(500, 400))
        MainWindow.setMaximumSize(QSize(900, 500))
        MainWindow.setMouseTracking(True)
        icon = QIcon()
        iconThemeName = u"computer"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(727, 225))
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setStyleSheet(u"")
        self.Body.setFrameShape(QFrame.NoFrame)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.Body)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(43, 0))
        self.leftMenu.setMaximumSize(QSize(200, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(25, 25, 25);")
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.aframe = QFrame(self.leftMenu)
        self.aframe.setObjectName(u"aframe")
        self.aframe.setMinimumSize(QSize(200, 225))
        self.aframe.setFrameShape(QFrame.NoFrame)
        self.aframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.aframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_page_2 = QPushButton(self.aframe)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(200, 45))
        self.btn_page_2.setMaximumSize(QSize(200, 45))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.btn_page_2.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.aframe)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(200, 45))
        self.btn_page_3.setMaximumSize(QSize(200, 45))
        self.btn_page_3.setFont(font)
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.btn_page_3.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btn_page_3)

        self.pushButton_4 = QPushButton(self.aframe)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(200, 45))
        self.pushButton_4.setMaximumSize(QSize(200, 45))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.aframe)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(200, 45))
        self.pushButton_5.setMaximumSize(QSize(200, 45))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(25, 25, 25);\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	border-left: 3px solid rgb(25, 25, 25);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	background-color: rgb(18, 18, 18);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_4.addWidget(self.aframe)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.Container = QFrame(self.Body)
        self.Container.setObjectName(u"Container")
        self.Container.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.Container.setFrameShape(QFrame.NoFrame)
        self.Container.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.Container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 43, 691, 431))
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setMidLineWidth(0)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName(u"widget_3")
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 0, 331, 51))

        self.verticalLayout_6.addWidget(self.widget_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_2 = QHBoxLayout(self.page_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.page_6)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.page_3)
        self.widget_2.setObjectName(u"widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 320, 121, 31))
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 320, 91, 31))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(9, 9, 655, 128))

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.miniButton = QPushButton(self.Container)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setGeometry(QRect(610, 0, 30, 30))
        self.miniButton.setMinimumSize(QSize(30, 30))
        self.miniButton.setMaximumSize(QSize(30, 30))
        self.miniButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(21, 21, 21)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8_minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon1)
        self.miniButton.setIconSize(QSize(30, 30))
        self.closeButton = QPushButton(self.Container)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(660, 0, 40, 30))
        self.closeButton.setMinimumSize(QSize(40, 30))
        self.closeButton.setMaximumSize(QSize(40, 30))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8_multiply.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(30, 30))
        self.maxiButton = QPushButton(self.Container)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setGeometry(QRect(640, 0, 30, 30))
        self.maxiButton.setMinimumSize(QSize(30, 30))
        self.maxiButton.setMaximumSize(QSize(30, 30))
        self.maxiButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 31, 31);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(21, 21, 21)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8_separate_document_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon3)
        self.maxiButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.Container)


        self.verticalLayout.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"QStatusBar {\n"
"	background-color: rgb(10, 11, 12);\n"
"}")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura i pritisak", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Klima", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Svjetla", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; font-style:italic; text-decoration: underline; color:#ffffff;\">SMART HOME AUTOMATION</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Temperatura: </span></p><p><span style=\" font-size:14pt;\"><br/></span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Pritisak: </span></p><p><span style=\" color:#ff0000;\"><br/></span></p></body></html>", None))
        self.label_4.setText("")
        self.miniButton.setText(QCoreApplication.translate("MainWindow", u"mini", None))
        self.closeButton.setText("")
        self.maxiButton.setText("")
    # retranslateUi

