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
        self.max_time.setFixedWidth(200)
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
        self.num_threads.setFixedWidth(value_width)
        self.num_threads.setValidator(QtGui.QIntValidator())
        hbox.addWidget(self.num_threads)

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
        label.setFixedHeight(300)
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
