#R. Bemrose
#Date: 20/12/2021
#Create .shp files for each .csv file with x and y coords
 
import arcpy
from arcpy import env
import os
 
#set working dir where files are saved
mydir = r\\...
arcpy.env.workspace = mydir
 
###generate .shp files for each .csv in list
for filename in os.listdir(mydir):
    if filename.endswith(".csv"):
        print(os.path.join(mydir, filename))
    else:
        continue
 
    in_table = filename
    out_layer = str(filename.rsplit(".",1)[0]) + "_pts"
    saved_layer = mydir
    x_c = "long"
    y_c = "lat"
 
    # Set the spatial reference
    spREF = r\\...prj
   
    # Make the XY layer
    out = arcpy.MakeXYEventLayer_management(in_table, x_c, y_c, out_layer, spREF)
    print out
 
    # Print the total rows
    print(arcpy.GetCount_management(out_layer))
   
    # Copy features to shapefile
    arcpy.CopyFeatures_management(out_layer, out_layer)

