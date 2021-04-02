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

class CellDef(QtWidgets.QWidget):
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

        header = QTreeWidgetItem(["---  Cell Type  ---"])
        self.tree.setHeaderItem(header)

        # cellname = QTreeWidgetItem(["epi cell"])
        # self.tree.insertTopLevelItem(0,cellname)

        # cellname = QTreeWidgetItem(["macrophage"])
        # self.tree.insertTopLevelItem(1,cellname)

        # cities =  QTreeWidgetItem(treeWidget)

        # titem = QtWidgets.QTreeWidgetItem
        # titem.setText(0,'ttt')

        # header.setText(0,"epithelial cell")
        # header.setText(1,"macrophage")
        # self.tree.addTopLevelItem(QTreeWidgetItem("foo"))

        items = []
        model = QtCore.QStringListModel()
        model.setStringList(["aaa","bbb"])
        # self.tree.insertTopLevelItems(None, model)
        # slist = QtCore.QStringList()
        # for i in range(10):
        #     items.append(QTreeWidgetItem(None, QtGui.QStringList(QString("item: %1").arg(i))))
        # self.tree.insertTopLevelItems(None, items)

        # self.log_widget.setHeaderItem(QtWidgets.QTreeWidgetItem(["date", "origin", "type", "message"]))


        self.cell_def_horiz_layout.addWidget(self.tree)

        self.scroll_cell_def_tree = QtWidgets.QScrollArea()
        self.scroll_cell_def_tree.setWidget(self.tree)

        # splitter.addWidget(self.tree)
        splitter.addWidget(self.scroll_cell_def_tree)

        #-------------------------------------------
        # self.tab = QtWidgets.QWidget()
        # self.tabs.resize(200,5)
        
        #-------------------------------------------
        label_width = 210
        units_width = 70

        self.scroll = QtWidgets.QScrollArea()
        splitter.addWidget(self.scroll)
        # self.cell_def_horiz_layout.addWidget(self.scroll)

        self.params_cell_def = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()

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
        label = QtWidgets.QLabel("Name of cell type:")
        label.setFixedWidth(110)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cell_type_name = QLineEdit()
        # Want to validate name, e.g., starts with alpha, no special chars, etc.
        # self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cell_type_name)
        self.vbox.addLayout(hbox)

        #------------------
        self.cycle_dropdown = QtWidgets.QComboBox()
        self.cycle_dropdown.setFixedWidth(300)
        # self.cycle_dropdown.currentIndex.connect(self.cycle_changed_cb)
        self.cycle_dropdown.currentIndexChanged.connect(self.cycle_changed_cb)

        # Rf. Section 17 of User Guide
        self.cycle_dropdown.addItem("live cells")
        self.cycle_dropdown.addItem("basic Ki67")
        self.cycle_dropdown.addItem("advanced Ki67")
        self.cycle_dropdown.addItem("flow cytometry")
        self.cycle_dropdown.addItem("flow cytometry separated")
        self.cycle_dropdown.addItem("cycling quiescent")
        self.cycle_dropdown.addItem("live apoptotic")
        self.cycle_dropdown.addItem("total cells")

        self.vbox.addWidget(self.cycle_dropdown)

        #=====  Phenotype 
        #============  Cycle ================================
        label = QtWidgets.QLabel("Phenotype: cycle")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 0->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate0_0 = QtWidgets.QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_0)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 0->1 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate0_1 = QtWidgets.QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_1.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_1)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 1->2 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate1_2 = QtWidgets.QLineEdit()
        self.cycle_trate1_2.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate1_2)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 2->3 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate2_3 = QtWidgets.QLineEdit()
        self.cycle_trate2_3.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate2_3)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 3->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate3_0 = QtWidgets.QLineEdit()
        self.cycle_trate3_0.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate3_0)

        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #============  Death ================================
        label = QtWidgets.QLabel("Phenotype: death")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #-----
        label = QtWidgets.QLabel("Apoptosis")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        self.vbox.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("death rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.death_apop_rate = QtWidgets.QLineEdit()
        self.death_apop_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.death_apop_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.phase0_duration = QtWidgets.QLineEdit()
        self.phase0_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.phase0_duration)
        units = QtWidgets.QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.phase1_duration = QtWidgets.QLineEdit()
        self.phase1_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.phase1_duration)
        units = QtWidgets.QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        # <phase_durations units="min">
        #     <duration index="0" fixed_duration="true">516</duration>

        # <unlysed_fluid_change_rate units="1/min">0.05</unlysed_fluid_change_rate>
        # <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("unlysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_unlysed_rate = QtWidgets.QLineEdit()
        self.apoptosis_unlysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_unlysed_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("lysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_lysed_rate = QtWidgets.QLineEdit()
        self.apoptosis_lysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_lysed_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_cytoplasmic_biomass_change_rate = QtWidgets.QLineEdit()
        self.apoptosis_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_cytoplasmic_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_nuclear_biomass_change_rate = QtWidgets.QLineEdit()
        self.apoptosis_nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_nuclear_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("calcification rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.calcification_rate = QtWidgets.QLineEdit()
        self.calcification_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.calcification_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("relative rupture volume")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.relative_rupture_volume = QtWidgets.QLineEdit()
        self.relative_rupture_volume.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.relative_rupture_volume)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-----------------------------------------------------------
        # self.vbox.addWidget(QHLine())
        label = QtWidgets.QLabel("Necrosis")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        # label_width = 210
        # units_width = 45
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("death rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.death_necrosis_rate = QtWidgets.QLineEdit()
        self.death_necrosis_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.death_necrosis_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.phase0_duration = QtWidgets.QLineEdit()
        self.phase0_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.phase0_duration)
        units = QtWidgets.QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.phase1_duration = QtWidgets.QLineEdit()
        self.phase1_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.phase1_duration)
        units = QtWidgets.QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        # <phase_durations units="min">
        #     <duration index="0" fixed_duration="true">516</duration>

        # <unlysed_fluid_change_rate units="1/min">0.05</unlysed_fluid_change_rate>
        # <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("unlysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_unlysed_rate = QtWidgets.QLineEdit()
        self.necrosis_unlysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_unlysed_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("lysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_lysed_rate = QtWidgets.QLineEdit()
        self.necrosis_lysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_lysed_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_cytoplasmic_biomass_change_rate = QtWidgets.QLineEdit()
        self.necrosis_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_cytoplasmic_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_nuclear_biomass_change_rate = QtWidgets.QLineEdit()
        self.necrosis_nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_nuclear_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("calcification rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.calcification_rate = QtWidgets.QLineEdit()
        self.calcification_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.calcification_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("relative rupture volume")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.relative_rupture_volume = QtWidgets.QLineEdit()
        self.relative_rupture_volume.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.relative_rupture_volume)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #============  Volume ================================
        label = QtWidgets.QLabel("Phenotype: volume")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # <total units="micron^3">2494</total>
        # <fluid_fraction units="dimensionless">0.75</fluid_fraction>
        # <nuclear units="micron^3">540</nuclear>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("total")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_total = QtWidgets.QLineEdit()
        self.volume_total.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_total)
        units = QtWidgets.QLabel("micron^3")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("fluid fraction")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_fluid_fraction = QtWidgets.QLineEdit()
        self.volume_fluid_fraction.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_fluid_fraction)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("nuclear")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_nuclear = QtWidgets.QLineEdit()
        self.volume_nuclear.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_nuclear)
        units = QtWidgets.QLabel("micron^3")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <fluid_change_rate units="1/min">0.05</fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">0.0045</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">0.0055</nuclear_biomass_change_rate>

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_fluid_change_rate = QtWidgets.QLineEdit()
        self.volume_fluid_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_fluid_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.cytoplasmic_biomass_change_rate = QtWidgets.QLineEdit()
        self.cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cytoplasmic_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.nuclear_biomass_change_rate = QtWidgets.QLineEdit()
        self.nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.nuclear_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <calcified_fraction units="dimensionless">0</calcified_fraction>
        # <calcification_rate units="1/min">0</calcification_rate>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("calcified fraction")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.calcified_fraction = QtWidgets.QLineEdit()
        self.calcified_fraction.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.calcified_fraction)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("calcified rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.calcified_rate = QtWidgets.QLineEdit()
        self.calcified_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.calcified_rate)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>


        # self.vbox.addWidget(QHLine())
        #============  Mechanics ================================
        label = QtWidgets.QLabel("Phenotype: mechanics")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

    # <cell_cell_adhesion_strength units="micron/min">0.4</cell_cell_adhesion_strength>
    # <cell_cell_repulsion_strength units="micron/min">10.0</cell_cell_repulsion_strength>
    # <relative_maximum_adhesion_distance units="dimensionless">1.25</relative_maximum_adhesion_distance>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cell-cell adhesion strength")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.cell_cell_adhesion_strength = QtWidgets.QLineEdit()
        self.cell_cell_adhesion_strength.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cell_cell_adhesion_strength)
        units = QtWidgets.QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cell-cell repulsion strength")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.cell_cell_repulsion_strength = QtWidgets.QLineEdit()
        self.cell_cell_repulsion_strength.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cell_cell_repulsion_strength)
        units = QtWidgets.QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("relative max adhesion distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.relative_maximum_adhesion_distance = QtWidgets.QLineEdit()
        self.relative_maximum_adhesion_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.relative_maximum_adhesion_distance)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
    
    # <options>
    #     <set_relative_equilibrium_distance enabled="false" units="dimensionless">1.8</set_relative_equilibrium_distance>
    #     <set_absolute_equilibrium_distance enabled="false" units="micron">15.12</set_absolute_equilibrium_distance>
    # </options>
        label = QtWidgets.QLabel("Options:")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        self.vbox.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("relative equilibrium distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.set_relative_equilibrium_distance = QtWidgets.QLineEdit()
        self.set_relative_equilibrium_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.set_relative_equilibrium_distance)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("absolute equilibrium distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.set_absolute_equilibrium_distance = QtWidgets.QLineEdit()
        self.set_absolute_equilibrium_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.set_absolute_equilibrium_distance)
        units = QtWidgets.QLabel("micron")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        #============  Motility ================================
        label = QtWidgets.QLabel("Phenotype: motility")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        # <speed units="micron/min">1</speed>
        # <persistence_time units="min">1</persistence_time>
        # <migration_bias units="dimensionless">.75</migration_bias>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("speed")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.speed = QtWidgets.QLineEdit()
        self.speed.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.speed)
        units = QtWidgets.QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("persistence time")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.persistence_time = QtWidgets.QLineEdit()
        self.persistence_time.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.persistence_time)
        units = QtWidgets.QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("migration bias")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.migration_bias = QtWidgets.QLineEdit()
        self.migration_bias.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.migration_bias)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <options>
        #     <enabled>false</enabled>
        #     <use_2D>true</use_2D>
        #     <chemotaxis>
        #         <enabled>false</enabled>
        #         <substrate>virus</substrate>
        #         <direction>1</direction>
        #     </chemotaxis>
        # </options>
        hbox = QtWidgets.QHBoxLayout()
        self.motility_enabled = QtWidgets.QCheckBox("enable")
        # self.motility_enabled.setAlignment(QtCore.Qt.AlignRight)
        # label.setFixedWidth(label_width)
        hbox.addWidget(self.motility_enabled)

        self.motility_2D = QtWidgets.QCheckBox("2D")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.motility_2D)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Chemotaxis")
        label.setFixedWidth(200)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        hbox.addWidget(label)

        self.chemotaxis_enabled = QtWidgets.QCheckBox("enabled")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.chemotaxis_enabled)
        self.vbox.addLayout(hbox)

        self.motility_substrate_dropdown = QtWidgets.QComboBox()
        self.motility_substrate_dropdown.setFixedWidth(300)
        # self.cycle_dropdown.currentIndex.connect(self.cycle_changed_cb)
        # self.motility_substrate_dropdown.currentIndexChanged.connect(self.motility_substrate_changed_cb)
        # self.motility_substrate_dropdown.addItem("oxygen")
        self.vbox.addWidget(self.motility_substrate_dropdown)

        #============  Secretion ================================
        label = QtWidgets.QLabel("Phenotype: secretion")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        # <substrate name="virus">
        #     <secretion_rate units="1/min">0</secretion_rate>
        #     <secretion_target units="substrate density">1</secretion_target>
        #     <uptake_rate units="1/min">10</uptake_rate>
        #     <net_export_rate units="total substrate/min">0</net_export_rate> 
        # </substrate> 
        
        # <substrate name="interferon">
        #     <secretion_rate units="1/min">0</secretion_rate>
        #     <secretion_target units="substrate density">1</secretion_target>
        #     <uptake_rate units="1/min">0</uptake_rate>
        #     <net_export_rate units="total substrate/min">0</net_export_rate> 
        # </substrate> 
        label = QtWidgets.QLabel("oxygen")
        label.setStyleSheet('background-color: lightgreen')
        label.setFixedWidth(150)
        self.vbox.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("secretion rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_rate1 = QtWidgets.QLineEdit()
        self.secretion_rate1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_rate1)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("target")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_target1 = QtWidgets.QLineEdit()
        self.secretion_target1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_target1)
        units = QtWidgets.QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("uptake rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.uptake_rate1 = QtWidgets.QLineEdit()
        self.uptake_rate1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.uptake_rate1)
        units = QtWidgets.QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("net export rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_net_export_rate = QtWidgets.QLineEdit()
        self.secretion_net_export_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_net_export_rate)
        units = QtWidgets.QLabel("total/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        #============  Molecular ================================
        label = QtWidgets.QLabel("Phenotype: molecular")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #=====  Custom data 
        label = QtWidgets.QLabel("Custom data")
        label.setStyleSheet("background-color: cyan")
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #==================================================================
        self.params_cell_def.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.params_cell_def)


        self.save_button = QtWidgets.QPushButton("Save")
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

    @QtCore.Slot()
    def cycle_changed_cb(self, idx):
        pass
        # QtWidgets.QMessageBox.information(self, "Cycle Changed:",
                #   "Current Cycle Index: %d" % idx )



    def fill_motility_substrates(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        # vp = []   # pointers to <variable> nodes
        if uep:
            idx = 0
            for var in uep.findall('variable'):
                # vp.append(var)
                # print(var.attrib['name'])
                name = var.attrib['name']
                self.motility_substrate_dropdown.addItem(name)

    def fill_gui(self, xml_root):
	# <cell_definitions>
	# 	<cell_definition name="default" ID="0">

        uep = xml_root.find(".//cell_definitions")
        if uep:
            self.tree.clear()
            idx = 0
            for cell_def in uep:
                # print(cell_def.attrib['name'])
                cd_name = cell_def.attrib['name']
                cellname = QTreeWidgetItem([cd_name])
                self.tree.insertTopLevelItem(idx,cellname)
                idx += 1

        # self.xmin.setText(xml_root.find(".//x_min").text)
        # self.xmax.setText(xml_root.find(".//x_max").text)

    # Read values from the GUI widgets and generate/write a new XML
    def fill_xml(self, xml_root):
        pass
        # TODO: verify valid type (numeric) and range?
        # xml_root.find(".//x_min").text = str(self.xmin.value)
        # xml_root.find(".//x_max").text = str(self.xmax.value)
