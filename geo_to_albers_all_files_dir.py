#R. Bemrose
#Date: 20/12/2021
#project from geo to Albers for all .shp files in all sub dir
 
import arcpy
from arcpy import env
import os
 
for dirname, dirnames, filenames in os.walk(r"\\..."):
    for subdirname in dirnames:
        #print os.path.join(dirname, subdirname)
        env.workspace = os.path.join(dirname, subdirname)
        mydir = env.workspace
        for filename in os.listdir(mydir):
            if filename.endswith(".shp"):
                print(os.path.join(mydir, filename))
            else:
                continue
 
            #input
            input_features = filename
 
            #output
            output_feature_class = str(filename.rsplit(".",1)[0]) + "_prj"
 
            #create a spatial reference object for the output coordinate system
            SrOut = r"\\...prj"
  
            #project
            arcpy.Project_management(input_features, output_feature_class, SrOut)

