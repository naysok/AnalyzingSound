import bpy
import csv

filePath = '/Users/yoshionao_mbp/Documents/AnalyzingSound/data/Cluster_A_30.csv'

f = open(filePath, "r")
reader = csv.reader(f)
# header = next(reader)

bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
cube = bpy.data.objects[bpy.context.object.name]


# for loop 内で、無駄な行空け NG

for i, row in enumerate(reader):
    # print(row)
    if (i > 0):

        size = abs(float(row[2]))*1.25 + 0.1
        rot = float(row[2])*0.5
        cube.scale.x = size
        cube.scale.y = size
        cube.scale.z = size
        cube.keyframe_insert(data_path = "scale", index=0, frame=i)
        cube.keyframe_insert(data_path = "scale", index=1, frame=i)
        cube.keyframe_insert(data_path = "scale", index=2, frame=i)
        # cube.rotation_euler.z = rot
        cube.rotation_euler.z = float(row[1])*0.005
        cube.keyframe_insert(data_path = "rotation_euler", index=2, frame=i)
