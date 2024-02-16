from Window_Env import *

class Testing_Window(DRIVER_Program_Window):
	def __init__(self):
		App = QApplication()
		super().__init__()
		sys.exit(App.exec())

	def processUI(layout):
		super().processUI()

		# TEST YOUR CODE HERE ---------------------------------------------------------------------
		row  : HBox     = layout.hbox()
		test : F_DRIVER = row.driver(DRIVER_Type.F)
		row  : HBox     = layout.hbox()
		list : List     = layout.list()
		test : I_DRIVER = list.driver(DRIVER_Type.I)
		test : B_DRIVER = list.driver(DRIVER_Type.B)
		test : F_DRIVER = list.driver(DRIVER_Type.F)
		test : E_DRIVER = list.driver(DRIVER_Type.E)
		row  : HBox     = list.hbox()
		list : List     = row.list()
		#list : Tree     = row.tree()
		test : E_DRIVER = list.driver(DRIVER_Type.E)
		# -----------------------------------------------------------------------------------------
		layout.restore()

Window = Testing_Window()