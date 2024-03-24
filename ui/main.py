from ._ui_main import Ui_MainWindow
from modules import config
from modules.create_link import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton, QDialogButtonBox, QLineEdit, QInputDialog, QFileDialog
from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal, QPoint
from PyQt5 import QtGui, QtCore
import subprocess
import sys, os

class CommandThread(QThread):
    output = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command
        self.should_run = True

    def run(self):
        if os.name == "nt":
            encode = "cp866"
        else:
            encode = "utf-8"
        process = subprocess.Popen(
            self.command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding=encode
        )

        for line in process.stdout: # type: ignore
            if not self.should_run:
                break
            self.output.emit(line.strip())
        self.output.emit("Команда завершила работу")

    def stop(self):
        self.should_run = False

class Main(Ui_MainWindow):

    def _load_buttons(self):

        def button_clicked(command):
            return lambda: self.execute_command(command)

        for i in range(20):
            cmd = config.read(i + 1)
            if cmd.command:
                self.buttons[i].setText(cmd.command_name)
                self.buttons[i].clicked.connect(button_clicked(cmd.command))
            else:
                self.buttons[i].deleteLater()

    def __init__(self, MainWindow: QMainWindow, Application: QApplication):
        super().__init__(MainWindow)
        
        self.MainWindow = MainWindow
        self.Application = Application
        self.buttons = [
            self.btn_command_1,
            self.btn_command_2,
            self.btn_command_3,
            self.btn_command_4,
            self.btn_command_5,
            self.btn_command_6,
            self.btn_command_7,
            self.btn_command_8,
            self.btn_command_9,
            self.btn_command_10,
            self.btn_command_11,
            self.btn_command_12,
            self.btn_command_13,
            self.btn_command_14,
            self.btn_command_15,
            self.btn_command_16,
            self.btn_command_17,
            self.btn_command_18,
            self.btn_command_19,
            self.btn_command_20,
        ]
        self._load_buttons()
        ########################
        self.btn_open_config.clicked.connect(self.open_config)
        self.btn_create_link.clicked.connect(self.create_link)

    def open_config(self):
        file_path = config.CONFIG_FILE
        if sys.platform.startswith('darwin'):  # macOS
            command = ['open', '-t', file_path]
        elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):  # Windows
            command = ['cmd', '/c' 'start', 'notepad.exe', file_path]
        elif sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):  # Linux/Unix
            command = ['xdg-open', file_path]
        else:
            self.console_widget.append("Открытие файла не поддерживается на данной операционной системе.")
            return

        subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def execute_command(self, command: str):
        cmd = command.split()
        self.command_thread = CommandThread(cmd)
        self.command_thread.output.connect(self.console_widget.append)
        self.command_thread.start()
    
    def create_link(self):
        cmd = self.lineEdit.text()
        icon_link = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        add_to_menu = self.radioButton.isChecked()
        add_to_desktop = self.radioButton_2.isChecked()
        create_desktop_file(name, icon_link, cmd, add_to_desktop, add_to_menu)
        

    def closeEvent(self, event):
        self.command_thread.stop()
        self.command_thread.wait()
        event.accept()
        
