# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import ui

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Add a new main window
    mainWindow =QMainWindow()
    # call the class from Qt
    ui = ui.Ui_MainWindow()
    # call the method of the class, add widget to the window
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())