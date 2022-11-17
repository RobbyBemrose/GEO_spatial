#R. Bemrose
#Date: 07/01/2022
#perform reclass
 
# Import arcpy module
import arcpy
 
f = r\\...shp
 
#arcpy.AddField_management(f, "out", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
 
fields = ["RANK","length","R_x_L"]
with arcpy.da.UpdateCursor(f, fields) as cursor:
    for row in cursor: #step through each row
        if row[0] == "1":
                row[2] = 1 * row[1]
        elif row[0] == "2":
                row[2] = 1 * row[1]
        elif row[0] == "3":
                row[2] = 0.50 * row[1]
        elif row[0] == "4":
                row[2] = 0.25 * row[1]
        elif row[0] == "5":
                row[2] = 0.125 * row[1]
        cursor.updateRow(row) #save

