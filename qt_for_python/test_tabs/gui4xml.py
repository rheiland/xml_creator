# https://doc.qt.io/qtforpython/gettingstarted.html

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFrame,QApplication,QWidget,QTabWidget,QFormLayout,QLineEdit, QHBoxLayout,QVBoxLayout,QRadioButton,QLabel,QCheckBox,QComboBox

from config_tab import Config
from cell_def_tab import CellDef

  
class PhysiCellXMLCreator(QTabWidget):
    def __init__(self, parent = None):
        super(PhysiCellXMLCreator, self).__init__(parent)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        # self.tab3 = QWidget()
        self.tab1 = Config()
        self.tab3 = CellDef()

        self.addTab(self.tab1,"Config Basics")
        self.addTab(self.tab2,"Microenvironment")
        self.addTab(self.tab3,"Cell Defs")
        # self.tab_config()
        self.tab_microenv()
        # self.tab_cell_defs()
        self.setWindowTitle("PhysiCell configuration")
		
    def tab_microenv(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QLineEdit())
        # self.setTabText(1,"Microenvironment")
        self.tab2.setLayout(layout)

    @QtCore.Slot()
    def save_xml(self):
        # self.text.setText(random.choice(self.hello))
        pass

    @QtCore.Slot()
    def cycle_changed_cb(self, idx):
        pass
        # QtWidgets.QMessageBox.information(self, "Cycle Changed:",
                #   "Current Cycle Index: %d" % idx )

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

def main():
    app = QApplication(sys.argv)
    ex = PhysiCellXMLCreator()
    ex.setGeometry(100,100, 700,600)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()