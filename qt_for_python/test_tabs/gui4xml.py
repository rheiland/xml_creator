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
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogNoButton')))
        self.grid = QGridLayout()
        lay.addLayout(self.grid)
        self.setLayout(lay)
        self.setMinimumSize(400, 320)

        # self.menubar = QtWidgets.QMenuBar(self)
        # self.file_menu = QtWidgets.QMenu('File')
        # self.file_menu.insertAction("Open")
        # self.menubar.addMenu(self.file_menu)

        # GUI tabs
        self.tab1 = Config()
        self.tab2 = SubstrateDef()
        self.tab3 = CellDef()

        self.addTab(self.tab1,"Config Basics")
        self.addTab(self.tab2,"Microenvironment")
        self.addTab(self.tab3,"Cell Types")


    def menu(self):
        menubar = QMenuBar(self)

        file_menu = menubar.addMenu('File')
        open_act = QtGui.QAction('Open', self)
        biorobots = QtGui.QAction('Load biorobots', self)
        save_act = QtGui.QAction('Save', self)
        saveas_act = QtGui.QAction('Save As', self)
        # open_act = QtGui.QAction('Open', self, checkable=True)
        file_menu.setStatusTip('enable/disable Dark mode')
        file_menu.addAction(open_act)
        file_menu.addAction(biorobots)
        file_menu.addAction(save_act)
        file_menu.addAction(saveas_act)

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