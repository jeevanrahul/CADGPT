import ezdxf

file_path = r"C:\Users\welcome\Desktop\Drawing1.dxf"

try:
    doc = ezdxf.readfile(file_path)
    print("Loaded sucessfully")

except IOError:
    print("Not found")

except ezdxf.DXFStructureError:
    print("Invalid or Corrupted file")

msp = doc.modelspace()

print(f"Total drawing elements: {len(msp)}") #Count number of drawing

entity_types = set(entity.dxftype() for entity in msp)

print(f"Types of entites in the drawing: {entity_types}")

for entity in msp:
    if entity.dxftype() =="LWPOLYLINE":
        print("New Poluline: ")
        for point in entity:
            x,y = point[0], point[1]
            #print(f"Point: ({x}, {y})")


polylines = []
for entity in msp:
    if entity.dxftype() == "LWPOLYLINE":
        points = [(point[0], point[1]) for point in entity]
        polylines.append(points)
    
#print(polylines)

import math
import numpy as np

def edge_length(points):
    lengths = []
    n = len(points)
    for i in range(n):
        