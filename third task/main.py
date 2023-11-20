import sys

from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('')

        self.bt = QPushButton('Создать', self)
        self.bt.move(30, 30)
        self.bt.resize(100, 70)

        self.bt.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
        k = randrange(500)
        qp.drawEllipse(300 - k // 2, 300 - k // 2, k, k)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())