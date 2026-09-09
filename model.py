import bpy

# 最初から入っているCube等を削除
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# テストモデル
bpy.ops.mesh.primitive_ico_sphere_add(
    subdivisions=3,
    radius=1.0,
    location=(0, 0, 0)
)

obj = bpy.context.object
obj.name = "TestModel"

# 少し縦長にする
obj.scale = (1.0, 1.0, 1.4)
bpy.ops.object.transform_apply(
    location=False,
    rotation=False,
    scale=True
)

# Smooth shading
for polygon in obj.data.polygons:
    polygon.use_smooth = True

# Blend保存
bpy.ops.wm.save_as_mainfile(
    filepath="/tmp/model.blend"
)

# GLB保存
bpy.ops.export_scene.gltf(
    filepath="/tmp/model.glb",
    export_format='GLB'
)

print("MODEL BUILD COMPLETE")
