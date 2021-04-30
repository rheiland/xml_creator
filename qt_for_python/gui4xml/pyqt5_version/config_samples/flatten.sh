python xml_hier2flat.py biorobots.xml
mv flat_xml_out.xml biorobots_flat.xml
sleep 1 

python xml_hier2flat.py cancer_biorobots.xml
mv flat_xml_out.xml cancer_biorobots_flat.xml

sleep 1
python xml_hier2flat.py cancer_immune3D.xml     
mv flat_xml_out.xml cancer_immune3D_flat.xml

sleep 1 
python xml_hier2flat.py pred_prey.xml
mv flat_xml_out.xml pred_prey_flat.xml

sleep 1 
python xml_hier2flat.py template2D.xml
mv flat_xml_out.xml template2D_flat.xml

sleep 1 
python xml_hier2flat.py template3D.xml
mv flat_xml_out.xml template3D_flat.xml

sleep 1 
python xml_hier2flat.py virus_macrophage.xml
mv flat_xml_out.xml virus_macrophage_flat.xml
