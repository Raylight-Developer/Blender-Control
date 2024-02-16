from Window_Env import *

class Testing_Window(DRIVER_Program_Window):
	def __init__(self):
		App = QApplication()
		super().__init__()
		sys.exit(App.exec())

	def processUI(layout):
		super().processUI()

		# TEST YOUR CODE HERE ---------------------------------------------------------------------
		row     : Row           = layout.row()
		test    : FloatProperty = row.prop(Prop_Type.FLOAT)
		row     : Row           = layout.row()
		dropdown: Dropdown      = layout.dropdown()
		test    : IntProperty   = dropdown.prop(Prop_Type.INT)
		test    : BoolProperty  = dropdown.prop(Prop_Type.BOOL)
		test    : FloatProperty = dropdown.prop(Prop_Type.FLOAT)
		test    : EnumProperty  = dropdown.prop(Prop_Type.ENUM)
		row     : Row           = dropdown.row()
		dropdown: Dropdown      = row.dropdown()
		list    : Search_List   = row.list()
		test    : EnumProperty  = list.prop(Prop_Type.ENUM)
		# -----------------------------------------------------------------------------------------
		layout.restore()

Window = Testing_Window()