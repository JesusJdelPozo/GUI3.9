from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self, name: str):
        super(MyWindow, self).__init__()
        self.initUI(name)

    def initUI(self, name: str):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle(name)
        self.label = QtWidgets.QLabel(self)
        self.label.setText('This label says things')
        self.label.move(50, 50)

        self.label = QtWidgets.QLabel(self)
        self.label.setText('This label says  other things')
        self.label.move(50, 200)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText('push the button to change the label1')
        self.button.adjustSize()
        self.button.clicked.connect(lambda :self.click('boton1'))

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.move(300, 0)
        self.button2.setText('push the button to change the label2')
        self.button2.adjustSize()
        self.button2.clicked.connect(lambda : self.click('boton2'))

    def click(self, text: str):
        self.label.setText(text)
        self.update()

    def update(self):
        self.label.adjustSize()



def window(name: str):
    # Creates a window with a given name
    app = QApplication(sys.argv)
    win = MyWindow(name)
    win.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    window('PyCharm window')