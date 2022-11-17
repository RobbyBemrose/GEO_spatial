#R. Bemrose
#Date: 05/07/2021
#select 10 km x 10 km by location using intersect of CMAs
 
import arcpy
from arcpy import env
import os
 
#set working dir where files are saved
env.workspace = r"\\...\outline_CMA_shapes"
 
grid = r"\\...\10km_x_10km_frame.shp"
 
#create list of files in folder
ListFiles = arcpy.ListFeatureClasses()
print ListFiles
 
for fc in ListFiles:
    print fc
    arcpy.MakeFeatureLayer_management(grid, "gRIDlyr" + str(fc))
    sel = arcpy.SelectLayerByLocation_management("gRIDlyr" + str(fc),"INTERSECT",fc)
    out_fname = "CMA" + str(fc)
    arcpy.CopyFeatures_management(sel, out_fname)

