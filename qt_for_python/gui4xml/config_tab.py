"""
Authors:
Randy Heiland (heiland@iu.edu)
Adam Morrow, Grant Waldrow, Drew Willis, Kim Crevecoeur
Dr. Paul Macklin (macklinp@iu.edu)

--- Versions ---
0.1 - initial version
"""

import sys
# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QFrame,QApplication,QWidget,QTabWidget,QFormLayout,QLineEdit, QHBoxLayout,QVBoxLayout,QRadioButton,QLabel,QCheckBox,QComboBox,QScrollArea
from PySide6.QtWidgets import QFrame

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

class Config(QWidget):
    def __init__(self):
        super().__init__()
        # global self.params_cell_def

        self.xml_root = None

        self.tab = QWidget()
        # self.tabs.resize(200,5)
        
        #-------------------------------------------
        label_width = 110
        domain_value_width = 100
        value_width = 60
        label_height = 20
        units_width = 70

        self.scroll = QScrollArea()  # might contain centralWidget

        self.params_cell_def = QWidget()
        self.vbox = QVBoxLayout()
        self.vbox.addStretch(0)


        #============  Domain ================================
        label = QLabel("Domain (micron)")
        label.setFixedHeight(label_height)
        label.setStyleSheet("background-color: orange")
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox.addWidget(label)

        hbox = QHBoxLayout()

        label = QLabel("Xmin")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.xmin = QLineEdit()
        self.xmin.setFixedWidth(domain_value_width)
        self.xmin.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.xmin)

        label = QLabel("Xmax")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.xmax = QLineEdit()
        self.xmax.setFixedWidth(domain_value_width)
        self.xmax.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.xmax)

        label = QLabel("dx")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.xdel = QLineEdit()
        self.xdel.setFixedWidth(value_width)
        self.xdel.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.xdel)

        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("Ymin")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.ymin = QLineEdit()
        self.ymin.setFixedWidth(domain_value_width)
        self.ymin.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.ymin)

        label = QLabel("Ymax")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.ymax = QLineEdit()
        self.ymax.setFixedWidth(domain_value_width)
        self.ymax.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.ymax)

        label = QLabel("dy")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.ydel = QLineEdit()
        self.ydel.setFixedWidth(value_width)
        self.ydel.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.ydel)

        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        label = QLabel("Zmin")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.zmin = QLineEdit()
        self.zmin.setFixedWidth(domain_value_width)
        self.zmin.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.zmin)

        label = QLabel("Zmax")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.zmax = QLineEdit()
        self.zmax.setFixedWidth(domain_value_width)
        self.zmax.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.zmax)

        label = QLabel("dz")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)
        self.zdel = QLineEdit()
        self.zdel.setFixedWidth(value_width)
        self.zdel.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.zdel)

        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()
        self.virtual_walls = QCheckBox("Virtual walls")
        # self.motility_enabled.setAlignment(QtCore.Qt.AlignRight)
        # label.setFixedWidth(label_width)
        hbox.addWidget(self.virtual_walls)
        self.vbox.addLayout(hbox)

        self.vbox.addWidget(QHLine())

        #----------
        hbox = QHBoxLayout()
        # hbox.setFixedHeight(label_width)

        label = QLabel("Max Time")
        # label_width = 210
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.max_time = QLineEdit()
        # self.max_time.setFixedWidth(200)
        self.max_time.setFixedWidth(domain_value_width)
        self.max_time.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.max_time)

        label = QLabel("min")
        label.setFixedWidth(units_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(label)

        self.vbox.addLayout(hbox)
        #----------
        hbox = QHBoxLayout()

        label = QLabel("# threads")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.num_threads = QLineEdit()
        # self.num_threads.setFixedWidth(value_width)
        self.num_threads.setFixedWidth(domain_value_width)
        self.num_threads.setValidator(QtGui.QIntValidator())
        hbox.addWidget(self.num_threads)

        label = QLabel("   ")
        label.setFixedWidth(units_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(label)

        self.vbox.addLayout(hbox)

        #------------------
        hbox = QHBoxLayout()

        label = QLabel("Save data:")
        label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(label)

        #------
        self.save_svg = QCheckBox("SVG")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.save_svg)

        label = QLabel("every")
        # label_width = 210
        # label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.svg_interval = QLineEdit()
        self.svg_interval.setFixedWidth(value_width)
        self.svg_interval.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.svg_interval)

        label = QLabel("min")
        # label.setFixedWidth(units_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(label)

        #------
        self.save_svg = QCheckBox("Full")
        # self.motility_2D.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(self.save_svg)

        label = QLabel("every")
        # label_width = 210
        # label.setFixedWidth(label_width)
        label.setAlignment(QtCore.Qt.AlignRight)
        hbox.addWidget(label)

        self.full_interval = QLineEdit()
        self.full_interval.setFixedWidth(value_width)
        self.full_interval.setValidator(QtGui.QDoubleValidator())
        hbox.addWidget(self.full_interval)

        label = QLabel("min")
        # label.setFixedWidth(units_width)
        label.setAlignment(QtCore.Qt.AlignLeft)
        hbox.addWidget(label)

        self.vbox.addLayout(hbox)

        #--------------
        self.cells_csv = QCheckBox("cells.csv")
        self.vbox.addWidget(self.cells_csv)

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

        self.layout = QVBoxLayout(self)

        self.layout.addWidget(self.scroll)


    # @QtCore.Slot()
    # def save_xml(self):
    #     # self.text.setText(random.choice(self.hello))
    #     pass


    def fill_gui(self):

        self.xmin.setText(self.xml_root.find(".//x_min").text)
        self.xmax.setText(self.xml_root.find(".//x_max").text)
        self.xdel.setText(self.xml_root.find(".//dx").text)

        self.ymin.setText(self.xml_root.find(".//y_min").text)
        self.ymax.setText(self.xml_root.find(".//y_max").text)
        self.ydel.setText(self.xml_root.find(".//dy").text)
    
        self.zmin.setText(self.xml_root.find(".//z_min").text)
        self.zmax.setText(self.xml_root.find(".//z_max").text)
        self.zdel.setText(self.xml_root.find(".//dz").text)
        
        self.max_time.setText(self.xml_root.find(".//max_time").text)
        
        self.num_threads.setText(self.xml_root.find(".//omp_num_threads").text)
        
        # if xml_root.find(".//full_data//enable").text.lower() == 'true':
        #     self.toggle_mcds.value = True
        # else:
        #     self.toggle_mcds.value = False
        self.full_interval.setText(self.xml_root.find(".//full_data//interval").text)

        # # NOTE: do this *after* filling the mcds_interval, directly above, due to the callback/constraints on them
        # if xml_root.find(".//SVG//enable").text.lower() == 'true':
        #     self.toggle_svg.value = True
        # else:
        #     self.toggle_svg.value = False
        self.svg_interval.setText(self.xml_root.find(".//SVG//interval").text)


    # Read values from the GUI widgets and generate/write a new XML
    def fill_xml(self):
        pass
        # TODO: verify valid type (numeric) and range?
        # xml_root.find(".//x_min").text = str(self.xmin.value)
        # xml_root.find(".//x_max").text = str(self.xmax.value)
        # xml_root.find(".//dx").text = str(self.xdelta.value)
        # xml_root.find(".//y_min").text = str(self.ymin.value)
        # xml_root.find(".//y_max").text = str(self.ymax.value)
        # xml_root.find(".//dy").text = str(self.ydelta.value)
        # xml_root.find(".//z_min").text = str(self.zmin.value)
        # xml_root.find(".//z_max").text = str(self.zmax.value)
        # xml_root.find(".//dz").text = str(self.zdelta.value)

        # xml_root.find(".//max_time").text = str(self.tmax.value)

        # xml_root.find(".//omp_num_threads").text = str(self.omp_threads.value)

        # xml_root.find(".//SVG").find(".//enable").text = str(self.toggle_svg.value)
        # xml_root.find(".//SVG").find(".//interval").text = str(self.svg_interval.value)
        # xml_root.find(".//full_data").find(".//enable").text = str(self.toggle_mcds.value)
        # xml_root.find(".//full_data").find(".//interval").text = str(self.mcds_interval.value)