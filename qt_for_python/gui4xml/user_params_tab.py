"""
Authors:
Randy Heiland (heiland@iu.edu)
Adam Morrow, Grant Waldrow, Drew Willis, Kim Crevecoeur
Dr. Paul Macklin (macklinp@iu.edu)

--- Versions ---
0.1 - initial version
"""

import sys
from PySide6 import QtCore, QtWidgets, QtGui
#from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import *
from PySide6.QtGui import QDoubleValidator

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

# class NewUserParam(QtWidgets.QWidget):
class NewUserParam(QtWidgets.QHBoxLayout):
    def __init__( self, main):
        super(NewUserParam, self).__init__()
        self.Main = main
        self.setup()

    def setup(self):
        print(self.Main.count)
        name = "pushButton_"+str(self.Main.count)
        print(name)
        self.name = QtWidgets.QPushButton('I am in Test widget '+str(self.Main.count))
        # layout = QtWidgets.QHBoxLayout()
        # layout.addWidget(self.name)
        self.addWidget(self.name)
        # self.setLayout(layout)

class UserParams(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # self.current_param = None
        self.xml_root = None
        self.count = 0

        #---------------
        # self.cell_defs = CellDefInstances()
        self.cell_def_horiz_layout = QtWidgets.QHBoxLayout()

        splitter = QtWidgets.QSplitter()

        #-------------------------------------------
        # self.tab = QtWidgets.QWidget()
        # self.tabs.resize(200,5)
        
        #-------------------------------------------
        label_width = 150
        units_width = 70

        self.scroll = QtWidgets.QScrollArea()
        splitter.addWidget(self.scroll)
        # self.cell_def_horiz_layout.addWidget(self.scroll)

        self.params_user_params = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addStretch(0)

        # self.cell_def_horiz_layout.addWidget(self.)

        #------------------
        hbox = QtWidgets.QHBoxLayout()
        self.new_button = QPushButton("New")
        hbox.addWidget(self.new_button)
        self.new_button.clicked.connect(self.new_cb)

        self.copy_button = QPushButton("Copy")
        hbox.addWidget(self.copy_button)

        self.delete_button = QPushButton("Delete")
        hbox.addWidget(self.delete_button)

        self.vbox.addLayout(hbox)
        self.vbox.addWidget(QHLine())

        #------------------
		# <random_seed type="int" units="dimensionless">0</random_seed> 
		# <cargo_signal_D type="double" units="micron/min^2">1e3</cargo_signal_D>

        hbox = QtWidgets.QHBoxLayout()
        # self.select = QtWidgets.QCheckBox("")
        col1 = QtWidgets.QLabel("Name")
        col1.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(col1)
        col2 = QtWidgets.QLabel("Type")
        col2.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(col2)
        col3 = QtWidgets.QLabel("Value")
        col3.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(col3)
        col4 = QtWidgets.QLabel("Units")
        col4.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(col4)
        # label.setFixedWidth(180)
        self.vbox.addLayout(hbox)

        #------------------
        hbox = QtWidgets.QHBoxLayout()

        self.select = QtWidgets.QCheckBox("")
        hbox.addWidget(self.select)

        self.name = QtWidgets.QLineEdit()
        # self.name.setValidator(QtGui.QDoubleValidator())
        # self.diffusion_coef.enter.connect(self.save_xml)
        hbox.addWidget(self.name)

        self.type = QtWidgets.QLineEdit()
        hbox.addWidget(self.type)

        self.value = QtWidgets.QLineEdit()
        # self.name.setValidator(QtGui.QDoubleValidator())
        # self.diffusion_coef.enter.connect(self.save_xml)
        hbox.addWidget(self.value)

        self.units = QtWidgets.QLineEdit()
        hbox.addWidget(self.units)

        # units = QtWidgets.QLabel("micron^2/min")
        # units.setFixedWidth(units_width)
        # hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #--------------------------
        # Dummy widget for filler??
        # label = QLabel("")
        # label.setFixedHeight(1000)
        # # label.setStyleSheet("background-color: orange")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # self.vbox.addWidget(label)


        #==================================================================
        self.params_user_params.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.params_user_params)

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.scroll)

    @QtCore.Slot()
    def new_cb(self):
        print("---- new_cb()")
        # self.create_user_param()
        # self.scrollLayout.addRow(NewUserParam(self))
        self.vbox.addLayout(NewUserParam(self))
        # self.vbox.addLayout(hbox)
        # self.vbox.addLayout(hbox)
        self.count = self.count + 1
        print(self.count)
    #     # self.text.setText(random.choice(self.hello))
    #     pass

    # def new_cb(self):
    #     print('---- new_cb():')

    def create_user_param(self):
        print("--- create_user_param()")
        hbox = QtWidgets.QHBoxLayout()
        select = QtWidgets.QCheckBox("")
        hbox.addWidget(select)
        name = QtWidgets.QLineEdit()
        hbox.addWidget(name)
        mytype = QtWidgets.QLineEdit()
        hbox.addWidget(mytype)
        value = QtWidgets.QLineEdit()
        hbox.addWidget(value)
        units = QtWidgets.QLineEdit()
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        self.params_user_params.setLayout(self.vbox)
        self.layout.addWidget(self.scroll)

    def fill_gui(self, substrate_name):
        pass

    def fill_xml(self):
        pass
    
    def clear_gui(self):
        pass