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
        self.idx_current_cell_def = 1  # 1-offset for XML
        self.xml_root = None
        self.custom_data_count = 0
        self.custom_data_units_width = 90
        self.cycle_duration_flag = False

        self.stacked = QStackedWidget()
        self.stack_idx_t00 = -1
        self.stack_idx_t01 = -1
        self.stack_idx_t02 = -1
        self.stack_idx_t03 = -1

        self.stack_idx_d00 = -1
        self.stack_idx_d01 = -1
        self.stack_idx_d02 = -1
        self.stack_idx_d03 = -1

        # <substrate name="virus">
        #     <secretion_rate units="1/min">0</secretion_rate>
        #     <secretion_target units="substrate density">1</secretion_target>
        #     <uptake_rate units="1/min">10</uptake_rate>
        #     <net_export_rate units="total substrate/min">0</net_export_rate> 
        # </substrate> 

        # Create lists for cell type secretion values, for each substrate (index by substrate index)
        self.secretion_rate_val = []  # .setText(uep.find(secretion_sub1_path+"secretion_rate").text)
        self.secretion_target_val = []
        self.secretion_uptake_rate_val = []
        self.secretion_net_export_rate_val = []

        # self.cell_defs = CellDefInstances()
        self.cell_def_horiz_layout = QHBoxLayout()

        splitter = QSplitter()

        tree_widget_width = 160
        tree_widget_height = 400

        self.tree = QTreeWidget()
        # self.tree.setStyleSheet("background-color: lightgray")
        self.tree.setFixedWidth(tree_widget_width)
        self.tree.setFixedHeight(tree_widget_height)
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
        controls_hbox = QHBoxLayout()
        self.new_button = QPushButton("New")
        controls_hbox.addWidget(self.new_button)

        self.copy_button = QPushButton("Copy")
        controls_hbox.addWidget(self.copy_button)

        self.delete_button = QPushButton("Delete")
        controls_hbox.addWidget(self.delete_button)

        # self.vbox.addLayout(hbox)
        # self.vbox.addWidget(QHLine())

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
        # self.cycle_dropdown.currentIndexChanged.connect(self.cycle_phase_transition_cb)

        # Rf. Section 17 of User Guide and core/PhysiCell_constants.{h,cpp}
        # static const int advanced_Ki67_cycle_model= 0;
        # static const int basic_Ki67_cycle_model=1;
        # static const int flow_cytometry_cycle_model=2;
        # static const int live_apoptotic_cycle_model=3;
        # static const int total_cells_cycle_model=4;
        # static const int live_cells_cycle_model = 5; 
        # static const int flow_cytometry_separated_cycle_model = 6; 
        # static const int cycling_quiescent_model = 7; 
        self.cycle_dropdown.addItem("live cells")   # 0 -> 0
        self.cycle_dropdown.addItem("basic Ki67")   # 0 -> 1, 1 -> 0
        self.cycle_dropdown.addItem("advanced Ki67")  # 0 -> 1, 1 -> 2, 2 -> 0
        self.cycle_dropdown.addItem("flow cytometry") # 0 -> 1, 1 -> 2, 2 -> 0
        self.cycle_dropdown.addItem("flow cytometry separated") # 0->1, 1->2, 2->3, 3->0
        self.cycle_dropdown.addItem("cycling quiescent") # 0 -> 1, 1 -> 0
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
        self.rb1 = QRadioButton("transition rate(s)", self)
        self.rb1.clicked.connect(self.cycle_phase_transition_cb)
        hbox.addWidget(self.rb1)
        self.rb2 = QRadioButton("duration(s)", self)
        self.rb2.clicked.connect(self.cycle_phase_transition_cb)
        hbox.addWidget(self.rb2)
        hbox.addStretch(1)  # not sure about this, but keeps buttons shoved to left
        self.vbox.addLayout(hbox)

        #-----------------------------
        # We'll create a unique widget to hold different rates or durations, depending
        # on which cycle and method of defining it (transition rates or duration times) is chosen.
        # Then we will only display the relevant one, based on these choices.
        # self.stacked = QStackedWidget()

        # transition rates
        self.stack_t00 = QWidget()
        self.stack_t01 = QWidget()
        self.stack_t02 = QWidget()
        self.stack_t03 = QWidget()

        # duration times
        self.stack_d00 = QWidget()
        self.stack_d01 = QWidget()
        self.stack_d02 = QWidget()
        self.stack_d03 = QWidget()


        #------ Cycle transition rate (1 node) ----------------------
        # self.cycle_dropdown.addItem("live cells")   # 0 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        # glayout.addWidget(*Widget, row, column, rowspan, colspan)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate00 = QLineEdit()
        self.cycle_trate00.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_0.enter.connect(self.save_xml)
        glayout.addWidget(self.cycle_trate00, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate00_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate00_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan
        # hbox.addWidget(units_1min)
        self.stack_t00.setLayout(glayout)   

        idx_stacked_widget = 0
        self.stack_idx_t00 = idx_stacked_widget 
        print(" new stacked widget: t00 -------------> ",idx_stacked_widget)
        self.stacked.addWidget(self.stack_t00)  # <------------- stack widget 0


        #------ Cycle transition rates (2 nodes) ----------------------
        # self.cycle_dropdown.addItem("basic Ki67")   # 0 -> 1, 1 -> 0
        # self.cycle_dropdown.addItem("cycling quiescent") # 0 -> 1, 1 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0->1 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate01 = QLineEdit()
        self.cycle_trate01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate10 = QLineEdit()
        self.cycle_trate10.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate10, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate10_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate10_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        #-------
        # glayout.addWidget(QLabel("rwh-------------------------------AAAAAAAAAAAAAAAAAAAAAaa"), 2,0,4,4) # w, row, column, rowspan, colspan
        # glayout.addWidget(QLabel(""), 2,0,3,4) # w, row, column, rowspan, colspan
        # glayout.addStretch(0)

        #---
        self.stack_t01.setLayout(glayout)

        idx_stacked_widget += 1
        self.stack_idx_t01 = idx_stacked_widget 
        print(" new stacked widget: t01 -------------> ",idx_stacked_widget)
        self.stacked.addWidget(self.stack_t01) # <------------- stack widget 1


        #------ Cycle transition rates (3 nodes) ----------------------
        # self.cycle_dropdown.addItem("advanced Ki67")  # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry") # 0 -> 1, 1 -> 2, 2 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0->1 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_02_01 = QLineEdit()
        self.cycle_trate_02_01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_02_01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_02_01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_02_01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1->2 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_02_12 = QLineEdit()
        self.cycle_trate_02_12.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_02_12, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_02_12_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_02_12_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 2->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 2,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_02_20 = QLineEdit()
        self.cycle_trate_02_20.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_02_20, 2,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_02_20_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_02_20_fixed, 2,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 2,4,1,1) # w, row, column, rowspan, colspan

        #-----
        self.stack_t02.setLayout(glayout)
        idx_stacked_widget += 1
        print(" new stacked widget: t02 -------------> ",idx_stacked_widget)
        self.stack_idx_t02 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_t02)


        #------ Cycle transition rates (4 nodes) ----------------------
        # self.cycle_dropdown.addItem("flow cytometry separated") # 0->1, 1->2, 2->3, 3->0

        glayout = QGridLayout()

        label = QLabel("phase 0->1 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_03_01 = QLineEdit()
        self.cycle_trate_03_01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_03_01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_03_01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_03_01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1->2 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_03_12 = QLineEdit()
        self.cycle_trate_03_12.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_03_12, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_03_12_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_03_12_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 2->3 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 2,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_03_23 = QLineEdit()
        self.cycle_trate_03_23.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_03_23, 2,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_03_23_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_03_23_fixed, 2,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 2,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 3->0 transition rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 3,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_trate_03_30 = QLineEdit()
        self.cycle_trate_03_30.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_trate_03_30, 3,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_trate_03_30_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_trate_03_30_fixed, 3,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("1/min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 3,4,1,1) # w, row, column, rowspan, colspan

        #-----
        self.stack_t03.setLayout(glayout)
        idx_stacked_widget += 1
        print(" new stacked widget: t03 -------------> ",idx_stacked_widget)
        self.stack_idx_t03 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_t03)


        #===========================================================================
        #------ Cycle duration rates ----------------------
        # self.cycle_dropdown.addItem("live cells")   # 0 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1)
        # glayout.addWidget(*Widget, row, column, rowspan, colspan)

        self.cycle_duration00 = QLineEdit()
        self.cycle_duration00.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration00, 0,1,1,2)

        self.cycle_duration00_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration00_fixed, 0,3,1,1)

        units = QLabel("min")
        units.setFixedWidth(units_width)
        units.setAlignment(QtCore.Qt.AlignCenter)
        glayout.addWidget(units, 0,4,1,1)

        #-----
        self.stack_d00.setLayout(glayout)
        idx_stacked_widget += 1
        print(" new stacked widget: d00 -------------> ",idx_stacked_widget)
        self.stack_idx_d00 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_d00)


        #------ Cycle duration rates (2 nodes) ----------------------
        # self.cycle_dropdown.addItem("basic Ki67")   # 0 -> 1, 1 -> 0
        # self.cycle_dropdown.addItem("cycling quiescent") # 0 -> 1, 1 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration01 = QLineEdit()
        self.cycle_duration01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration10 = QLineEdit()
        self.cycle_duration10.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration10, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration10_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration10_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        # glayout.addWidget(QLabel(""), 2,0,1,1) # w, row, column, rowspan, colspan

        #-------
        self.stack_d01.setLayout(glayout)

        idx_stacked_widget += 1
        print(" new stacked widget: d01 -------------> ",idx_stacked_widget)
        self.stack_idx_d01 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_d01)


        #------ Cycle duration (3 nodes) ----------------------
        # self.cycle_dropdown.addItem("advanced Ki67")  # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry") # 0 -> 1, 1 -> 2, 2 -> 0

        glayout = QGridLayout()

        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_02_01 = QLineEdit()
        self.cycle_duration_02_01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_02_01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_02_01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_02_01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_02_12 = QLineEdit()
        self.cycle_duration_02_12.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_02_12, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_02_12_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_02_12_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 2 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 2,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_02_20 = QLineEdit()
        self.cycle_duration_02_20.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_02_20, 2,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_02_20_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_02_20_fixed, 2,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 2,4,1,1) # w, row, column, rowspan, colspan

        #-----
        self.stack_d02.setLayout(glayout)

        idx_stacked_widget += 1
        print(" new stacked widget: d02 -------------> ",idx_stacked_widget)
        self.stack_idx_d02 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_d02) 


        #------ Cycle duration (4 nodes) ----------------------
        # self.cycle_dropdown.addItem("flow cytometry separated") # 0->1, 1->2, 2->3, 3->0

        glayout = QGridLayout()

        label = QLabel("phase 0 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 0,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_03_01 = QLineEdit()
        self.cycle_duration_03_01.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_03_01, 0,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_03_01_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_03_01_fixed, 0,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 0,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 1 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 1,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_03_12 = QLineEdit()
        self.cycle_duration_03_12.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_03_12, 1,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_03_12_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_03_12_fixed, 1,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 1,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 2 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 2,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_03_23 = QLineEdit()
        self.cycle_duration_03_23.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_03_23, 2,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_03_23_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_03_23_fixed, 2,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 2,4,1,1) # w, row, column, rowspan, colspan

        #-------
        label = QLabel("phase 3 duration")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        glayout.addWidget(label, 3,0,1,1) # w, row, column, rowspan, colspan

        self.cycle_duration_03_30 = QLineEdit()
        self.cycle_duration_03_30.setValidator(QtGui.QDoubleValidator())
        glayout.addWidget(self.cycle_duration_03_30, 3,1,1,2) # w, row, column, rowspan, colspan

        self.cycle_duration_03_30_fixed = QCheckBox("Fixed")
        glayout.addWidget(self.cycle_duration_03_30_fixed, 3,3,1,1) # w, row, column, rowspan, colspan

        units = QLabel("min")
        units.setAlignment(QtCore.Qt.AlignCenter)
        units.setFixedWidth(units_width)
        glayout.addWidget(units, 3,4,1,1) # w, row, column, rowspan, colspan

        #-----
        self.stack_d03.setLayout(glayout)
        idx_stacked_widget += 1
        print(" new stacked widget: d03 -------------> ",idx_stacked_widget)
        self.stack_idx_d03 = idx_stacked_widget 
        self.stacked.addWidget(self.stack_d03)


        #---------------------------------------------
        # After adding all combos of cycle widgets (groups) to the stacked widget, 
        # add it to this panel.
        self.vbox.addWidget(self.stacked)

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
        # hbox = QHBoxLayout()
        # label = QLabel("phase 1 duration")
        # label.setFixedWidth(label_width)
        # label.setAlignment(QtCore.Qt.AlignRight)
        # hbox.addWidget(label)
        # self.apoptosis_phase1_duration = QLineEdit()
        # self.apoptosis_phase1_duration.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.apoptosis_phase1_duration)

        # self.apoptosis_phase1_duration_fixed = QCheckBox("Fixed")
        # hbox.addWidget(self.apoptosis_phase1_duration_fixed)

        # units = QLabel("min")
        # units.setFixedWidth(units_width)
        # units.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(units)
        # self.vbox.addLayout(hbox)

        # #-------
        # hbox = QHBoxLayout()
        # label = QLabel("phase 2 duration")
        # label.setFixedWidth(label_width)
        # label.setAlignment(QtCore.Qt.AlignRight)
        # hbox.addWidget(label)
        # self.apoptosis_phase2_duration = QLineEdit()
        # self.apoptosis_phase2_duration.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.apoptosis_phase2_duration)

        # self.apoptosis_phase2_duration_fixed = QCheckBox("Fixed")
        # hbox.addWidget(self.apoptosis_phase2_duration_fixed)

        # units = QLabel("min")
        # units.setFixedWidth(units_width)
        # units.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(units)
        # self.vbox.addLayout(hbox)

        # #-------
        # hbox = QHBoxLayout()
        # label = QLabel("phase 3 duration")
        # label.setFixedWidth(label_width)
        # label.setAlignment(QtCore.Qt.AlignRight)
        # hbox.addWidget(label)
        # self.apoptosis_phase3_duration = QLineEdit()
        # self.apoptosis_phase3_duration.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.apoptosis_phase3_duration)

        # self.apoptosis_phase3_duration_fixed = QCheckBox("Fixed")
        # hbox.addWidget(self.apoptosis_phase3_duration_fixed)

        # units = QLabel("min")
        # units.setFixedWidth(units_width)
        # units.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(units)
        # self.vbox.addLayout(hbox)

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
        # hbox = QHBoxLayout()
        # label = QLabel("phase 2 duration")
        # label.setFixedWidth(label_width)
        # label.setAlignment(QtCore.Qt.AlignRight)
        # hbox.addWidget(label)
        # self.necrosis_phase2_duration = QLineEdit()
        # self.necrosis_phase2_duration.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.necrosis_phase2_duration)

        # self.necrosis_phase2_duration_fixed = QCheckBox("Fixed")
        # hbox.addWidget(self.necrosis_phase2_duration_fixed)

        # units = QLabel("min")
        # units.setFixedWidth(units_width)
        # units.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(units)
        # self.vbox.addLayout(hbox)
        # #-----
        # hbox = QHBoxLayout()
        # label = QLabel("phase 3 duration")
        # label.setFixedWidth(label_width)
        # label.setAlignment(QtCore.Qt.AlignRight)
        # hbox.addWidget(label)
        # self.necrosis_phase3_duration = QLineEdit()
        # self.necrosis_phase3_duration.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.necrosis_phase3_duration)

        # self.necrosis_phase3_duration_fixed = QCheckBox("Fixed")
        # hbox.addWidget(self.necrosis_phase3_duration_fixed)

        # units = QLabel("min")
        # units.setFixedWidth(units_width)
        # units.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(units)
        # self.vbox.addLayout(hbox)

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
        self.motility_substrate_dropdown.currentIndexChanged.connect(self.motility_substrate_changed_cb)
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

        # cycle_path = ".//cell_definition[" + str(idx_current_cell_def) + "]//phenotype//cycle"
        # phase_transition_path = cycle_path + "//phase_transition_rates"
        # print(' >> phase_transition_path ')
        # pt_uep = uep.find(phase_transition_path)

        self.secretion_substrate_dropdown = QComboBox()
        self.secretion_substrate_dropdown.setFixedWidth(300)
        self.secretion_substrate_dropdown.currentIndexChanged.connect(self.secretion_substrate_changed_cb)
        self.vbox.addWidget(self.secretion_substrate_dropdown)

        # self.uep_cell_defs = self.xml_root.find(".//cell_definitions")
        # print('self.uep_cell_defs= ',self.uep_cell_defs)
        # # secretion_path = ".//cell_definition[" + str(idx_current_cell_def) + "]//phenotype//secretion//"
        # uep_secretion = self.xml_root.find(".//cell_definitions//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//secretion")
        # print('uep_secretion = ',uep_secretion )
        # # vp = []   # pointers to <variable> nodes
        # if self.uep_cell_defs:
        #     # uep = self.xml_root.find('.//secretion')  # find unique entry point
        #     idx = 0
        #     for sub in uep_secretion.findall('substrate'):
        #         # vp.append(var)
        #         print(idx,") -- secretion substrate = ",sub.attrib['name'])
        #         idx += 1

        # label = QLabel("oxygen")
        # label.setStyleSheet('background-color: lightgreen')
        # label.setFixedWidth(150)
        # self.vbox.addWidget(label)

        hbox = QHBoxLayout()
        label = QLabel("secretion rate")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.secretion_rate = QLineEdit()
        self.secretion_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_rate)
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
        self.secretion_target = QLineEdit()
        self.secretion_target.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.secretion_target)
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
        self.uptake_rate = QLineEdit()
        self.uptake_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.uptake_rate)
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

        #-------------------------
        custom_data_controls_hbox = QHBoxLayout()
        # self.new_button = QPushButton("New")
        self.new_button = QPushButton("Append 5 more rows")
        custom_data_controls_hbox.addWidget(self.new_button)
        self.new_button.clicked.connect(self.append_more_cb)

        self.clear_button = QPushButton("Clear selected rows")
        custom_data_controls_hbox.addWidget(self.clear_button)
        self.clear_button.clicked.connect(self.clear_rows_cb)

        self.vbox.addLayout(custom_data_controls_hbox)

        #-------------------------
        # Fixed names for columns:
        hbox = QHBoxLayout()
        # self.select = QtWidgets.QCheckBox("")
        w = QLabel("Name")
        w.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(w)
        # col2 = QtWidgets.QLabel("Type")
        # col2.setAlignment(QtCore.Qt.AlignCenter)
        # hbox.addWidget(col2)
        w = QLabel("Value (double)")
        w.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(w)
        w = QLabel("Units")
        w.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(w)
        # label.setFixedWidth(180)
        self.vbox.addLayout(hbox)


                # Create lists for the various input boxes
        self.custom_data_select = []
        self.custom_data_name = []
        self.custom_data_value = []
        self.custom_data_units = []

        for idx in range(10):   # rwh/TODO - this should depend on how many in the .xml
            # self.main_layout.addLayout(NewUserParam(self))
            hbox = QHBoxLayout()
            w = QCheckBox("")
            self.custom_data_select.append(w)
            hbox.addWidget(w)

            w = QLineEdit()
            self.custom_data_name.append(w)
            # self.name.setValidator(QtGui.QDoubleValidator())
            # self.diffusion_coef.enter.connect(self.save_xml)
            hbox.addWidget(w)
            # if idx == 0:
            #     w.setText("random_seed")

            w = QLineEdit()
            self.custom_data_value.append(w)
            # w.setValidator(QtGui.QDoubleValidator())
            # if idx == 0:
            #     w.setText("0")
            hbox.addWidget(w)

            w = QLineEdit()
            w.setFixedWidth(self.custom_data_units_width)
            self.custom_data_units.append(w)
            hbox.addWidget(w)

            # units = QtWidgets.QLabel("micron^2/min")
            # units.setFixedWidth(units_width)
            # hbox.addWidget(units)
            self.vbox.addLayout(hbox)
            # self.vbox.addLayout(hbox)
            # self.vbox.addLayout(hbox)
            self.custom_data_count = self.custom_data_count + 1

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

        self.layout.addLayout(controls_hbox)

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
        self.customize_cycle_choices()
        # QMessageBox.information(self, "Cycle Changed:",
                #   "Current Cycle Index: %d" % idx )

    @QtCore.Slot()
    def motility_substrate_changed_cb(self, idx):
        print('------ motility_substrate_changed_cb(): idx = ',idx)
        print(self.motility_substrate_dropdown.currentText())

    @QtCore.Slot()
    def secretion_substrate_changed_cb(self, idx):
        print('------ secretion_substrate_changed_cb(): idx = ',idx)
        print(self.secretion_substrate_dropdown.currentText())

        # uep = self.xml_root.find('.//microenvironment_setup')  # find unique entry point
        secretion_substrate_path = self.xml_root.find(".//cell_definitions//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//secretion//substrate[" + str(idx+1) + "]")
        if (secretion_substrate_path):
            print(secretion_substrate_path)

        # <substrate name="virus">
        #     <secretion_rate units="1/min">0</secretion_rate>
        #     <secretion_target units="substrate density">1</secretion_target>
        #     <uptake_rate units="1/min">10</uptake_rate>
        #     <net_export_rate units="total substrate/min">0</net_export_rate> 
        # </substrate> 
        # uep = self.xml_root.find(".//cell_definitions//cell_definition")
        # print(" secretion_rate=", secretion_substrate_path.find('.//secretion_rate').text ) 
        self.secretion_rate.setText(secretion_substrate_path.find(".//secretion_rate").text)
        self.secretion_target.setText(secretion_substrate_path.find(".//secretion_target").text)
        self.uptake_rate.setText(secretion_substrate_path.find(".//uptake_rate").text)
        self.secretion_net_export_rate.setText(secretion_substrate_path.find(".//net_export_rate").text)


        # self.cycle_dropdown.addItem("live cells")   # 0 -> 0
        # self.cycle_dropdown.addItem("basic Ki67")   # 0 -> 1, 1 -> 0
        # self.cycle_dropdown.addItem("advanced Ki67")  # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry") # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry separated") # 0->1, 1->2, 2->3, 3->0
        # self.cycle_dropdown.addItem("cycling quiescent") # 0 -> 1, 1 -> 0
    def cycle_phase_transition_cb(self):
        # rb1.toggled.connect(self.updateLabel)(self, idx_choice):
        # print('self.cycle_rows_vbox.count()=', self.cycle_rows_vbox.count())
        print('cycle_phase_transition_cb: self.stacked.count()=', self.stacked.count())

        radioBtn = self.sender()
        if radioBtn.isChecked():
            print("--------- ",radioBtn.text())

        print("self.cycle_dropdown.currentText() = ",self.cycle_dropdown.currentText())
        print("self.cycle_dropdown.currentIndex() = ",self.cycle_dropdown.currentIndex())

        # self.cycle_rows_vbox.clear()
        # if radioBtn.text().find("duration"):
        if "duration" in radioBtn.text():
            print('cycle_phase_transition_cb: --> duration')
            self.cycle_duration_flag = True
            self.customize_cycle_choices()
        else:  # transition rates
            print('cycle_phase_transition_cb: NOT duration')
            self.cycle_duration_flag = False
            self.customize_cycle_choices()
            # pass
        

        # self.cycle_dropdown.addItem("live cells")   # 0 -> 0
        # self.cycle_dropdown.addItem("basic Ki67")   # 0 -> 1, 1 -> 0
        # self.cycle_dropdown.addItem("advanced Ki67")  # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry") # 0 -> 1, 1 -> 2, 2 -> 0
        # self.cycle_dropdown.addItem("flow cytometry separated") # 0->1, 1->2, 2->3, 3->0
        # self.cycle_dropdown.addItem("cycling quiescent") # 0 -> 1, 1 -> 0
    def customize_cycle_choices(self):

        if self.cycle_duration_flag:  # specifying duration times (radio button)
            if self.cycle_dropdown.currentIndex() == 0:  # live
                print("customize_cycle_choices():  idx = ",self.stack_idx_d00)
                self.stacked.setCurrentIndex(self.stack_idx_d00)
            elif (self.cycle_dropdown.currentIndex() == 1) or (self.cycle_dropdown.currentIndex() == 5):  # basic Ki67 or cycling quiescent
                print("customize_cycle_choices():  idx = ",self.stack_idx_d01)
                self.stacked.setCurrentIndex(self.stack_idx_d01)
            elif (self.cycle_dropdown.currentIndex() == 2) or (self.cycle_dropdown.currentIndex() == 3):  # advanced Ki67 or flow cytometry
                print("customize_cycle_choices():  idx = ",self.stack_idx_d02)
                self.stacked.setCurrentIndex(self.stack_idx_d02)
            elif (self.cycle_dropdown.currentIndex() == 4):  # flow cytometry separated
                print("customize_cycle_choices():  idx = ",self.stack_idx_d03)
                self.stacked.setCurrentIndex(self.stack_idx_d03)

        else:  # specifying transition rates (radio button)
            if self.cycle_dropdown.currentIndex() == 0:  # live
                print("customize_cycle_choices():  idx = ",self.stack_idx_t00)
                self.stacked.setCurrentIndex(self.stack_idx_t00)
            elif (self.cycle_dropdown.currentIndex() == 1) or (self.cycle_dropdown.currentIndex() == 5):  # basic Ki67 or cycling quiescent
                print("customize_cycle_choices():  idx = ",self.stack_idx_t01)
                self.stacked.setCurrentIndex(self.stack_idx_t01)
            elif (self.cycle_dropdown.currentIndex() == 2) or (self.cycle_dropdown.currentIndex() == 3):  # advanced Ki67 or flow cytometry
                print("customize_cycle_choices():  idx = ",self.stack_idx_t02)
                self.stacked.setCurrentIndex(self.stack_idx_t02)
            elif (self.cycle_dropdown.currentIndex() == 4):  # flow cytometry separated
                print("customize_cycle_choices():  idx = ",self.stack_idx_t03)
                self.stacked.setCurrentIndex(self.stack_idx_t03)

    @QtCore.Slot()
    def clear_rows_cb(self):
        print("----- clearing all selected rows")

    @QtCore.Slot()
    def append_more_cb(self):
        for idx in range(5):
            # self.main_layout.addLayout(NewUserParam(self))
            hbox = QHBoxLayout()
            w = QCheckBox("")
            self.custom_data_select.append(w)
            hbox.addWidget(w)

            w = QLineEdit()
            self.custom_data_name.append(w)
            hbox.addWidget(w)

            w = QLineEdit()
            self.custom_data_value.append(w)
            # w.setValidator(QtGui.QDoubleValidator())
            hbox.addWidget(w)

            w = QLineEdit()
            w.setFixedWidth(self.custom_data_units_width)
            self.custom_data_units.append(w)
            hbox.addWidget(w)

            self.vbox.addLayout(hbox)
            # self.main_layout.addLayout(hbox)
            self.custom_data_count = self.custom_data_count + 1
            print(self.custom_data_count)

    #---------------------------------
    # def fill_motility_substrates(self):
    def fill_substrates_comboboxes(self):
        print("------- fill_substrates_comboboxes")
        self.motility_substrate_dropdown.clear()
        self.secretion_substrate_dropdown.clear()
        uep = self.xml_root.find('.//microenvironment_setup')  # find unique entry point
        # vp = []   # pointers to <variable> nodes
        if uep:
            idx = 0
            for var in uep.findall('variable'):
                # vp.append(var)
                print(" --> ",var.attrib['name'])
                name = var.attrib['name']
                self.motility_substrate_dropdown.addItem(name)
                self.secretion_substrate_dropdown.addItem(name)

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

        print('--------- fill_gui: cell_def_name=',cell_def_name)
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

        self.idx_current_cell_def = idx + 1  # we use 1-offset indices below 

        cycle_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//cycle"
        cycle_code = int(uep.find(cycle_path).attrib['code'])
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

        if cycle_code == 0:
            self.cycle_dropdown.setCurrentIndex(2)
        elif cycle_code == 1:
            self.cycle_dropdown.setCurrentIndex(1)
        elif cycle_code == 2:
            self.cycle_dropdown.setCurrentIndex(3)
        elif cycle_code == 5:
            self.cycle_dropdown.setCurrentIndex(0)
        elif cycle_code == 6:
            self.cycle_dropdown.setCurrentIndex(4)
        elif cycle_code == 7:
            self.cycle_dropdown.setCurrentIndex(5)

		# <cell_definition name="cargo cell" ID="2" visible="true">
		# 	<phenotype>
		# 		<cycle code="5" name="live">  
		# 			<phase_transition_rates units="1/min"> 
		# 				<rate start_index="0" end_index="0" fixed_duration="false">0.0</rate>
		# 			</phase_transition_rates>
        phase_transition_path = cycle_path + "//phase_transition_rates"
        print(' >> phase_transition_path ')
        pt_uep = uep.find(phase_transition_path)
        if pt_uep:
            # self.rb1 = QRadioButton("transition rate(s)", self)
            self.rb1.setChecked(True)
            for rate in pt_uep: 
                print(rate)
                print("start_index=",rate.attrib["start_index"])
                if (rate.attrib['start_index'] == "0") and (rate.attrib['end_index'] == "0"):
                    self.cycle_trate00.setText(rate.text)
                elif (rate.attrib['start_index'] == "0") and (rate.attrib['end_index'] == "1"):
                    self.cycle_trate01.setText(rate.text)
                elif (rate.attrib['start_index'] == "1") and (rate.attrib['end_index'] == "2"):
                    self.cycle_trate12.setText(rate.text)
                elif (rate.attrib['start_index'] == "2") and (rate.attrib['end_index'] == "3"):
                    self.cycle_trate23.setText(rate.text)
                elif (rate.attrib['start_index'] == "3") and (rate.attrib['end_index'] == "0"):
                    self.cycle_trate30.setText(rate.text)


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
            self.rb2.setChecked(True)
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

        death_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//death//"
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
                # elif  pd.attrib['index'] == "1":
                #     self.apoptosis_phase1_duration.setText(pd.text)
                # elif  pd.attrib['index'] == "2":
                #     self.apoptosis_phase2_duration.setText(pd.text)
                # elif  pd.attrib['index'] == "3":
                #     self.apoptosis_phase3_duration.setText(pd.text)

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
                # elif  pd.attrib['index'] == "2":
                #     self.necrosis_phase2_duration.setText(pd.text)
                # elif  pd.attrib['index'] == "3":
                #     self.necrosis_phase3_duration.setText(pd.text)

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

        volume_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//volume//"
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

				# <mechanics> 
				# 	<cell_cell_adhesion_strength units="micron/min">0.4</cell_cell_adhesion_strength>
				# 	<cell_cell_repulsion_strength units="micron/min">10.0</cell_cell_repulsion_strength>
				# 	<relative_maximum_adhesion_distance units="dimensionless">1.25</relative_maximum_adhesion_distance>
					
				# 	<options>
				# 		<set_relative_equilibrium_distance enabled="false" units="dimensionless">1.8</set_relative_equilibrium_distance>
				# 		<set_absolute_equilibrium_distance enabled="false" units="micron">15.12</set_absolute_equilibrium_distance>
				# 	</options>

        # # ---------  mechanics 
        mechanics_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//mechanics//"
        print('mechanics_path=',mechanics_path)

        self.cell_cell_adhesion_strength.setText(uep.find(mechanics_path+"cell_cell_adhesion_strength").text)
        self.cell_cell_repulsion_strength.setText(uep.find(mechanics_path+"cell_cell_repulsion_strength").text)
        self.relative_maximum_adhesion_distance.setText(uep.find(mechanics_path+"relative_maximum_adhesion_distance").text)

        mechanics_options_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//mechanics//options//"
        self.set_relative_equilibrium_distance.setText(uep.find(mechanics_options_path+"set_relative_equilibrium_distance").text)
        self.set_absolute_equilibrium_distance.setText(uep.find(mechanics_options_path+"set_absolute_equilibrium_distance").text)

        if uep.find(mechanics_options_path+"set_relative_equilibrium_distance").attrib['enabled'].lower() == 'true':
            self.set_relative_equilibrium_distance_enabled.setChecked(True)
        else:
            self.set_relative_equilibrium_distance_enabled.setChecked(False)

        if uep.find(mechanics_options_path+"set_absolute_equilibrium_distance").attrib['enabled'].lower() == 'true':
            self.set_absolute_equilibrium_distance_enabled.setChecked(True)
        else:
            self.set_absolute_equilibrium_distance_enabled.setChecked(False)

        # self.float24.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_adhesion_strength').text)
        # self.float25.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        # self.float26.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        # self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        # self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))


				# <motility>  
				# 	<speed units="micron/min">5.0</speed>
				# 	<persistence_time units="min">5.0</persistence_time>
				# 	<migration_bias units="dimensionless">0.5</migration_bias>
					
				# 	<options>
				# 		<enabled>true</enabled>
				# 		<use_2D>true</use_2D>
				# 		<chemotaxis>
				# 			<enabled>false</enabled>
				# 			<substrate>director signal</substrate>
				# 			<direction>1</direction>
				# 		</chemotaxis>
				# 	</options>

        # # ---------  motility 
        motility_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//motility//"
        print('motility_path=',motility_path)

        self.speed.setText(uep.find(motility_path+"speed").text)
        self.persistence_time.setText(uep.find(motility_path+"persistence_time").text)
        self.migration_bias.setText(uep.find(motility_path+"migration_bias").text)

        motility_options_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//motility//options//"

        # print(' motility options enabled', uep.find(motility_options_path +'enabled').text)
        if uep.find(motility_options_path +'enabled').text.lower() == 'true':
            self.motility_enabled.setChecked(True)
        else:
            self.motility_enabled.setChecked(False)

        if uep.find(motility_options_path +'use_2D').text.lower() == 'true':
            self.motility_2D.setChecked(True)
        else:
            self.motility_2D.setChecked(False)


        # # ---------  secretion 

        # <substrate name="virus">
        #     <secretion_rate units="1/min">0</secretion_rate>
        #     <secretion_target units="substrate density">1</secretion_target>
        #     <uptake_rate units="1/min">10</uptake_rate>
        #     <net_export_rate units="total substrate/min">0</net_export_rate> 
        # </substrate> 

        secretion_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//secretion//"
        print('secretion_path =',secretion_path)
        secretion_sub1_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//secretion//substrate[1]//"


        # if self.uep_cell_defs:
        # self.uep_cell_defs = self.xml_root.find(".//cell_definitions")
        # print('self.uep_cell_defs= ',self.uep_cell_defs)
        # # secretion_path = ".//cell_definition[" + str(idx_current_cell_def) + "]//phenotype//secretion//"
        uep_secretion = self.xml_root.find(".//cell_definitions//cell_definition[" + str(self.idx_current_cell_def) + "]//phenotype//secretion")
        print('uep_secretion = ',uep_secretion )
        
        self.secretion_rate_val.clear()
        self.secretion_target_val.clear()
        self.secretion_uptake_rate_val.clear()
        self.secretion_net_export_rate_val.clear()
        idx = 0
        for sub in uep_secretion.findall('substrate'):
            print(idx,") -- secretion substrate = ",sub.attrib['name'])
            self.secretion_rate_val.append(sub.find("secretion_rate").text)
            self.secretion_target_val.append(sub.find("secretion_target").text)
            self.secretion_uptake_rate_val.append(sub.find("uptake_rate").text)
            self.secretion_net_export_rate_val.append(sub.find("net_export_rate").text)
            idx += 1


        self.secretion_rate.setText(self.secretion_rate_val[0])
        self.secretion_target.setText(self.secretion_target_val[0])
        self.uptake_rate.setText(self.secretion_uptake_rate_val[0])
        self.secretion_net_export_rate.setText(self.secretion_net_export_rate_val[0])

        # # ---------  molecular 


        # # ---------  custom data 
        # <custom_data>  
        # 	<receptor units="dimensionless">0.0</receptor>
        # 	<cargo_release_o2_threshold units="mmHg">10</cargo_release_o2_threshold>

        uep_custom_data = self.xml_root.find(".//cell_definitions//cell_definition[" + str(self.idx_current_cell_def) + "]//custom_data")
        # custom_data_path = ".//cell_definition[" + str(self.idx_current_cell_def) + "]//custom_data//"
        print('uep_custom_data=',uep_custom_data)

        idx = 0
        # rwh/TODO: if we have more vars than we initially created rows for, we'll need
        # to call 'append_more_cb' for the excess.
        for var in uep_custom_data:
            print(idx, ") ",var)
            self.custom_data_name[idx].setText(var.tag)
            print("tag=",var.tag)
            self.custom_data_value[idx].setText(var.text)

            if 'units' in var.keys():
                self.custom_data_units[idx].setText(var.attrib['units'])
            idx += 1


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
        # self.apoptosis_phase1_duration.setText('')
        # self.apoptosis_phase2_duration.setText('')
        # self.apoptosis_phase3_duration.setText('')
        self.apoptosis_unlysed_rate.setText('')
        self.apoptosis_lysed_rate.setText('')
        self.apoptosis_cytoplasmic_biomass_change_rate.setText('')
        self.apoptosis_nuclear_biomass_change_rate.setText('')
        self.apoptosis_calcification_rate.setText('')
        self.apoptosis_relative_rupture_volume.setText('')
        self.necrosis_death_rate.setText('')
        self.necrosis_phase0_duration.setText('')
        self.necrosis_phase1_duration.setText('')
        # self.necrosis_phase2_duration.setText('')
        # self.necrosis_phase3_duration.setText('')
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
        self.secretion_rate.setText('')
        self.secretion_target.setText('')
        self.uptake_rate.setText('')
        self.secretion_net_export_rate.setText('')
