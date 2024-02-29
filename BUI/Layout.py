from .Drivers import *

class HBox(QT_Linear_Contents):
	def __init__(self, main):
		super().__init__()
		self.main = main
		self.Linear_Layout.setSpacing(5)
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
	def setUID(self, uid):
		self.main.uid = super().setUID(uid)
		return self.main.uid
	def hbox(self) -> 'HBox':
		hbox = HBox(self.main)
		self.main.uid = hbox.setUID(self.main.uid)
		self.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox(self.main)
		self.main.uid = vbox.setUID(self.main.uid)
		self.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List(self.main)
		self.main.uid = list.setUID(self.main.uid)
		self.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree(self.main)
		self.main.uid = tree.setUID(self.main.uid)
		self.addWidget(tree)
		return tree
	def i_driver(self) -> I_DRIVER:
		driver = I_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def f_driver(self) -> F_DRIVER:
		driver = F_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def b_driver(self) -> B_DRIVER:
		driver = B_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def e_driver(self) -> E_DRIVER:
		driver = E_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def p_driver(self) -> P_DRIVER:
		driver = P_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver

class VBox(QT_Linear_Contents):
	def __init__(self, main):
		super().__init__(True)
		self.main = main
		self.Linear_Layout.setSpacing(5)
		#self.setStyleName("Box")
	def setUID(self, uid):
		self.main.uid = super().setUID(uid)
		return self.main.uid
	def hbox(self) -> 'HBox':
		hbox = HBox(self.main)
		self.main.uid = hbox.setUID(self.main.uid)
		self.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox(self.main)
		self.main.uid = vbox.setUID(self.main.uid)
		self.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List(self.main)
		self.main.uid = list.setUID(self.main.uid)
		self.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree(self.main)
		self.main.uid = tree.setUID(self.main.uid)
		self.addWidget(tree)
		return tree
	def i_driver(self) -> I_DRIVER:
		driver = I_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def f_driver(self) -> F_DRIVER:
		driver = F_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def b_driver(self) -> B_DRIVER:
		driver = B_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def e_driver(self) -> E_DRIVER:
		driver = E_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def p_driver(self) -> P_DRIVER:
		driver = P_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.addWidget(driver)
		self.main.Properties.append(driver)
		return driver

class List(QT_Linear_Contents):
	def __init__(self, main):
		super().__init__(True)
		self.main = main
		self.Toggle = QT_Button().setStyleName("List_Dropdown").setText("").setToolTip("").setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		self.Container = QT_Scroll_Area().setStyleName("List_Scroll_Area").setContentsStyleName("List_Contents")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Toggle.clicked.connect(self.expandCollapse)
	def saveSettings(self) -> Dict:
		return { "state": self.Toggle.isChecked()}
	def restoreSettings(self, state: Dict):
		if state["state"]:
			self.Container.show()
			self.Toggle.setChecked(True)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		elif not state["state"] :
			self.Container.hide()
			self.Toggle.setChecked(False)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def setUID(self, uid):
		self.main.uid = super().setUID(uid)
		return self.main.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def hbox(self) -> 'HBox':
		hbox = HBox(self.main)
		self.main.uid = hbox.setUID(self.main.uid)
		self.Container.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox(self.main)
		self.main.uid = vbox.setUID(self.main.uid)
		self.Container.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List(self.main)
		self.main.uid = list.setUID(self.main.uid)
		self.Container.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree(self.main)
		self.main.uid = tree.setUID(self.main.uid)
		self.Container.addWidget(tree)
		return tree
	def i_driver(self) -> I_DRIVER:
		driver = I_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def f_driver(self) -> F_DRIVER:
		driver = F_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def b_driver(self) -> B_DRIVER:
		driver = B_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def e_driver(self) -> E_DRIVER:
		driver = E_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def p_driver(self) -> P_DRIVER:
		driver = P_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver

class Tree(QT_Linear_Contents):
	def __init__(self, main):
		super().__init__(True)
		self.main = main
		self.SearchBar = QT_Line_Editor().setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/Icons/Window/SEARCH.svg"))
		self.SearchBar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText("").setToolTip("").setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Container.addWidget(self.SearchBar)
		self.Toggle.clicked.connect(self.expandCollapse)
	def saveSettings(self) -> Dict:
		return { "state": self.Toggle.isChecked()}
	def restoreSettings(self, state: Dict):
		if state["state"]:
			self.Container.show()
			self.Toggle.setChecked(True)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		elif not state["state"] :
			self.Container.hide()
			self.Toggle.setChecked(False)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def setUID(self, uid):
		self.main.uid = super().setUID(uid)
		return self.main.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def hbox(self) -> 'HBox':
		hbox = HBox(self.main)
		self.main.uid = hbox.setUID(self.main.uid)
		self.Container.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox(self.main)
		self.main.uid = vbox.setUID(self.main.uid)
		self.Container.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List(self.main)
		self.main.uid = list.setUID(self.main.uid)
		self.Container.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree(self.main)
		self.main.uid = tree.setUID(self.main.uid)
		self.Container.addWidget(tree)
		return tree
	def i_driver(self) -> I_DRIVER:
		driver = I_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def f_driver(self) -> F_DRIVER:
		driver = F_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def b_driver(self) -> B_DRIVER:
		driver = B_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def e_driver(self) -> E_DRIVER:
		driver = E_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver
	def p_driver(self) -> P_DRIVER:
		driver = P_DRIVER()
		self.main.uid = driver.setUID(self.main.uid)
		self.Container.addWidget(driver)
		self.main.Properties.append(driver)
		return driver