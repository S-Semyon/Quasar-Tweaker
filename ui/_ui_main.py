from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("* {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QLabel {\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #000;\n"
"    background-color: #022901;\n"
"}\n"
"\n"
"#console_widget {\n"
"    border: 1px solid #000;\n"
"    background-color: #303030;\n"
"}")
        self.main_icon = QtGui.QIcon()
        self.main_icon.addPixmap(QtGui.QPixmap("icons\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) # type: ignore
        MainWindow.setWindowIcon(self.main_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.console_widget = QtWidgets.QTextBrowser(self.centralwidget)
        self.console_widget.setGeometry(QtCore.QRect(10, 301, 781, 291))
        self.console_widget.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.console_widget.setObjectName("console_widget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 140, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 120, 261, 20))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(480, -10, 20, 311))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 170, 261, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(510, 190, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 70, 261, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(510, 90, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(510, 220, 200, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(510, 240, 200, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.btn_create_link = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_link.setGeometry(QtCore.QRect(510, 260, 151, 31))
        self.btn_create_link.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_create_link.setObjectName("btn_create_link")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 20, 191, 31))
        self.label_4.setObjectName("label_4")
        self.btn_command_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_1.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.btn_command_1.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_1.setObjectName("btn_command_1")
        self.btn_command_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_2.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.btn_command_2.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_2.setObjectName("btn_command_2")
        self.btn_command_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_3.setGeometry(QtCore.QRect(10, 90, 151, 31))
        self.btn_command_3.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_3.setObjectName("btn_command_3")
        self.btn_command_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_4.setGeometry(QtCore.QRect(10, 130, 151, 31))
        self.btn_command_4.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_4.setObjectName("btn_command_4")
        self.btn_command_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_5.setGeometry(QtCore.QRect(10, 170, 151, 31))
        self.btn_command_5.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_5.setObjectName("btn_command_5")
        self.btn_command_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_6.setGeometry(QtCore.QRect(10, 210, 151, 31))
        self.btn_command_6.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_6.setObjectName("btn_command_6")
        self.btn_command_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_7.setGeometry(QtCore.QRect(10, 250, 151, 31))
        self.btn_command_7.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_7.setObjectName("btn_command_7")
        self.btn_command_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_8.setGeometry(QtCore.QRect(170, 10, 151, 31))
        self.btn_command_8.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_8.setObjectName("btn_command_8")
        self.btn_command_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_9.setGeometry(QtCore.QRect(170, 50, 151, 31))
        self.btn_command_9.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_9.setObjectName("btn_command_9")
        self.btn_command_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_10.setGeometry(QtCore.QRect(170, 90, 151, 31))
        self.btn_command_10.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_10.setObjectName("btn_command_10")
        self.btn_command_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_11.setGeometry(QtCore.QRect(170, 130, 151, 31))
        self.btn_command_11.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_11.setObjectName("btn_command_11")
        self.btn_command_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_12.setGeometry(QtCore.QRect(170, 170, 151, 31))
        self.btn_command_12.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_12.setObjectName("btn_command_12")
        self.btn_command_13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_13.setGeometry(QtCore.QRect(170, 210, 151, 31))
        self.btn_command_13.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_13.setObjectName("btn_command_13")
        self.btn_command_14 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_14.setGeometry(QtCore.QRect(170, 250, 151, 31))
        self.btn_command_14.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_14.setObjectName("btn_command_14")
        self.btn_command_15 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_15.setGeometry(QtCore.QRect(330, 10, 151, 31))
        self.btn_command_15.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_15.setObjectName("btn_command_15")
        self.btn_command_16 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_16.setGeometry(QtCore.QRect(330, 50, 151, 31))
        self.btn_command_16.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_16.setObjectName("btn_command_16")
        self.btn_open_config = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_config.setGeometry(QtCore.QRect(330, 250, 151, 31))
        self.btn_open_config.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_open_config.setObjectName("btn_open_config")
        self.btn_command_18 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_18.setGeometry(QtCore.QRect(330, 130, 151, 31))
        self.btn_command_18.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_18.setObjectName("btn_command_18")
        self.btn_command_17 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_17.setGeometry(QtCore.QRect(330, 90, 151, 31))
        self.btn_command_17.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_17.setObjectName("btn_command_17")
        self.btn_command_19 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_19.setGeometry(QtCore.QRect(330, 170, 151, 31))
        self.btn_command_19.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_19.setObjectName("btn_command_19")
        self.btn_command_20 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_command_20.setGeometry(QtCore.QRect(330, 210, 151, 31))
        self.btn_command_20.setStyleSheet("QPushButton {\n"
"    font: 10pt \"Ubuntu\";\n"
"    background-color: #0aab45;\n"
"    border: none;\n"
"    color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #046929;\n"
"}")
        self.btn_command_20.setObjectName("btn_command_20")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quasar Tweaker"))
        self.console_widget.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># Console</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Команда выполнения"))
        self.label_2.setText(_translate("MainWindow", "Ссылка на иконку"))
        self.label_3.setText(_translate("MainWindow", "Название"))
        self.radioButton.setText(_translate("MainWindow", "Добавить в меню"))
        self.radioButton_2.setText(_translate("MainWindow", "Добавить на рабочий стол"))
        self.btn_create_link.setText(_translate("MainWindow", "Создать"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Создание ярлыка</span></p></body></html>"))
        self.btn_command_1.setText(_translate("MainWindow", "Команда"))
        self.btn_command_2.setText(_translate("MainWindow", "Команда"))
        self.btn_command_3.setText(_translate("MainWindow", "Команда"))
        self.btn_command_4.setText(_translate("MainWindow", "Команда"))
        self.btn_command_5.setText(_translate("MainWindow", "Команда"))
        self.btn_command_6.setText(_translate("MainWindow", "Команда"))
        self.btn_command_7.setText(_translate("MainWindow", "Команда"))
        self.btn_command_8.setText(_translate("MainWindow", "Команда"))
        self.btn_command_9.setText(_translate("MainWindow", "Команда"))
        self.btn_command_10.setText(_translate("MainWindow", "Команда"))
        self.btn_command_11.setText(_translate("MainWindow", "Команда"))
        self.btn_command_12.setText(_translate("MainWindow", "Команда"))
        self.btn_command_13.setText(_translate("MainWindow", "Команда"))
        self.btn_command_14.setText(_translate("MainWindow", "Команда"))
        self.btn_command_15.setText(_translate("MainWindow", "Команда"))
        self.btn_command_16.setText(_translate("MainWindow", "Команда"))
        self.btn_open_config.setText(_translate("MainWindow", "Открыть config.json"))
        self.btn_command_18.setText(_translate("MainWindow", "Команда"))
        self.btn_command_17.setText(_translate("MainWindow", "Команда"))
        self.btn_command_19.setText(_translate("MainWindow", "Команда"))
        self.btn_command_20.setText(_translate("MainWindow", "Команда"))
