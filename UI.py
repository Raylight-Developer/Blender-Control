from BUI import *
layout = Column()
# LEAVE THE HEADER FOR TYPING

row : Row = layout.row()
test_slider: FloatProperty = row.prop(Type.FLOAT, "Test Slider")
test_slider.set_driver_expression('bpy.data.objects["Cube"].data.shape_keys.key_blocks["Example"].value = float(driver/100)')