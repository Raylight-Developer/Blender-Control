from Window_Env import *

class Testing_Window(DRIVER_Program_Window):
	def __init__(self):
		App = QApplication()
		super().__init__()
		sys.exit(App.exec())

	def processUI(main):
		super().processUI()

		# TEST YOUR CODE HERE ---------------------------------------------------------------------
		hbox : HBox     = main.hbox()
		test : F_DRIVER = main.driver(DRIVER_Type.F)
		hbox : HBox     = main.hbox()
		list : List     = main.list()
		test : I_DRIVER = list.driver(DRIVER_Type.I)
		test : B_DRIVER = list.driver(DRIVER_Type.B)
		test : F_DRIVER = list.driver(DRIVER_Type.F)
		test : E_DRIVER = list.driver(DRIVER_Type.E)
		test : P_DRIVER = list.driver(DRIVER_Type.P)
		hbox : HBox     = list.hbox()
		list : List     = hbox.list()
		test : E_DRIVER = list.driver(DRIVER_Type.E)
		# -----------------------------------------------------------------------------------------
		main.restore()

Window = Testing_Window()