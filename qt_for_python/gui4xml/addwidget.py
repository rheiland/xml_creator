#from PyQt4 import QtGui, QtCore
from PySide6 import QtGui, QtCore, QtWidgets
import sys

# class Main(QtGui.QMainWindow):
class Main(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__()
        self.GUI()


    def GUI(self):

        self.count = 0

        # main button
        # self.addButton = QtGui.QPushButton('button to add other widgets')
        self.addButton = QtWidgets.QPushButton('button to add other widgets')
        self.addButton.clicked.connect(self.addWidget)

        # scroll area widget contents - layout
        self.scrollLayout = QtWidgets.QFormLayout()

        # scroll area widget contents
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        # scroll area
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        # main layout
        self.mainLayout = QtWidgets.QVBoxLayout()

        # add all main to the main vLayout
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.scrollArea)

        # central widget
        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # set central widget
        self.setCentralWidget(self.centralWidget)

    def addWidget(self):
        self.scrollLayout.addRow(Test(self))
        self.count = self.count + 1
        print(self.count)


# class Test(QtGui.QWidget):
class Test(QtWidgets.QWidget):

    def __init__( self, main):
        super(Test, self).__init__()
        self.Main = main
        self.setup()


    def setup(self):

        print(self.Main.count)

        name = "pushButton_"+str(self.Main.count)
        print(name)

        self.name = QtWidgets.QPushButton('I am in Test widget '+str(self.Main.count))


        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.name)
        self.setLayout(layout)


# app = QtGui.QApplication(sys.argv)
app = QtWidgets.QApplication(sys.argv)
myWidget = Main()
myWidget.show()
app.exec_()

# def main():
#     app = QApplication(sys.argv)
#     ex = PhysiCellXMLCreator()
#     ex.setGeometry(100,100, 800,600)
#     ex.show()
#     sys.exit(app.exec_())
	
# if __name__ == '__main__':
#     main()