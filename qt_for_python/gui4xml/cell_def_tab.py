"""
Authors:
Randy Heiland (heiland@iu.edu)
Adam Morrow, Grant Waldrow, Drew Willis, Kim Crevecoeur
Dr. Paul Macklin (macklinp@iu.edu)

--- Versions ---
0.1 - initial version
"""

import sys
from PySide6 import QtCore, QtGui
#from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import *
from PySide6.QtGui import QDoubleValidator

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class CellDef(QWidget):
    def __init__(self):
        super().__init__()
        # global self.params_cell_def

        self.current_cell_def = None
        self.xml_root = None

        # self.cell_defs = CellDefInstances()
        self.cell_def_horiz_layout = QHBoxLayout()

        splitter = QSplitter()

        tree_widget_width = 160

        self.tree = QTreeWidget()
        self.tree.setStyleSheet("background-color: lightgray")
        self.tree.setFixedWidth(tree_widget_width)
        # self.tree.setColumnCount(1)
        self.tree.itemClicked.connect(self.tree_item_changed_cb)

        header = QTreeWidgetItem(["---  Cell Type  ---"])
        self.tree.setHeaderItem(header)

        # cellname = QTreeWidgetItem(["epi cell"])
        # self.tree.insertTopLevelItem(0,cellname)

        # cellname = QTreeWidgetItem(["macrophage"])
        # self.tree.insertTopLevelItem(1,cellname)

        # cities =  QTreeWidgetItem(treeWidget)

        # titem = QTreeWidgetItem
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

        # self.log_widget.setHeaderItem(QTreeWidgetItem(["date", "origin", "type", "message"]))


        self.cell_def_horiz_layout.addWidget(self.tree)

        self.scroll_cell_def_tree = QScrollArea()
        self.scroll_cell_def_tree.setWidget(self.tree)

        # splitter.addWidget(self.tree)
        splitter.addWidget(self.scroll_cell_def_tree)

        #-------------------------------------------
        # self.tab = QWidget()
        # self.tabs.resize(200,5)
        
        #-------------------------------------------
        label_width = 210
        units_width = 70

        self.scroll = QScrollArea()
        splitter.addWidget(self.scroll)
        # self.cell_def_horiz_layout.addWidget(self.scroll)

        self.params_cell_def = QWidget()
        self.vbox = QVBoxLayout()

        # self.cell_def_horiz_layout.addWidget(self.)

        #------------------
        hbox = QHBoxLayout()
        self.new_button = QPushButton("New")
        hbox.addWidget(self.new_button)

        self.copy_button = QPushButton("Copy")
        hbox.addWidget(self.copy_button)

        self.delete_button = QPushButton("Delete")
        hbox.addWidget(self.delete_button)

        self.vbox.addLayout(hbox)
        self.vbox.addWidget(QHLine())

        #------------------
        hbox = QHBoxLayout()
        label = QLabel("Name of cell type:")
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
        self.cycle_dropdown = QComboBox()
        self.cycle_dropdown.setFixedWidth(300)
        # self.cycle_dropdown.currentIndex.connect(self.cycle_changed_cb)
        self.cycle_dropdown.currentIndexChanged.connect(self.cycle_changed_cb)

        # Rf. Section 17 of User Guide and core/PhysiCell_constants.{h,cpp}
        # static const int advanced_Ki67_cycle_model= 0;
        # static const int basic_Ki67_cycle_model=1;
        # static const int flow_cytometry_cycle_model=2;
        # static const int live_apoptotic_cycle_model=3;
        # static const int total_cells_cycle_model=4;
        # static const int live_cells_cycle_model = 5; 
        # static const int flow_cytometry_separated_cycle_model = 6; 
        # static const int cycling_quiescent_model = 7; 
        self.cycle_dropdown.addItem("live cells")
        self.cycle_dropdown.addItem("basic Ki67")
        self.cycle_dropdown.addItem("advanced Ki67")
        self.cycle_dropdown.addItem("flow cytometry")
        self.cycle_dropdown.addItem("flow cytometry separated")
        self.cycle_dropdown.addItem("cycling quiescent")
        # self.cycle_dropdown.addItem("live apoptotic")
        # self.cycle_dropdown.addItem("total cells")

        self.vbox.addWidget(self.cycle_dropdown)

        #=====  Phenotype 
        #============  Cycle ================================
        label = QLabel("Phenotype: cycle")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)

        #----------------------------
        hbox = QHBoxLayout()
        label = QLabel("phase 0->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate0_0 = QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_0)

        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        #------ Cycle transition rates ----------------------
        hbox = QHBoxLayout()
        label = QLabel("phase 0->1 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate0_1 = QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_1.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_1)

        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 1->2 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate1_2 = QLineEdit()
        self.cycle_trate1_2.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate1_2)

        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 2->3 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate2_3 = QLineEdit()
        self.cycle_trate2_3.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate2_3)

        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 3->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_trate3_0 = QLineEdit()
        self.cycle_trate3_0.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate3_0)

        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        #------ Cycle duration rates ----------------------
        hbox = QHBoxLayout()
        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_duration0 = QLineEdit()
        self.cycle_duration0.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_duration0)

        self.cycle_duration0_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.cycle_duration0_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_duration1 = QLineEdit()
        self.cycle_duration1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_duration1)

        self.cycle_duration1_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.cycle_duration1_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 2 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_duration2 = QLineEdit()
        self.cycle_duration2.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_duration2)

        self.cycle_duration2_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.cycle_duration2_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("phase 3 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.cycle_duration3 = QLineEdit()
        self.cycle_duration3.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_duration3)

        self.cycle_duration3_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.cycle_duration3_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #============  Death ================================
        label = QLabel("Phenotype: death")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #----------------
        label = QLabel("Apoptosis")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        self.vbox.addWidget(label)

        hbox = QHBoxLayout()
        label = QLabel("death rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_death_rate = QLineEdit()
        self.apoptosis_death_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_death_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        # <cycle code="6" name="Flow cytometry model (separated)">  
        #     <phase_durations units="min"> 
        #         <duration index="0" fixed_duration="false">300.0</duration>
        #         <duration index="1" fixed_duration="true">480</duration>
        #         <duration index="2" fixed_duration="true">240</duration>
        #         <duration index="3" fixed_duration="true">60</duration>
        #     </phase_durations>

        hbox = QHBoxLayout()
        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.apoptosis_phase0_duration = QLineEdit()
        self.apoptosis_phase0_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_phase0_duration)

        self.apoptosis_phase0_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.apoptosis_phase0_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-------
        hbox = QHBoxLayout()
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_phase1_duration = QLineEdit()
        self.apoptosis_phase1_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_phase1_duration)

        self.apoptosis_phase1_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.apoptosis_phase1_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-------
        hbox = QHBoxLayout()
        label = QLabel("phase 2 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_phase2_duration = QLineEdit()
        self.apoptosis_phase2_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_phase2_duration)

        self.apoptosis_phase2_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.apoptosis_phase2_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-------
        hbox = QHBoxLayout()
        label = QLabel("phase 3 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_phase3_duration = QLineEdit()
        self.apoptosis_phase3_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_phase3_duration)

        self.apoptosis_phase3_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.apoptosis_phase3_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-------
        # <phase_durations units="min">
        #     <duration index="0" fixed_duration="true">516</duration>

        # <unlysed_fluid_change_rate units="1/min">0.05</unlysed_fluid_change_rate>
        # <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>
        hbox = QHBoxLayout()
        label = QLabel("unlysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_unlysed_rate = QLineEdit()
        self.apoptosis_unlysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_unlysed_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("lysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_lysed_rate = QLineEdit()
        self.apoptosis_lysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_lysed_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_cytoplasmic_biomass_change_rate = QLineEdit()
        self.apoptosis_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_cytoplasmic_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        hbox = QHBoxLayout()
        label = QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_nuclear_biomass_change_rate = QLineEdit()
        self.apoptosis_nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_nuclear_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("calcification rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_calcification_rate = QLineEdit()
        self.apoptosis_calcification_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_calcification_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("relative rupture volume")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.apoptosis_relative_rupture_volume = QLineEdit()
        self.apoptosis_relative_rupture_volume.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_relative_rupture_volume)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-------------------------
        # self.vbox.addWidget(QHLine())
        label = QLabel("Necrosis")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        # label_width = 210
        # units_width = 45
        hbox = QHBoxLayout()
        label = QLabel("death rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_death_rate = QLineEdit()
        self.necrosis_death_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_death_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-----
        hbox = QHBoxLayout()
        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_phase0_duration = QLineEdit()
        self.necrosis_phase0_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_phase0_duration)

        self.necrosis_phase0_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.necrosis_phase0_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-----
        hbox = QHBoxLayout()
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_phase1_duration = QLineEdit()
        self.necrosis_phase1_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_phase1_duration)

        self.necrosis_phase1_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.necrosis_phase1_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #-----
        hbox = QHBoxLayout()
        label = QLabel("phase 2 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_phase2_duration = QLineEdit()
        self.necrosis_phase2_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_phase2_duration)

        self.necrosis_phase2_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.necrosis_phase2_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        #-----
        hbox = QHBoxLayout()
        label = QLabel("phase 3 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_phase3_duration = QLineEdit()
        self.necrosis_phase3_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_phase3_duration)

        self.necrosis_phase3_duration_fixed = QCheckBox("Fixed")
        hbox.addWidget(self.necrosis_phase3_duration_fixed)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        # <phase_durations units="min">
        #     <duration index="0" fixed_duration="true">516</duration>

        #----------------------------------------
        # <unlysed_fluid_change_rate units="1/min">0.05</unlysed_fluid_change_rate>
        # <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>
        hbox = QHBoxLayout()
        label = QLabel("unlysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_unlysed_rate = QLineEdit()
        self.necrosis_unlysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_unlysed_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("lysed fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_lysed_rate = QLineEdit()
        self.necrosis_lysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_lysed_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_cytoplasmic_biomass_change_rate = QLineEdit()
        self.necrosis_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_cytoplasmic_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        hbox = QHBoxLayout()
        label = QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_nuclear_biomass_change_rate = QLineEdit()
        self.necrosis_nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_nuclear_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("calcification rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_calcification_rate = QLineEdit()
        self.necrosis_calcification_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_calcification_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("relative rupture volume")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.necrosis_relative_rupture_volume = QLineEdit()
        self.necrosis_relative_rupture_volume.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.necrosis_relative_rupture_volume)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #============  Volume ================================
        label = QLabel("Phenotype: volume")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # <total units="micron^3">2494</total>
        # <fluid_fraction units="dimensionless">0.75</fluid_fraction>
        # <nuclear units="micron^3">540</nuclear>
        hbox = QHBoxLayout()
        label = QLabel("total")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_total = QLineEdit()
        self.volume_total.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_total)
        units = QLabel("micron^3")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("fluid fraction")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_fluid_fraction = QLineEdit()
        self.volume_fluid_fraction.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_fluid_fraction)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("nuclear")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_nuclear = QLineEdit()
        self.volume_nuclear.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_nuclear)
        units = QLabel("micron^3")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <fluid_change_rate units="1/min">0.05</fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">0.0045</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">0.0055</nuclear_biomass_change_rate>

        hbox = QHBoxLayout()
        label = QLabel("fluid change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_fluid_change_rate = QLineEdit()
        self.volume_fluid_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_fluid_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("cytoplasmic biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_cytoplasmic_biomass_change_rate = QLineEdit()
        self.volume_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_cytoplasmic_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("nuclear biomass change rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_nuclear_biomass_change_rate = QLineEdit()
        self.volume_nuclear_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_nuclear_biomass_change_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <calcified_fraction units="dimensionless">0</calcified_fraction>
        # <calcification_rate units="1/min">0</calcification_rate>
        hbox = QHBoxLayout()
        label = QLabel("calcification fraction")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_calcified_fraction = QLineEdit()
        self.volume_calcified_fraction.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_calcified_fraction)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("calcified rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.volume_calcification_rate = QLineEdit()
        self.volume_calcification_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.volume_calcification_rate)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
        
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        hbox = QHBoxLayout()
        label = QLabel("relative rupture volume")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.relative_rupture_volume = QLineEdit()
        self.relative_rupture_volume.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.relative_rupture_volume)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        # self.vbox.addWidget(QHLine())
        #============  Mechanics ================================
        label = QLabel("Phenotype: mechanics")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

    # <cell_cell_adhesion_strength units="micron/min">0.4</cell_cell_adhesion_strength>
    # <cell_cell_repulsion_strength units="micron/min">10.0</cell_cell_repulsion_strength>
    # <relative_maximum_adhesion_distance units="dimensionless">1.25</relative_maximum_adhesion_distance>
        hbox = QHBoxLayout()
        label = QLabel("cell-cell adhesion strength")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.cell_cell_adhesion_strength = QLineEdit()
        self.cell_cell_adhesion_strength.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cell_cell_adhesion_strength)
        units = QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("cell-cell repulsion strength")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.cell_cell_repulsion_strength = QLineEdit()
        self.cell_cell_repulsion_strength.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cell_cell_repulsion_strength)
        units = QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("relative max adhesion distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.relative_maximum_adhesion_distance = QLineEdit()
        self.relative_maximum_adhesion_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.relative_maximum_adhesion_distance)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)
    
    # <options>
    #     <set_relative_equilibrium_distance enabled="false" units="dimensionless">1.8</set_relative_equilibrium_distance>
    #     <set_absolute_equilibrium_distance enabled="false" units="micron">15.12</set_absolute_equilibrium_distance>
    # </options>
        label = QLabel("Options:")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        self.vbox.addWidget(label)

        #--------
        hbox = QHBoxLayout()
        label = QLabel("relative equilibrium distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.set_relative_equilibrium_distance = QLineEdit()
        self.set_relative_equilibrium_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.set_relative_equilibrium_distance)

        self.set_relative_equilibrium_distance_enabled = QCheckBox("enable")
        hbox.addWidget(self.set_relative_equilibrium_distance_enabled)

        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        #--------
        hbox = QHBoxLayout()
        label = QLabel("absolute equilibrium distance")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.set_absolute_equilibrium_distance = QLineEdit()
        self.set_absolute_equilibrium_distance.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.set_absolute_equilibrium_distance)

        self.set_absolute_equilibrium_distance_enabled = QCheckBox("enable")
        hbox.addWidget(self.set_absolute_equilibrium_distance_enabled)

        units = QLabel("micron")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        #============  Motility ================================
        label = QLabel("Phenotype: motility")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        # <speed units="micron/min">1</speed>
        # <persistence_time units="min">1</persistence_time>
        # <migration_bias units="dimensionless">.75</migration_bias>
        hbox = QHBoxLayout()
        label = QLabel("speed")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.speed = QLineEdit()
        self.speed.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.speed)
        units = QLabel("micron/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("persistence time")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.persistence_time = QLineEdit()
        self.persistence_time.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.persistence_time)
        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("migration bias")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.migration_bias = QLineEdit()
        self.migration_bias.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.migration_bias)
        units = QLabel("")
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
        hbox = QHBoxLayout()
        self.motility_enabled = QCheckBox("enable")
        # self.motility_enabled.setAlignment(QtCore.Qt.AlignRight)
        # label.setFixedWidth(label_width)
        hbox.addWidget(self.motility_enabled)

        self.motility_2D = QCheckBox("2D")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.motility_2D)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("Chemotaxis")
        label.setFixedWidth(200)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setStyleSheet('background-color: yellow')
        hbox.addWidget(label)

        self.chemotaxis_enabled = QCheckBox("enabled")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.chemotaxis_enabled)
        self.vbox.addLayout(hbox)

        self.motility_substrate_dropdown = QComboBox()
        self.motility_substrate_dropdown.setFixedWidth(300)
        # self.cycle_dropdown.currentIndex.connect(self.cycle_changed_cb)
        # self.motility_substrate_dropdown.currentIndexChanged.connect(self.motility_substrate_changed_cb)
        # self.motility_substrate_dropdown.addItem("oxygen")
        self.vbox.addWidget(self.motility_substrate_dropdown)

        #============  Secretion ================================
        label = QLabel("Phenotype: secretion")
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
        label = QLabel("oxygen")
        label.setStyleSheet('background-color: lightgreen')
        label.setFixedWidth(150)
        self.vbox.addWidget(label)

        hbox = QHBoxLayout()
        label = QLabel("secretion rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_rate1 = QLineEdit()
        self.secretion_rate1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_rate1)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("target")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_target1 = QLineEdit()
        self.secretion_target1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_target1)
        units = QLabel("")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("uptake rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.uptake_rate1 = QLineEdit()
        self.uptake_rate1.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.uptake_rate1)
        units = QLabel("1/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        label = QLabel("net export rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_net_export_rate = QLineEdit()
        self.secretion_net_export_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_net_export_rate)
        units = QLabel("total/min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(units)
        self.vbox.addLayout(hbox)


        #============  Molecular ================================
        label = QLabel("Phenotype: molecular")
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #=====  Custom data 
        label = QLabel("Custom data")
        label.setStyleSheet("background-color: cyan")
        self.vbox.addWidget(label)
        # self.vbox.addWidget(QHLine())

        #==================================================================
        self.params_cell_def.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.params_cell_def)


        self.save_button = QPushButton("Save")
        # self.text = QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)

        self.layout = QVBoxLayout(self)

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
        # pass
        print('------ cycle_changed_cb(): idx = ',idx)
        # QMessageBox.information(self, "Cycle Changed:",
                #   "Current Cycle Index: %d" % idx )



    def fill_motility_substrates(self):
        uep = self.xml_root.find('.//microenvironment_setup')  # find unique entry point
        # vp = []   # pointers to <variable> nodes
        if uep:
            idx = 0
            for var in uep.findall('variable'):
                # vp.append(var)
                # print(var.attrib['name'])
                name = var.attrib['name']
                self.motility_substrate_dropdown.addItem(name)

    def tree_item_changed_cb(self, it,col):
        print('--- tree_item_changed:', it, col, it.text(col) )
        self.current_cell_def = it.text(col)
        print('--- self.current_cell_def= ',self.current_cell_def )
        # fill in the GUI with this one's params
        self.fill_gui(self.current_cell_def)

    def populate_tree(self):
        uep = self.xml_root.find(".//cell_definitions")
        if uep:
            self.tree.clear()
            idx = 0
            for cell_def in uep:
                # print(cell_def.attrib['name'])
                cd_name = cell_def.attrib['name']
                cellname = QTreeWidgetItem([cd_name])
                self.tree.insertTopLevelItem(idx,cellname)
                idx += 1

    def first_cell_def_name(self):
        uep = self.xml_root.find(".//cell_definitions//cell_definition")
        if uep:
                return(uep.attrib['name'])

    def fill_gui(self, cell_def_name):
	# <cell_definitions>
	# 	<cell_definition name="default" ID="0">

        # <cell_definition name="motile tumor cell" ID="1">
        if cell_def_name == None:
            cell_def_name = self.xml_root.find(".//cell_definitions//cell_definition").attrib['name']

        print('fill_gui: cell_def_name=',cell_def_name)
        self.cell_type_name.setText(cell_def_name)


        uep = self.xml_root.find(".//cell_definitions")
        if uep:
            # self.tree.clear()
            idx = 0
            for cell_def in uep:
                # print(cell_def.attrib['name'])
                cd_name = cell_def.attrib['name']
                # cd_cycle_code = cell_def.attrib['name']
                cellname = QTreeWidgetItem([cd_name])
                print('cellname.text(0)=',cellname.text(0))
                cellidx = QTreeWidgetItem([cd_name]).indexOfChild
                print('cellidx=',cellidx)
                print('cell_def_name=',cell_def_name)
                if cellname.text(0) == cell_def_name:
                    print("break out of cell_def loop with idx=",idx)
                    break
                # self.tree.insertTopLevelItem(idx,cellname)
                idx += 1

        idx += 1  # we use 1-offset indices below 

        cycle_path = ".//cell_definition[" + str(idx) + "]//phenotype//cycle"
        cycle_code = uep.find(cycle_path).attrib['code']
        print(' >> cycle_path=',cycle_path, ", code=",cycle_code)
        # static const int advanced_Ki67_cycle_model= 0;
        # static const int basic_Ki67_cycle_model=1;
        # static const int flow_cytometry_cycle_model=2;
        # static const int live_apoptotic_cycle_model=3;
        # static const int total_cells_cycle_model=4;
        # static const int live_cells_cycle_model = 5; 
        # static const int flow_cytometry_separated_cycle_model = 6; 
        # static const int cycling_quiescent_model = 7; 

        # self.cycle_dropdown.addItem("live cells")
        # self.cycle_dropdown.addItem("basic Ki67")
        # self.cycle_dropdown.addItem("advanced Ki67")
        # self.cycle_dropdown.addItem("flow cytometry")
        # self.cycle_dropdown.addItem("flow cytometry separated")
        # self.cycle_dropdown.addItem("cycling quiescent")

        if cycle_code == 6:
            self.cycle_dropdown.setCurrentIndex(4)
        else:
            self.cycle_dropdown.setCurrentIndex(1)


        # <cycle code="6" name="Flow cytometry model (separated)">  
        #     <phase_durations units="min"> 
        #         <duration index="0" fixed_duration="false">300.0</duration>
        #         <duration index="1" fixed_duration="true">480</duration>
        #         <duration index="2" fixed_duration="true">240</duration>
        #         <duration index="3" fixed_duration="true">60</duration>
        #     </phase_durations>
        #
        # self.phase0_duration = QLineEdit()
        phase_durations_path = cycle_path + "//phase_durations"
        print(' >> phase_durations_path =',phase_durations_path )
        pd_uep = uep.find(phase_durations_path)
        print(' >> pd_uep =',pd_uep )
        if pd_uep:
            for pd in pd_uep: 
                print(pd)
                print("index=",pd.attrib["index"])
                if  pd.attrib['index'] == "0":
                    self.cycle_duration0.setText(pd.text)
                elif  pd.attrib['index'] == "1":
                    self.cycle_duration1.setText(pd.text)
                elif  pd.attrib['index'] == "2":
                    self.cycle_duration2.setText(pd.text)
                elif  pd.attrib['index'] == "3":
                    self.cycle_duration3.setText(pd.text)

        # rf. microenv:
        # self.cell_type_name.setText(var.attrib['name'])
        # self.diffusion_coef.setText(vp[0].find('.//diffusion_coefficient').text)

        # ------------------ cell_definition: default
        # ---------  cycle (live)
        # self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)

                # <death> 
                #   <model code="100" name="apoptosis"> 
                #    ...
                #   <model code="101" name="necrosis">

        # ---------  death 

        death_path = ".//cell_definition[" + str(idx) + "]//phenotype//death//"
        print('death_path=',death_path)

        # rwh/TODO: validate we've got apoptosis or necrosis since order is not required in XML.
        apoptosis_path = death_path + "model[1]//"
        # self.apoptosis_death_rate.setText(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.apoptosis_death_rate.setText(uep.find(apoptosis_path + 'death_rate').text)

        phase_durations_path = apoptosis_path + "phase_durations"
        print(' >> phase_durations_path =',phase_durations_path )
        pd_uep = uep.find(phase_durations_path)
        print(' >> pd_uep =',pd_uep )
        if pd_uep:
            for pd in pd_uep: 
                print(pd)
                print("index=",pd.attrib["index"])
                if  pd.attrib['index'] == "0":
                    self.apoptosis_phase0_duration.setText(pd.text)
                elif  pd.attrib['index'] == "1":
                    self.apoptosis_phase1_duration.setText(pd.text)
                elif  pd.attrib['index'] == "2":
                    self.apoptosis_phase2_duration.setText(pd.text)
                elif  pd.attrib['index'] == "3":
                    self.apoptosis_phase3_duration.setText(pd.text)

        #-----
        necrosis_path = death_path + "model[2]//"
        self.necrosis_death_rate.setText(uep.find(necrosis_path + 'death_rate').text)

        phase_durations_path = necrosis_path + "phase_durations"
        print(' >> necrosis phase_durations_path =',phase_durations_path )
        pd_uep = uep.find(phase_durations_path)
        print(' >> pd_uep =',pd_uep )
        if pd_uep:
            for pd in pd_uep: 
                print(pd)
                print("index=",pd.attrib["index"])
                if  pd.attrib['index'] == "0":
                    self.necrosis_phase0_duration.setText(pd.text)
                elif  pd.attrib['index'] == "1":
                    self.necrosis_phase1_duration.setText(pd.text)
                elif  pd.attrib['index'] == "2":
                    self.necrosis_phase2_duration.setText(pd.text)
                elif  pd.attrib['index'] == "3":
                    self.necrosis_phase3_duration.setText(pd.text)

        #-----
        apoptosis_params_path = apoptosis_path + "parameters//"
        necrosis_params_path = necrosis_path + "parameters//"

        # necrosis_path = ".//cell_definition[" + str(idx) + "]//phenotype//death//"
        # self.apoptosis_unlysed_rate.setText(uep.find('.//cell_definition[1]//phenotype//death//model[1]//unlysed_fluid_change_rate').text)

        # full_str = death_path + "model[1]//unlysed_fluid_change_rate"
        # print('full_str=',full_str)
        # self.apoptosis_unlysed_rate.setText(uep.find(full_str).text)

        # <parameters>
        #     <unlysed_fluid_change_rate units="1/min">0.07</unlysed_fluid_change_rate>
        #     <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        #     <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        #     <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        #     <calcification_rate units="1/min">0</calcification_rate>
        #     <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        #---- apoptosis
        self.apoptosis_unlysed_rate.setText(uep.find(apoptosis_params_path+"unlysed_fluid_change_rate").text)
        self.apoptosis_lysed_rate.setText(uep.find(apoptosis_params_path+"lysed_fluid_change_rate").text)
        self.apoptosis_cytoplasmic_biomass_change_rate.setText(uep.find(apoptosis_params_path+"cytoplasmic_biomass_change_rate").text)
        self.apoptosis_nuclear_biomass_change_rate.setText(uep.find(apoptosis_params_path+"nuclear_biomass_change_rate").text)
        self.apoptosis_calcification_rate.setText(uep.find(apoptosis_params_path+"nuclear_biomass_change_rate").text)
        self.apoptosis_relative_rupture_volume.setText(uep.find(apoptosis_params_path+"relative_rupture_volume").text)

        #---- necrosis
        self.necrosis_unlysed_rate.setText(uep.find(necrosis_params_path+"unlysed_fluid_change_rate").text)
        self.necrosis_lysed_rate.setText(uep.find(necrosis_params_path+"lysed_fluid_change_rate").text)
        self.necrosis_cytoplasmic_biomass_change_rate.setText(uep.find(necrosis_params_path+"cytoplasmic_biomass_change_rate").text)
        self.necrosis_nuclear_biomass_change_rate.setText(uep.find(necrosis_params_path+"nuclear_biomass_change_rate").text)
        self.necrosis_calcification_rate.setText(uep.find(necrosis_params_path+"nuclear_biomass_change_rate").text)
        self.necrosis_relative_rupture_volume.setText(uep.find(necrosis_params_path+"relative_rupture_volume").text)

        # self.apoptosis_unlysed_rate.setText(uep.find("'" + death_path + "model[1]//unlysed_fluid_change_rate'" + ").text)"

        # self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//lysed_fluid_change_rate').text)
        # self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//cytoplasmic_biomass_change_rate').text)
        # self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//nuclear_biomass_change_rate').text)
        # self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//calcification_rate').text)
        # self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//parameters//relative_rupture_volume').text)
        # self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        # self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        # self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        # self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        # self.float12.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        # self.float13.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        # self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)

        # # ---------  volume 
                # <volume>  
				# 	<total units="micron^3">2494</total>
				# 	<fluid_fraction units="dimensionless">0.75</fluid_fraction>
				# 	<nuclear units="micron^3">540</nuclear>
					
				# 	<fluid_change_rate units="1/min">0.05</fluid_change_rate>
				# 	<cytoplasmic_biomass_change_rate units="1/min">0.0045</cytoplasmic_biomass_change_rate>
				# 	<nuclear_biomass_change_rate units="1/min">0.0055</nuclear_biomass_change_rate>
					
				# 	<calcified_fraction units="dimensionless">0</calcified_fraction>
				# 	<calcification_rate units="1/min">0</calcification_rate>
					
				# 	<relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>

        volume_path = ".//cell_definition[" + str(idx) + "]//phenotype//volume//"
        print('volume_path=',volume_path)

        self.volume_total.setText(uep.find(volume_path+"total").text)
        self.volume_fluid_fraction.setText(uep.find(volume_path+"fluid_fraction").text)
        self.volume_nuclear.setText(uep.find(volume_path+"nuclear").text)
        self.volume_fluid_change_rate.setText(uep.find(volume_path+"fluid_change_rate").text)
        self.volume_cytoplasmic_biomass_change_rate.setText(uep.find(volume_path+"cytoplasmic_biomass_change_rate").text)
        self.volume_nuclear_biomass_change_rate.setText(uep.find(volume_path+"nuclear_biomass_change_rate").text)
        self.volume_calcified_fraction.setText(uep.find(volume_path+"calcified_fraction").text)
        self.volume_calcification_rate.setText(uep.find(volume_path+"calcification_rate").text)
        self.relative_rupture_volume.setText(uep.find(volume_path+"relative_rupture_volume").text)

        # self.necrosis_relative_rupture_volume.setText(uep.find(necrosis_params_path+"relative_rupture_volume").text)

        # self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//volume//total').text)
        # self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_fraction').text)
        # self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear').text)
        # self.float18.value = float(uep.find('.//cell_definition[1]//phenotype//volume//fluid_change_rate').text)
        # self.float19.value = float(uep.find('.//cell_definition[1]//phenotype//volume//cytoplasmic_biomass_change_rate').text)
        # self.float20.value = float(uep.find('.//cell_definition[1]//phenotype//volume//nuclear_biomass_change_rate').text)
        # self.float21.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcified_fraction').text)
        # self.float22.value = float(uep.find('.//cell_definition[1]//phenotype//volume//calcification_rate').text)
        # self.float23.value = float(uep.find('.//cell_definition[1]//phenotype//volume//relative_rupture_volume').text)

        # # ---------  mechanics 
        mechanics_path = ".//cell_definition[" + str(idx) + "]//phenotype//mechanics//"
        print('mechanics_path=',mechanics_path)

        self.cell_cell_adhesion_strength.setText(uep.find(mechanics_path+"cell_cell_adhesion_strength").text)
        self.cell_cell_repulsion_strength.setText(uep.find(mechanics_path+"cell_cell_repulsion_strength").text)
        self.relative_maximum_adhesion_distance.setText(uep.find(mechanics_path+"relative_maximum_adhesion_distance").text)

        mechanics_options_path = ".//cell_definition[" + str(idx) + "]//phenotype//mechanics//options//"
        self.set_relative_equilibrium_distance.setText(uep.find(mechanics_options_path+"set_relative_equilibrium_distance").text)
        self.set_absolute_equilibrium_distance.setText(uep.find(mechanics_options_path+"set_absolute_equilibrium_distance").text)


        # self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        # self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        # self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        # self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        # self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))

        # # ---------  motility 
        motility_path = ".//cell_definition[" + str(idx) + "]//phenotype//motility//"
        print('motility_path=',motility_path)

        self.speed.setText(uep.find(motility_path+"speed").text)
        self.persistence_time.setText(uep.find(motility_path+"persistence_time").text)
        self.migration_bias.setText(uep.find(motility_path+"migration_bias").text)

        motility_options_path = ".//cell_definition[" + str(idx) + "]//phenotype//motility//options//"


        # self.float29.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        # self.float30.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        # self.float31.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        # self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        # self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        # self.bool4.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//enabled').text.lower()))
        # self.chemotaxis_substrate1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//substrate').text
        # self.chemotaxis_direction1.value = uep.find('.//cell_definition[1]//phenotype//motility//options//chemotaxis//direction').text

        # # ---------  secretion 
        secretion_path = ".//cell_definition[" + str(idx) + "]//phenotype//secretion//"
        print('secretion_path =',secretion_path)

        # self.speed.setText(uep.find(secretion_path+"speed").text)

        # self.text0.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]').attrib['name']
        # self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_rate').text)
        # self.float33.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//secretion_target').text)
        # self.float34.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//uptake_rate').text)
        # self.float35.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[1]//net_export_rate').text)
        # self.text1.value = uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]').attrib['name']
        # self.float36.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_rate').text)
        # self.float37.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//secretion_target').text)
        # self.float38.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//uptake_rate').text)
        # self.float39.value = float(uep.find('.//cell_definition[1]//phenotype//secretion//substrate[2]//net_export_rate').text)


    # Read values from the GUI widgets and generate/write a new XML
    def fill_xml(self):
        pass
        # TODO: verify valid type (numeric) and range?
        # xml_root.find(".//x_min").text = str(self.xmin.value)
        # xml_root.find(".//x_max").text = str(self.xmax.value)

    def clear_gui(self):
        self.cell_type_name.setText('')
        self.cycle_trate0_0.setText('')
        self.cycle_trate0_1.setText('')
        self.cycle_trate1_2.setText('')
        self.cycle_trate2_3.setText('')
        self.cycle_trate3_0.setText('')
        self.cycle_duration0.setText('')
        self.cycle_duration1.setText('')
        self.cycle_duration2.setText('')
        self.cycle_duration3.setText('')
        self.apoptosis_death_rate.setText('')
        self.apoptosis_phase0_duration.setText('')
        self.apoptosis_phase1_duration.setText('')
        self.apoptosis_phase2_duration.setText('')
        self.apoptosis_phase3_duration.setText('')
        self.apoptosis_unlysed_rate.setText('')
        self.apoptosis_lysed_rate.setText('')
        self.apoptosis_cytoplasmic_biomass_change_rate.setText('')
        self.apoptosis_nuclear_biomass_change_rate.setText('')
        self.apoptosis_calcification_rate.setText('')
        self.apoptosis_relative_rupture_volume.setText('')
        self.necrosis_death_rate.setText('')
        self.necrosis_phase0_duration.setText('')
        self.necrosis_phase1_duration.setText('')
        self.necrosis_phase2_duration.setText('')
        self.necrosis_phase3_duration.setText('')
        self.necrosis_unlysed_rate.setText('')
        self.necrosis_lysed_rate.setText('')
        self.necrosis_cytoplasmic_biomass_change_rate.setText('')
        self.necrosis_nuclear_biomass_change_rate.setText('')
        self.necrosis_calcification_rate.setText('')
        self.necrosis_relative_rupture_volume.setText('')
        self.volume_total.setText('')
        self.volume_fluid_fraction.setText('')
        self.volume_nuclear.setText('')
        self.volume_fluid_change_rate.setText('')
        self.volume_cytoplasmic_biomass_change_rate.setText('')
        self.volume_nuclear_biomass_change_rate.setText('')
        self.volume_calcified_fraction.setText('')
        self.volume_calcification_rate.setText('')
        self.relative_rupture_volume.setText('')
        self.cell_cell_adhesion_strength.setText('')
        self.cell_cell_repulsion_strength.setText('')
        self.relative_maximum_adhesion_distance.setText('')
        self.set_relative_equilibrium_distance.setText('')
        self.set_absolute_equilibrium_distance.setText('')
        self.speed.setText('')
        self.persistence_time.setText('')
        self.migration_bias.setText('')
        self.secretion_rate1.setText('')
        self.secretion_target1.setText('')
        self.uptake_rate1.setText('')
        self.secretion_net_export_rate.setText('')
