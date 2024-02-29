from Window_Env import *
#-------------------------------------------------------------------------------------------------#

list = main.list()
driv = list.i_driver().setMin(-5).setMax(5)
driv = list.f_driver().setMin(-1)
driv = list.b_driver()
driv = list.e_driver()
driv = list.p_driver()

list = main.list()
i_dr = list.i_driver().setLabelIcon(Icon.I_DRIVER)
f_dr = list.f_driver().setLabelIcon(Icon.F_DRIVER)
b_dr = list.b_driver().setLabelIcon(Icon.B_DRIVER)
e_dr = list.e_driver().setLabelIcon(Icon.E_DRIVER)
p_dr = list.p_driver().setLabelIcon(Icon.P_DRIVER)

list = main.list()
i_dr = list.i_driver().setLabel(None).setLabelIcon(Icon.I_DRIVER)
f_dr = list.f_driver().setLabel(None).setLabelIcon(Icon.F_DRIVER)
b_dr = list.b_driver().setLabel(None).setLabelIcon(Icon.B_DRIVER)
e_dr = list.e_driver().setLabel(None).setLabelIcon(Icon.E_DRIVER).addItems(["Item A","Item B","Item C"])
p_dr = list.p_driver().setLabel(None).setLabelIcon(Icon.P_DRIVER)