
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFrame


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()
        # self.tabs.resize(300,200)
        self.tabs.resize(200,5)
        
        self.tabs.addTab(self.tab1,"Config")
        self.tabs.addTab(self.tab2,"Microenv")
        self.tabs.addTab(self.tab3,"Cell Types")
        self.tabs.addTab(self.tab4,"User Params")
        # self.tabs.addTab("tab1")

        self.scroll = QtWidgets.QScrollArea()  # might contain centralWidget
        self.params = QtWidgets.QWidget()       # contains collection of Vertical Box
        self.vbox = QtWidgets.QVBoxLayout()

        self.cycle_dropdown = QtWidgets.QComboBox()
        self.cycle_dropdown.addItem("cycle 1")
        self.cycle_dropdown.addItem("cycle 2")
        self.cycle_dropdown.addItem("cycle 3")

        self.vbox.addWidget(self.cycle_dropdown)

        #=====  Phenotype 
        #============  Cycle ================================
        label = QtWidgets.QLabel("Phenotype: cycle")
        self.vbox.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase0->Phase1 transition rate")
        hbox.addWidget(label)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase1->Phase2 transition rate")
        hbox.addWidget(label)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase2->Phase3 transition rate")
        hbox.addWidget(label)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase3->Phase4 transition rate")
        hbox.addWidget(label)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        self.vbox.addWidget(QHLine())
        #--------------------------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase0->Phase0 transition rate")
        hbox.addWidget(label)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        self.vbox.addWidget(QHLine())


        # self.vbox.addLayout(hbox)
        #----------
        #============  Death ================================
        label = QtWidgets.QLabel("Phenotype: death")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())
        #============  Volume ================================
        label = QtWidgets.QLabel("Phenotype: volume")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())
        #============  Mechanics ================================
        label = QtWidgets.QLabel("Phenotype: mechanics")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())
        #============  Motility ================================
        label = QtWidgets.QLabel("Phenotype: motility")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())
        #============  Secretion ================================
        label = QtWidgets.QLabel("Phenotype: secretion")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())
        #============  Molecular ================================
        label = QtWidgets.QLabel("Phenotype: molecular")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())

        #=====  Custom data 
        label = QtWidgets.QLabel("Custom data")
        self.vbox.addWidget(label)
        self.vbox.addWidget(QHLine())

        #==================================================================
        self.params.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.params)


        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(QHLine())
        # self.layout.addWidget(self.params)
        self.layout.addWidget(self.scroll)
        # self.layout.addWidget(self.vbox)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)

        # self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())

