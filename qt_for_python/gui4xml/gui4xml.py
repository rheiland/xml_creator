"""
Authors:
Randy Heiland (heiland@iu.edu)
Adam Morrow, Grant Waldrow, Drew Willis, Kim Crevecoeur
Dr. Paul Macklin (macklinp@iu.edu)

--- Versions ---
0.1 - initial version
"""
# https://doc.qt.io/qtforpython/gettingstarted.html

import sys
import xml.etree.ElementTree as ET  # https://docs.python.org/2/library/xml.etree.elementtree.html

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFrame,QApplication,QWidget,QTabWidget,QFormLayout,QLineEdit, QHBoxLayout,QVBoxLayout,QRadioButton,QLabel,QCheckBox,QComboBox, QMenuBar,QStyle,QGridLayout 

from config_tab import Config
from cell_def_tab import CellDef 
from microenv_tab import SubstrateDef 

  
class PhysiCellXMLCreator(QTabWidget):
    def __init__(self, parent = None):
        super(PhysiCellXMLCreator, self).__init__(parent)

        self.setWindowTitle("PhysiCell configuration")

        # Menus
        lay = QVBoxLayout(self)
        lay.setContentsMargins(5, 35, 5, 5)
        self.menu()
        # self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogNoButton')))
        self.setWindowIcon(QtGui.QIcon('physicell_logo_25pct.png'))
        self.grid = QGridLayout()
        lay.addLayout(self.grid)
        self.setLayout(lay)
        self.setMinimumSize(400, 320)

        # self.menubar = QtWidgets.QMenuBar(self)
        # self.file_menu = QtWidgets.QMenu('File')
        # self.file_menu.insertAction("Open")
        # self.menubar.addMenu(self.file_menu)

        # GUI tabs
        config_file = "virus_macrophage.xml"
        config_file = "biorobots.xml"
        tree = ET.parse(config_file)
        xml_root = tree.getroot()

        self.tab1 = Config()
        self.tab1.fill_gui(xml_root)

        self.tab2 = SubstrateDef()
        self.tab2.fill_gui(xml_root)

        self.tab3 = CellDef()

        self.addTab(self.tab1,"Config Basics")
        self.addTab(self.tab2,"Microenvironment")
        self.addTab(self.tab3,"Cell Types")


    def biorobots(self):
        self.config_file = "biorobots.xml"
        self.tree = ET.parse(self.config_file)
        self.xml_root = self.tree.getroot()
        self.tab1.fill_gui(self.xml_root)
        self.tab2.fill_gui(self.xml_root)

    def virus_mac(self):
        self.config_file = "virus_macrophage.xml"
        self.tree = ET.parse(self.config_file)
        self.xml_root = self.tree.getroot()
        self.tab1.fill_gui(self.xml_root)
        self.tab2.fill_gui(self.xml_root)

    def menu(self):
        menubar = QMenuBar(self)

        file_menu = menubar.addMenu('File')
        # samples = QtGui.QAction('Load sample', self)

        save_act = QtGui.QAction('Save', self)
        saveas_act = QtGui.QAction('Save As', self)
        # open_act = QtGui.QAction('Open', self, checkable=True)

        # file_menu.setStatusTip('enable/disable Dark mode')
        new_act = QtGui.QAction('New (template 2D)', self)
        file_menu.addAction(new_act)

        samples_menu = file_menu.addMenu("Load sample")
        biorobots_act = QtGui.QAction('biorobots', self)
        samples_menu.addAction(biorobots_act)
        biorobots_act.triggered.connect(self.biorobots)

        cancer_biorobots_act = QtGui.QAction('cancer biorobots', self)
        samples_menu.addAction(cancer_biorobots_act)

        hetero_act = QtGui.QAction('heterogeneity', self)
        samples_menu.addAction(hetero_act)

        pred_prey_act = QtGui.QAction('predator-prey-farmer', self)
        samples_menu.addAction(pred_prey_act)

        virus_mac_act = QtGui.QAction('virus-macrophage', self)
        samples_menu.addAction(virus_mac_act)
        virus_mac_act.triggered.connect(self.virus_mac)

        worm_act = QtGui.QAction('worm', self)
        samples_menu.addAction(worm_act)
        cancer_immune_act = QtGui.QAction('cancer immune (3D)', self)
        samples_menu.addAction(cancer_immune_act)
        template3D_act = QtGui.QAction('template (3D)', self)
        samples_menu.addAction(template3D_act)

        file_menu.addAction(save_act)
        file_menu.addAction(saveas_act)


        # samples_menu = menubar.addMenu('Samples')
        # samples.addAction('Load sample', self)

        tools_menu = menubar.addMenu('Tools')
        email = QtGui.QAction('Validate', self)
        tools_menu.addAction(email)
		

def main():
    app = QApplication(sys.argv)
    ex = PhysiCellXMLCreator()
    ex.setGeometry(100,100, 800,600)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()