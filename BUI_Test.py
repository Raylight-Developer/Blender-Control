from Window_Env import *
#-------------------------------------------------------------------------------------------------#
hbox : HBox     = main.hbox()
driv : F_DRIVER = main.driver(DRIVER_Type.F)
hbox : HBox     = main.hbox()
list : List     = main.list()
driv : I_DRIVER = list.driver(DRIVER_Type.I)
driv : F_DRIVER = list.driver(DRIVER_Type.F).setMin(-1)
driv : B_DRIVER = list.driver(DRIVER_Type.B)
driv : E_DRIVER = list.driver(DRIVER_Type.E)
driv : P_DRIVER = list.driver(DRIVER_Type.P)
list : List     = main.list()
driv : I_DRIVER = list.driver(DRIVER_Type.I).setLabelIcon(Icon.I_DRIVER)
driv : F_DRIVER = list.driver(DRIVER_Type.F).setLabelIcon(Icon.F_DRIVER)
driv : B_DRIVER = list.driver(DRIVER_Type.B).setLabelIcon(Icon.B_DRIVER)
driv : E_DRIVER = list.driver(DRIVER_Type.E).setLabelIcon(Icon.E_DRIVER)
driv : P_DRIVER = list.driver(DRIVER_Type.P).setLabelIcon(Icon.P_DRIVER)