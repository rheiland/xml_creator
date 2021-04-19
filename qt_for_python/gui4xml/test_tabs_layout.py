import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
	
    def initUI(self):
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout()
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        self.tab_widget = QTabWidget()
        self.cycle_tab = QWidget()
        self.death_tab = QWidget()
        self.tab_widget.addTab(self.cycle_tab,"Cycle")
        self.tab_widget.addTab(self.death_tab,"Death")

        splitter1 = QSplitter()
        textedit = QTextEdit()

        # lay = QVBoxLayout(self)
        # lay.setContentsMargins(5, 35, 5, 5)

        splitter1.addWidget(topleft)
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100,200])

        vbox.addWidget(self.tab_widget)
        vbox.addWidget(splitter1)

        self.setLayout(vbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Test Tabs QSplitter widget groups')
        self.show()
		
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()
