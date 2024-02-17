from Window_Env import *

def processUI(main):
	super(Standalone_Window, main).processUI()

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

Standalone_Window.processUI = processUI
Test_Window = Standalone_Window()