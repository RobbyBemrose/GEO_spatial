#R. Bemrose
#Date: 05/07/2021
#Create 500 m x 500 m grid for each CMA using the 10 km x 10 km grid CMA extent
 
import arcpy
from arcpy import env
import os
 
#set working dir where files are saved
env.workspace = r"\\..."
 
#env.overwriteOutput = True
 
#create list of files in folder
ListFiles = arcpy.ListFeatureClasses()
 
###write all .shp (FC) files to .txt
txtFile = open(r"\\...*txt","w")
#loop over list of files
for fc in ListFiles:
    print fc
    txtFile.write(fc)
    txtFile.write(os.linesep)
txtFile.close()
print "saved .txt with filenames"
 
###generate .5 km x .5 km grid for each CMA shp grid(10 km x 10 km) saved in dir
#loop over files in list
for fc in ListFiles:
    print fc
    #add prefix to filename and remove .shp file ext
    out_fname = "500m_" + str(fc.rsplit(".",1)[0])
    #set coordinate system of the output fishnet using the same as the input .shp
    env.outputCoordinateSystem = arcpy.Describe(fc).spatialReference
    print out_fname
    #return describe object with extent properties
    desc = arcpy.Describe(fc)
    #create fishnet grid, set grid size 500 x 500, projection is in metres
    arcpy.CreateFishnet_management(out_fname,str(desc.extent.lowerLeft),str(desc.extent.XMin) + " " + str(desc.extent.YMax + 10),"500","500","0","0",str(desc.extent.upperRight),"NO_LABELS","#","POLYGON")
 
###clip .5 km x .5 km grid to shape of 10 km x 10 km grid
#loop over files in list
for fc in ListFiles:
    print fc
    #add prefix to filename
    in_fname = "500m_" + str(fc)
    #remove .shp ext from filename
    out_fnameClp = "500m_clip_" + str(fc.rsplit(".",1)[0])
    #set local variables, tolerance is blank
    xy_tolerance = ""
    #execute Clip
    arcpy.Clip_analysis(in_fname, fc, out_fnameClp, xy_tolerance)

