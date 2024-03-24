from ui.main import Main
from PyQt5 import QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main(MainWindow, app)
    MainWindow.show()
    sys.exit(app.exec_())
