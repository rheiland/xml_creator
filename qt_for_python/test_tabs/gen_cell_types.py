import xmltodict as x2d

fname = 'biorobots.xml'
fname = 'virus_macrophage.xml'
with open(fname) as xml:
    doc = x2d.parse(xml.read())

indent8 = '        '
cells_tab_file = "cell_types_skeleton.py"
fp= open(cells_tab_file, 'w')

dl = list(doc.items())

cell_defs = dl[0][1]['cell_definitions']
print('# of cell_defs = ',len(cell_defs['cell_definition']))

# In [15]: (cell_defs['cell_definition'][0]['phenotype'])['cycle']
# Out[15]: 
# OrderedDict([('@code', '5'),
#              ('@name', 'live'),
#              ('phase_transition_rates',
#               OrderedDict([('@units', '1/min'),
#                            ('rate',
#                             OrderedDict([('@start_index', '0'),
#                                          ('@end_index', '0'),
#                                          ('@fixed_duration', 'false'),
#                                          ('#text', '0.0')]))]))])

#In [10]: len(cell_defs['cell_definition'][0]['phenotype'])
#Out[10]: 7

#In [14]: (cell_defs['cell_definition'][0]['phenotype']).keys()
#Out[14]: odict_keys(['cycle', 'death', 'volume', 'mechanics', 'motility', 'secretion', 'molecular'])

# In [23]: pheno_parts = list((cell_defs['cell_definition'][0]['phenotype']).keys())
# In [24]: pheno_parts
# Out[24]: ['cycle', 'death', 'volume', 'mechanics', 'motility', 'secretion', 'molecular']
pheno_parts = list((cell_defs['cell_definition'][0]['phenotype']).keys())
        # label = QtWidgets.QLabel("Phenotype: cycle")
        # label.setStyleSheet("background-color: orange")
        # self.vbox_cell_def.addWidget(label)
for pp in pheno_parts:
    fp.write("#        -----------\n")
    print("---------- pp=",pp)
    lstr = indent8 + "label = QtWidgets.QLabel('Phenotype: " + pp + "')\n"
    fp.write(lstr)
    lstr = indent8 + "label.setStyleSheet('background-color: orange')\n"
    fp.write(lstr)
    lstr = indent8 + "self.vbox_cell_def.addWidget(label)\n"
    fp.write(lstr)

    if pp == 'cycle':
        for rate in (cell_defs['cell_definition'][0]['phenotype'])['cycle']['phase_transition_rates']['rate']:
            # print('rate=',rate)  # , type(rate)
            # print('start_index = ',rate['@start_index'])
            fp.write('\n')
            lstr = indent8 + "hbox = QtWidgets.QHBoxLayout()\n"
            fp.write(lstr)
            lstr = indent8 + "label = QtWidgets.QLabel('Phase: " + rate['@start_index'] + '->' + rate['@end_index'] + " rate')\n"
            fp.write(lstr)
            lstr = indent8 + "hbox.addWidget(label)\n"
            fp.write(lstr)
            #--------
            objname = "self.cycle_trate"+ rate['@start_index'] + '_' + rate['@end_index']
            lstr = indent8 + objname + " = QtWidgets.QLineEdit()\n"
            fp.write(lstr)
            lstr = indent8 + objname + ".setValidator(QtGui.QDoubleValidator())\n"
            fp.write(lstr)
            lstr = indent8 + "hbox.addWidget(" + objname + ")\n"
            fp.write(lstr)

            #--------
            lstr = indent8 + "label = 1/min\n"
            fp.write(lstr)
            lstr = indent8 + "hbox.addWidget(label)\n"
            fp.write(lstr)

            lstr = indent8 + "self.vbox_cell_def.addLayout(hbox)\n"
            fp.write(lstr)
        fp.write("#        -----------\n")

        # self.cycle1_trate0_1 = QtWidgets.QLineEdit()
        # # self.cycle1_trate0_1.setValidator(QtGui.QIntValidator())
        # self.cycle1_trate0_1.setValidator(QtGui.QDoubleValidator())
        # # self.cycle1_trate0_1.enter.connect(self.save_xml)
        # hbox.addWidget(self.cycle1_trate0_1)

# OrderedDict([('@start_index', '0'), ('@end_index', '1'), ('@fixed_duration', 'false'), ('#text', '0')])
# OrderedDict([('@start_index', '1'), ('@end_index', '2'), ('@fixed_duration', 'true'), ('#text', '0.00208333')])

#In [16]: (cell_defs['cell_definition'][0]['phenotype'])['cycle'].keys()
#Out[16]: odict_keys(['@code', '@name', 'phase_transition_rates'])

# In [17]: (cell_defs['cell_definition'][0]['phenotype'])['cycle']['phase_transition_rates']
# Out[17]: 
# OrderedDict([('@units', '1/min'),
#              ('rate',
#               OrderedDict([('@start_index', '0'),
#                            ('@end_index', '0'),
#                            ('@fixed_duration', 'false'),
#                            ('#text', '0.0')]))])


        # hbox = QtWidgets.QHBoxLayout()
        # label = QtWidgets.QLabel("Phase0->Phase1 transition rate")
        # hbox.addWidget(label)

        # self.cycle1_trate0_1 = QtWidgets.QLineEdit()
        # # self.cycle1_trate0_1.setValidator(QtGui.QIntValidator())
        # self.cycle1_trate0_1.setValidator(QtGui.QDoubleValidator())
        # # self.cycle1_trate0_1.enter.connect(self.save_xml)
        # hbox.addWidget(self.cycle1_trate0_1)

        # units = QtWidgets.QLabel("1/min")
        # hbox.addWidget(units)
        # self.vbox_cell_def.addLayout(hbox)
        #----------

# In [21]: (cell_defs['cell_definition'][0]['phenotype'])['cycle']['phase_transition_rates']['rate']
# Out[21]: 
# OrderedDict([('@start_index', '0'),
#              ('@end_index', '0'),
#              ('@fixed_duration', 'false'),
#              ('#text', '0.0')])

# In [22]: (cell_defs['cell_definition'][0]['phenotype'])['cycle']['phase_transition_rates']['rate']['@start_index']
# Out[22]: '0'




# Write the beginning of the Python module for the 'Cell Types' tab in the GUI
# cells_tab_file = "cells_def.py"
# cells_tab_file = "cell_types_skeleton.py"
# print("\n --------------------------------- ")
# print()
# fp= open(cells_tab_file, 'w')
#fp.write(cells_tab_header)
fp.close()
print("Generated a new: ", cells_tab_file)