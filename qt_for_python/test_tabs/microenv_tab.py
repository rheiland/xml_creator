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

class SubstrateDef(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # global self.params_cell_def

        # self.cell_defs = CellDefInstances()
        self.cell_def_horiz_layout = QtWidgets.QHBoxLayout()

        splitter = QtWidgets.QSplitter()

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setStyleSheet("background-color: lightgray")
        # self.tree.setColumnCount(1)

        header = QTreeWidgetItem(["---  Substrate or Signal---"])
        self.tree.setHeaderItem(header)

        cellname = QTreeWidgetItem(["virus"])
        self.tree.insertTopLevelItem(0,cellname)

        cellname = QTreeWidgetItem(["interferon"])
        self.tree.insertTopLevelItem(1,cellname)


        self.cell_def_horiz_layout.addWidget(self.tree)

        self.scroll_cell_def_tree = QtWidgets.QScrollArea()
        self.scroll_cell_def_tree.setWidget(self.tree)

        # splitter.addWidget(self.tree)
        splitter.addWidget(self.scroll_cell_def_tree)

        #-------------------------------------------
        # self.tab = QtWidgets.QWidget()
        # self.tabs.resize(200,5)
        
        #-------------------------------------------
        label_width = 150
        units_width = 70

        self.scroll = QtWidgets.QScrollArea()
        splitter.addWidget(self.scroll)
        # self.cell_def_horiz_layout.addWidget(self.scroll)

        self.params_cell_def = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addStretch(0)

        # self.cell_def_horiz_layout.addWidget(self.)

        #------------------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Name of substrate or signal:")
        label.setFixedWidth(180)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cell_type_name = QLineEdit()
        # Want to validate name, e.g., starts with alpha, no special chars, etc.
        # self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cell_type_name)
        self.vbox.addLayout(hbox)

        #------------------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("diffusion coefficient")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.diffusion_coef = QtWidgets.QLineEdit()
        self.diffusion_coef.setValidator(QtGui.QDoubleValidator())
        # self.diffusion_coef.enter.connect(self.save_xml)
        hbox.addWidget(self.diffusion_coef)

        units = QtWidgets.QLabel("micron^2/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("decay rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.decay_rate = QtWidgets.QLineEdit()
        self.decay_rate.setValidator(QtGui.QDoubleValidator())
        # self.decay_rate.enter.connect(self.save_xml)
        hbox.addWidget(self.decay_rate)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("initial condition")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.init_cond = QtWidgets.QLineEdit()
        self.init_cond.setValidator(QtGui.QDoubleValidator())
        # self.init_cond.enter.connect(self.save_xml)
        hbox.addWidget(self.init_cond)

        units = QtWidgets.QLabel("mmol")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Dirichlet BC")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.bdy_cond = QtWidgets.QLineEdit()
        self.bdy_cond.setValidator(QtGui.QDoubleValidator())
        # self.bdy_cond.enter.connect(self.save_xml)
        hbox.addWidget(self.bdy_cond)

        units = QtWidgets.QLabel("mmol")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)

        self.dirichlet_bc_enabled = QtWidgets.QCheckBox("on/off")
        # self.motility_enabled.setAlignment(QtCore.Qt.AlignRight)
        # label.setFixedWidth(label_width)
        hbox.addWidget(self.dirichlet_bc_enabled)

        self.vbox.addLayout(hbox)
        #-------------

        hbox = QtWidgets.QHBoxLayout()
        self.gradients = QtWidgets.QCheckBox("calculate gradients")
        hbox.addWidget(self.gradients)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        self.track_in_agents = QtWidgets.QCheckBox("track in agents")
        hbox.addWidget(self.track_in_agents)
        self.vbox.addLayout(hbox)

        #--------------------------
        # Dummy widget for filler??
        label = QLabel("")
        label.setFixedHeight(300)
        # label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)

        #==================================================================
        self.params_cell_def.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.params_cell_def)


        # self.save_button = QtWidgets.QPushButton("Save")
        # self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)

        # self.layout.addWidget(self.tabs)
        # self.layout.addWidget(QHLine())
        # self.layout.addWidget(self.params)

        # self.layout.addWidget(self.scroll)
        self.layout.addWidget(splitter)

        # self.layout.addWidget(self.vbox)
        # self.layout.addWidget(self.text)

        # self.layout.addWidget(self.save_button)
        # self.save_button.clicked.connect(self.save_xml)


    # @QtCore.Slot()
    # def save_xml(self):
    #     # self.text.setText(random.choice(self.hello))
    #     pass
