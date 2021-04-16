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
from PySide6.QtWidgets import QFrame,QApplication,QWidget,QTabWidget,QFormLayout,QLineEdit, QHBoxLayout,QVBoxLayout,QRadioButton,QLabel,QCheckBox,QComboBox, QMenuBar,QStyle,QGridLayout, QTreeWidgetItem

from config_tab import Config
from cell_def_tab import CellDef 
from microenv_tab import SubstrateDef 
from user_params_tab import UserParams 
  
class PhysiCellXMLCreator(QTabWidget):
    def __init__(self, parent = None):
        super(PhysiCellXMLCreator, self).__init__(parent)

        self.title_prefix = "PhysiCell model configuration: "
        self.setWindowTitle(self.title_prefix)

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

        # By default, let's startup the app with a default of template2D (a copy)
        # self.new_model_cb()  # default on startup
        config_file = "config_samples/template2D_flat.xml"
        config_file = "config_samples/subcellular_flat.xml"
        config_file = "config_samples/cancer_biorobots_flat.xml"
        tree = ET.parse(config_file)
        self.xml_root = tree.getroot()

        self.num_models = 0
        self.model = {}  # key: name, value:[read-only, tree]

        self.config_tab = Config()
        self.config_tab.xml_root = self.xml_root
        self.config_tab.fill_gui()

        self.microenv_tab = SubstrateDef()
        self.microenv_tab.xml_root = self.xml_root
        substrate_name = self.microenv_tab.first_substrate_name()
        print("gui4xml: substrate_name=",substrate_name)
        self.microenv_tab.fill_gui(substrate_name)
        self.microenv_tab.populate_tree()

        # self.tab2.tree.setCurrentItem(QTreeWidgetItem,0)  # item

        self.celldef_tab = CellDef()
        self.celldef_tab.xml_root = self.xml_root
        cd_name = self.celldef_tab.first_cell_def_name()
        print("gui4xml: cd_name=",cd_name)
        self.celldef_tab.fill_gui(cd_name)
        self.celldef_tab.populate_tree()
        self.celldef_tab.fill_substrates_comboboxes()

        self.microenv_tab.celldef_tab = self.celldef_tab
        
        self.user_params_tab = UserParams()
        self.user_params_tab.xml_root = self.xml_root
        self.user_params_tab.fill_gui()

        #------------------
        self.addTab(self.config_tab,"Config Basics")
        self.addTab(self.microenv_tab,"Microenvironment")
        self.addTab(self.celldef_tab,"Cell Types")
        self.addTab(self.user_params_tab,"User Params")

        self.setCurrentIndex(2)  # debug: display the Cell Types tab on startup


    def menu(self):
        menubar = QMenuBar(self)

        #--------------
        file_menu = menubar.addMenu('File')

        # open_act = QtGui.QAction('Open', self, checkable=True)
        open_act = QtGui.QAction('Open', self)
        # recent_act = QtGui.QAction('Recent', self)
        save_act = QtGui.QAction('Save', self)
        saveas_act = QtGui.QAction('Save As my.xml', self)
        saveas_act.triggered.connect(self.save_as_cb)

        # file_menu.setStatusTip('enable/disable Dark mode')
        new_model_act = QtGui.QAction('New (template 2D)', self)
        file_menu.addAction(new_model_act)
        new_model_act.triggered.connect(self.new_model_cb)

        #--------------
        samples_menu = file_menu.addMenu("Samples (read-only)")
        biorobots_act = QtGui.QAction('biorobots', self)
        samples_menu.addAction(biorobots_act)
        biorobots_act.triggered.connect(self.biorobots_cb)

        cancer_biorobots_act = QtGui.QAction('cancer biorobots', self)
        samples_menu.addAction(cancer_biorobots_act)
        cancer_biorobots_act.triggered.connect(self.cancer_biorobots_cb)

        hetero_act = QtGui.QAction('heterogeneity', self)
        samples_menu.addAction(hetero_act)
        hetero_act.triggered.connect(self.hetero_cb)

        pred_prey_act = QtGui.QAction('predator-prey-farmer', self)
        samples_menu.addAction(pred_prey_act)
        pred_prey_act.triggered.connect(self.pred_prey_cb)

        virus_mac_act = QtGui.QAction('virus-macrophage', self)
        samples_menu.addAction(virus_mac_act)
        virus_mac_act.triggered.connect(self.virus_mac_cb)

        worm_act = QtGui.QAction('worm', self)
        samples_menu.addAction(worm_act)
        worm_act.triggered.connect(self.worm_cb)

        cancer_immune_act = QtGui.QAction('cancer immune (3D)', self)
        samples_menu.addAction(cancer_immune_act)
        cancer_immune_act.triggered.connect(self.cancer_immune_cb)

        template3D_act = QtGui.QAction('template (3D)', self)
        samples_menu.addAction(template3D_act)
        template3D_act.triggered.connect(self.template3D_cb)

        subcell_act = QtGui.QAction('subcellular', self)
        samples_menu.addAction(subcell_act)
        subcell_act.triggered.connect(self.subcell_cb)

        #--------------
        file_menu.addAction(open_act)
        # file_menu.addAction(recent_act)
        file_menu.addAction(save_act)
        file_menu.addAction(saveas_act)


        #--------------
        self.models_menu = menubar.addMenu('Models')
        models_menu_act = QtGui.QAction('-----', self)
        self.models_menu.addAction(models_menu_act)
        models_menu_act.triggered.connect(self.select_current_model_cb)
        # self.models_menu.addAction('Load sample', self.select_current_model_cb)

        #--------------
        tools_menu = menubar.addMenu('Tools')
        tools_menu_act = QtGui.QAction('Validate', self)
        tools_menu.addAction(tools_menu_act)

    #-----------------------------------------------------------------
    def add_new_model(self, name, read_only):
        # does it already exist? If so, return
        if name in self.model.keys():
            return
        self.model[name] = read_only
        self.num_models += 1
        print(" self.model (dict)= ",self.model)

        models_menu_act = QtGui.QAction(name, self)
        self.models_menu.addAction(models_menu_act)
        models_menu_act.triggered.connect(self.select_current_model_cb)

        self.setWindowTitle(self.title_prefix + name)

    def select_current_model_cb(self):
        # models_menu_act = QtGui.QAction(name, self)
        # self.models_menu.addAction(models_menu_act)
        model_act = self.models_menu.menuAction()
        print('select_current_model_cb: ',model_act)
        action = self.sender()
        model_name = action.text()
        print('select_current_model_cb: name= ',model_name)

        self.setWindowTitle(self.title_prefix + model_name)

    def reset_xml_root(self):
        self.xml_root = self.tree.getroot()
        self.config_tab.xml_root = self.xml_root
        self.microenv_tab.xml_root = self.xml_root
        self.celldef_tab.xml_root = self.xml_root

        self.config_tab.fill_gui()

        self.microenv_tab.clear_gui()
        self.microenv_tab.populate_tree()
        self.microenv_tab.fill_gui(None)

        self.celldef_tab.clear_gui()
        self.celldef_tab.populate_tree()
        self.celldef_tab.fill_gui(None)
        self.celldef_tab.fill_substrates_comboboxes()

    def show_sample_model(self):
        # self.config_file = "config_samples/biorobots.xml"
        self.tree = ET.parse(self.config_file)
        # self.xml_root = self.tree.getroot()
        self.reset_xml_root()
        # self.config_tab.fill_gui(self.xml_root)  # 
        # self.microenv_tab.fill_gui(self.xml_root)  # microenv
        # self.celldef_tab.fill_gui("foobar")  # cell defs
        # self.celldef_tab.fill_motility_substrates()

    def save_as_cb(self):
        self.microenv_tab.fill_xml()

    def new_model_cb(self):
        name = "copy_template2D"
        self.add_new_model(name, False)
        self.config_file = "config_samples/template2D_flat.xml"
        self.show_sample_model()

    def biorobots_cb(self):
        name = "biorobots_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

        # self.tree = ET.parse(self.config_file)
        # self.xml_root = self.tree.getroot()
        # self.celldef_tab.xml_root = self.xml_root
        # self.config_tab.fill_gui(self.xml_root)
        # self.microenv_tab.fill_gui(self.xml_root)
        # self.celldef_tab.fill_gui(self.xml_root)

    def cancer_biorobots_cb(self):
        name = "cancer_biorobots_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def hetero_cb(self):
        name = "heterogeneity"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def pred_prey_cb(self):
        name = "pred_prey_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def virus_mac_cb(self):
        name = "virus_macrophage_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()
        # self.tree = ET.parse(self.config_file)
        # self.xml_root = self.tree.getroot()
        # self.tab1.fill_gui(self.xml_root)
        # self.tab2.fill_gui(self.xml_root)

    def worm_cb(self):
        name = "worm"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def cancer_immune_cb(self):
        name = "cancer_immune3D_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def template3D_cb(self):
        name = "template3D_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

    def subcell_cb(self):
        name = "subcellular_flat"
        self.add_new_model(name, True)
        self.config_file = "config_samples/" + name + ".xml"
        self.show_sample_model()

		
def main():
    app = QApplication(sys.argv)
    ex = PhysiCellXMLCreator()
    ex.setGeometry(100,100, 800,600)
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()