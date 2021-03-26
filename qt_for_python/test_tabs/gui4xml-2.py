"""
=========================================================================================
  Parse a PhysiCell configuration file (XML) and generate a Jupyter (Python) module for 'Cell Types' GUI tab.
  
==========================================================================================
 
  Example  use:
  ------------
    python gui4xml.py
    python gui4xml.py biorobots.xml
  
  Outputs
  -------
    Save an XML file representing the data in the GUI.
 
Authors:
Randy Heiland (heiland@iu.edu)
Dr. Paul Macklin (macklinp@iu.edu)

--- Versions ---
0.1 - initial version

"""

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFrame


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class Cell_Types_Tab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.vbox_cell_def = QtWidgets.QVBoxLayout()

        QtWidgets.QLabel('Phenotype: cycle')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: death')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: volume')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: mechanics')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: motility')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: secretion')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)
#        -----------
        QtWidgets.QLabel('Phenotype: molecular')
        label.setStyleSheet('background-color: orange')
        self.vbox_cell_def.addWidget(label)

        return self.vbox_cell_def


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # global self.params_cell_def

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
        self.tabs.currentChanged.connect(self.tab_changed_cb)

        #-------------------------------------------
        self.vbox_config = QtWidgets.QVBoxLayout()
        self.vbox_microenv = QtWidgets.QVBoxLayout()
        self.vbox_user_params = QtWidgets.QVBoxLayout()

        #-------------------------------------------
        self.scroll = QtWidgets.QScrollArea()  # might contain centralWidget

        self.params_cell_def = QtWidgets.QWidget()
        self.vbox_cell_def = QtWidgets.QVBoxLayout()

        self.params_config = QtWidgets.QWidget()
        self.vbox_config = QtWidgets.QVBoxLayout()

        self.cycle_dropdown = QtWidgets.QComboBox()

        self.cycle_dropdown.addItem("advanced Ki67")
        self.cycle_dropdown.addItem("basic Ki67")
        self.cycle_dropdown.addItem("flow cytometry")
        self.cycle_dropdown.addItem("live apoptotic")
        self.cycle_dropdown.addItem("total cells")
        self.cycle_dropdown.addItem("live cells")
        self.cycle_dropdown.addItem("flow cytometry separated")
        self.cycle_dropdown.addItem("cycling quiescent")

        self.vbox_cell_def.addWidget(self.cycle_dropdown)

        #=====  Phenotype 
        #============  Cycle ================================
        label = QtWidgets.QLabel("Phenotype: cycle")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 0->0 transition rate")
        hbox.addWidget(label)

        self.cycle_trate0_0 = QtWidgets.QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_0)

        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 0->1 transition rate")
        hbox.addWidget(label)

        self.cycle_trate0_1 = QtWidgets.QLineEdit()
        # self.cycle_trate0_1.setValidator(QtGui.QIntValidator())
        self.cycle_trate0_1.setValidator(QtGui.QDoubleValidator())
        # self.cycle_trate0_1.enter.connect(self.save_xml)
        hbox.addWidget(self.cycle_trate0_1)

        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 1->2 transition rate")
        hbox.addWidget(label)

        self.cycle_trate1_2 = QtWidgets.QLineEdit()
        self.cycle_trate1_2.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate1_2)

        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 2->3 transition rate")
        hbox.addWidget(label)

        self.cycle_trate2_3 = QtWidgets.QLineEdit()
        self.cycle_trate2_3.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate2_3)

        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)
        #----------
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Phase 3->4 transition rate")
        hbox.addWidget(label)

        self.cycle_trate3_4 = QtWidgets.QLineEdit()
        self.cycle_trate3_4.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.cycle_trate3_4)

        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        # self.vbox_cell_def.addWidget(QHLine())
        #--------------------------
        # hbox = QtWidgets.QHBoxLayout()
        # label = QtWidgets.QLabel("Phase0->Phase0 transition rate")
        # hbox.addWidget(label)

        # self.cycle_trate0_0 = QtWidgets.QLineEdit()
        # self.cycle_trate0_0.setValidator(QtGui.QDoubleValidator())
        # hbox.addWidget(self.cycle_trate0_0)

        # units = QtWidgets.QLabel("1/min")
        # hbox.addWidget(units)
        # self.vbox_cell_def.addLayout(hbox)

        #--------------------------
        # self.vbox_cell_def.addWidget(QHLine())


        # self.vbox_cell_def.addLayout(hbox)
        #----------
        #============  Death ================================
        label = QtWidgets.QLabel("Phenotype: death")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())

        #-----
        label = QtWidgets.QLabel("Apoptosis")
        label.setStyleSheet('background-color: yellow')
        self.vbox_cell_def.addWidget(label)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("death rate")
        hbox.addWidget(label)
        self.death_apop_rate = QtWidgets.QLineEdit()
        self.death_apop_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.death_apop_rate)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("phase 0 duration")
        hbox.addWidget(label)
        self.phase0_duration = QtWidgets.QLineEdit()
        self.phase0_duration.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.phase0_duration)
        units = QtWidgets.QLabel("min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        # <phase_durations units="min">
        #     <duration index="0" fixed_duration="true">516</duration>

        # <unlysed_fluid_change_rate units="1/min">0.05</unlysed_fluid_change_rate>
        # <lysed_fluid_change_rate units="1/min">0</lysed_fluid_change_rate>
        # <cytoplasmic_biomass_change_rate units="1/min">1.66667e-02</cytoplasmic_biomass_change_rate>
        # <nuclear_biomass_change_rate units="1/min">5.83333e-03</nuclear_biomass_change_rate>
        # <calcification_rate units="1/min">0</calcification_rate>
        # <relative_rupture_volume units="dimensionless">2.0</relative_rupture_volume>
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("unlysed_fluid_change_rate")
        hbox.addWidget(label)
        self.apoptosis_unlysed_rate = QtWidgets.QLineEdit()
        self.apoptosis_unlysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_unlysed_rate)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("lysed_fluid_change_rate")
        hbox.addWidget(label)
        self.apoptosis_lysed_rate = QtWidgets.QLineEdit()
        self.apoptosis_lysed_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_lysed_rate)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("cytoplasmic_biomass_change_rate")
        hbox.addWidget(label)
        self.apoptosis_cytoplasmic_biomass_change_rate = QtWidgets.QLineEdit()
        self.apoptosis_cytoplasmic_biomass_change_rate.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.apoptosis_cytoplasmic_biomass_change_rate)
        units = QtWidgets.QLabel("1/min")
        hbox.addWidget(units)
        self.vbox_cell_def.addLayout(hbox)

        #-----
        # self.vbox_cell_def.addWidget(QHLine())
        label = QtWidgets.QLabel("Necrosis")
        label.setStyleSheet('background-color: yellow')
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())
        #============  Volume ================================
        label = QtWidgets.QLabel("Phenotype: volume")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())
        #============  Mechanics ================================
        label = QtWidgets.QLabel("Phenotype: mechanics")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())
        #============  Motility ================================
        label = QtWidgets.QLabel("Phenotype: motility")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())
        #============  Secretion ================================
        label = QtWidgets.QLabel("Phenotype: secretion")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())
        #============  Molecular ================================
        label = QtWidgets.QLabel("Phenotype: molecular")
        label.setStyleSheet("background-color: orange")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())

        #=====  Custom data 
        label = QtWidgets.QLabel("Custom data")
        label.setStyleSheet("background-color: cyan")
        self.vbox_cell_def.addWidget(label)
        # self.vbox_cell_def.addWidget(QHLine())

        #==================================================================
        self.params_cell_def.setLayout(self.vbox_cell_def)

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
        self.layout.addWidget(self.scroll)
        # self.layout.addWidget(self.vbox_cell_def)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.save_button)

        self.save_button.clicked.connect(self.save_xml)


    @QtCore.Slot()
    def save_xml(self):
        # self.text.setText(random.choice(self.hello))
        pass

    @QtCore.Slot()
    def tab_changed_cb(self, idx):
        # self.text.setText(random.choice(self.hello))
        # pass
        QtWidgets.QMessageBox.information(self, "Tab Index Changed!",
                  "Current Tab Index: %d" % idx )
        # if idx == 2:
        #     self.scroll.setWidget(self.params_cell_def)
        # else:
        #     self.scroll.setWidget(self.params_config)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(500, 600)
    widget.show()

    sys.exit(app.exec_())

