

cp ~/git/PhysiCell_dev_branch/sample_projects/template2D/config/PhysiCell_settings.xml template2D.xml
cp ~/git/PhysiCell_dev_branch/sample_projects/cancer_biorobots/config/PhysiCell_settings.xml cancer_biorobots.xml
cp ~/git/PhysiCell_dev_branch/sample_projects/heterogeneity/config/PhysiCell_settings.xml heterogeneity.xml
cp ~/git/PhysiCell_dev_branch/sample_projects/pred_prey_farmer/config/PhysiCell_settings.xml pred-prey.xml
cp ~/git/PhysiCell_dev_branch/sample_projects/cancer_immune/config/PhysiCell_settings.xml cancer_immune3D.xml
cp ~/git/PhysiCell_dev_branch/sample_projects/template3D/config/PhysiCell_settings.xml template3D.xml

-------------

~/git/xml_creator/qt_for_python/gui4xml/config_samples$ python flatten_cell_def_xml.py template2D.xml 
argc= 2

--- Phase 0: Build a Python dict, cell_def, that contains keys = name and values = {'ID':value, 'parent':value}
cell_defs = <Element 'cell_definitions' at 0x10c823d10>
{'name': 'tumor cell', 'ID': '0'}
{'name': 'motile tumor cell', 'ID': '1', 'parent_type': 'tumor cell'}
cell_defs_dict=  {'tumor cell': {'ID': '0', 'parent': None}, 'motile tumor cell': {'ID': '1', 'parent': 'tumor cell'}}

--- Phase 1: create a new .xml containing N copies of 'default' cell_definition, with desired names.
--- Remove all but root node (top cell_def)
removing  motile tumor cell
--- Insert duplicate root cell_def for of its children
   root_name =  tumor cell
[{'ID': '0', 'parent': None}, {'ID': '1', 'parent': 'tumor cell'}]
inserting child of  tumor cell
renaming child of  tumor cell  to be  motile tumor cell with ID  1
--->  tmp2.xml

mv tmp2.xml template2D_flat.xml
---------------

python xml_hier2flat.py biorobots.xml 
mv flat_xml_out.xml biorobots_flat.xml

python xml_hier2flat.py cancer_biorobots.xml 
mv flat_xml_out.xml cancer_biorobots_flat.xml

python xml_hier2flat.py cancer_immune3D.xml	
mv flat_xml_out.xml cancer_immune3D_flat.xml

python xml_hier2flat.py pred_prey.xml	
mv flat_xml_out.xml pred_prey_flat.xml

python xml_hier2flat.py template2D.xml	
mv flat_xml_out.xml template2D_flat.xml

python xml_hier2flat.py template3D.xml	
mv flat_xml_out.xml template3D_flat.xml

python xml_hier2flat.py virus_macrophage.xml
mv flat_xml_out.xml virus_macrophage_flat.xml

