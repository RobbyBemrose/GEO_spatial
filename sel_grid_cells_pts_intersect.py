#R. Bemrose
#Date: 21/12/2021
#select grid cells that pts intersect and save to file
 
import arcpy
from arcpy import env
import os
 
#set working dir where files are saved
mydir = r\\...
arcpy.env.workspace = mydir
 
###for each shapefile in dir
for fc in os.listdir(mydir):
    if fc.endswith(".shp"):
        print(os.path.join(mydir, fc))
    else:
        continue
 
    #1 km grid
    grid = r\\...shp
 
    arcpy.MakeFeatureLayer_management(grid, "gRIDsel" + str(fc))
 
    # Define Selection criteria
    Selection = arcpy.SelectLayerByLocation_management("gRIDsel" + str(fc), "INTERSECT", fc)
 
    #add prefix to output filename
    out_fname = str(fc.rsplit(".",1)[0]) + "_grid"
   
    # Define output selection and fc
    arcpy.CopyFeatures_management(Selection, out_fname)

