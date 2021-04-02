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

class SubstrateDef(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # global self.params_cell_def

        # self.cell_defs = CellDefInstances()
        self.cell_def_horiz_layout = QtWidgets.QHBoxLayout()

        splitter = QtWidgets.QSplitter()

        tree_widget_width = 160

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setStyleSheet("background-color: lightgray")
        self.tree.setFixedWidth(tree_widget_width)
        # self.tree.setColumnCount(1)

        header = QTreeWidgetItem(["---  Substrate ---"])
        self.tree.setHeaderItem(header)

        # cellname = QTreeWidgetItem(["virus"])
        # self.tree.insertTopLevelItem(0,cellname)

        # cellname = QTreeWidgetItem(["interferon"])
        # self.tree.insertTopLevelItem(1,cellname)


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
        self.new_button = QPushButton("New")
        hbox.addWidget(self.new_button)

        self.copy_button = QPushButton("Copy")
        hbox.addWidget(self.copy_button)

        self.delete_button = QPushButton("Delete")
        hbox.addWidget(self.delete_button)

        self.vbox.addLayout(hbox)
        self.vbox.addWidget(QHLine())

        #------------------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Name of substrate:")
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

        self.dirichlet_bc = QtWidgets.QLineEdit()
        self.dirichlet_bc.setValidator(QtGui.QDoubleValidator())
        # self.bdy_cond.enter.connect(self.save_xml)
        hbox.addWidget(self.dirichlet_bc)

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
        label.setFixedHeight(1000)
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

    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            self.tree.clear()
            idx = 0
            for var in uep.findall('variable'):
                vp.append(var)
                # print(var.attrib['name'])
                name = var.attrib['name']
                substrate_name = QTreeWidgetItem([name])
                self.tree.insertTopLevelItem(idx,substrate_name)
                idx += 1


        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point

        self.cell_type_name.setText(var.attrib['name'])
        self.diffusion_coef.setText(vp[0].find('.//diffusion_coefficient').text)
        self.decay_rate.setText(vp[0].find('.//decay_rate').text)
        self.init_cond.setText(vp[0].find('.//initial_condition').text)
        self.dirichlet_bc.setText(vp[0].find('.//Dirichlet_boundary_condition').text)

        # self.chemical_A_decay_rate.value = float(vp[0].find('.//decay_rate').text)
        # self.chemical_A_initial_condition.value = float(vp[0].find('.//initial_condition').text)
        # self.chemical_A_Dirichlet_boundary_condition.value = float(vp[0].find('.//Dirichlet_boundary_condition').text)
        # if vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
        #   self.chemical_A_Dirichlet_boundary_condition_toggle.value = True
        # else:
        #   self.chemical_A_Dirichlet_boundary_condition_toggle.value = False

        # self.chemical_B_diffusion_coefficient.value = float(vp[1].find('.//diffusion_coefficient').text)
        # self.chemical_B_decay_rate.value = float(vp[1].find('.//decay_rate').text)
        # self.chemical_B_initial_condition.value = float(vp[1].find('.//initial_condition').text)
        # self.chemical_B_Dirichlet_boundary_condition.value = float(vp[1].find('.//Dirichlet_boundary_condition').text)
        # if vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
        #   self.chemical_B_Dirichlet_boundary_condition_toggle.value = True
        # else:
        #   self.chemical_B_Dirichlet_boundary_condition_toggle.value = False

        # self.chemical_C_diffusion_coefficient.value = float(vp[2].find('.//diffusion_coefficient').text)
        # self.chemical_C_decay_rate.value = float(vp[2].find('.//decay_rate').text)
        # self.chemical_C_initial_condition.value = float(vp[2].find('.//initial_condition').text)
        # self.chemical_C_Dirichlet_boundary_condition.value = float(vp[2].find('.//Dirichlet_boundary_condition').text)
        # if vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
        #   self.chemical_C_Dirichlet_boundary_condition_toggle.value = True
        # else:
        #   self.chemical_C_Dirichlet_boundary_condition_toggle.value = False

        # if uep.find('.//options//calculate_gradients').text.lower() == 'true':
        #   self.calculate_gradient.value = True
        # else:
        #   self.calculate_gradient.value = False
        # if uep.find('.//options//track_internalized_substrates_in_each_agent').text.lower() == 'true':
        #   self.track_internal.value = True
        # else:
        #   self.track_internal.value = False

    # Read values from the GUI widgets and generate/write a new XML
    def fill_xml(self, xml_root):
        pass