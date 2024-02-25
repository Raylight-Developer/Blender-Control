try: from .Drivers import *
except: from Drivers import*
if TYPE_CHECKING:
	from Drivers import *

class HBox(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
		self.Linear_Layout.setSpacing(5)
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def hbox(self) -> 'HBox':
		hbox = HBox()
		self.uid = hbox.setUID(self.uid)
		self.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox()
		self.uid = vbox.setUID(self.uid)
		self.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List()
		self.uid = list.setUID(self.uid)
		self.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree()
		self.uid = tree.setUID(self.uid)
		self.addWidget(tree)
		return tree
	def driver(self, type: DRIVER_Type, window = None) -> Union[I_DRIVER, F_DRIVER, B_DRIVER, E_DRIVER, P_DRIVER]:
		if type == DRIVER_Type.I:
			driver = I_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.F:
			driver = F_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.B:
			driver = B_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.E:
			driver = E_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.P:
			driver = P_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		if window: window.Properties.append(driver)
		return driver

class VBox(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Linear_Layout.setSpacing(5)
		#self.setStyleName("Box")
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def hbox(self) -> 'HBox':
		hbox = HBox()
		self.uid = hbox.setUID(self.uid)
		self.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox()
		self.uid = vbox.setUID(self.uid)
		self.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List()
		self.uid = list.setUID(self.uid)
		self.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree()
		self.uid = tree.setUID(self.uid)
		self.addWidget(tree)
		return tree
	def driver(self, type: DRIVER_Type, window = None) -> Union[I_DRIVER, F_DRIVER, B_DRIVER, E_DRIVER, P_DRIVER]:
		if type == DRIVER_Type.I:
			driver = I_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.F:
			driver = F_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.B:
			driver = B_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.E:
			driver = E_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		elif type == DRIVER_Type.P:
			driver = P_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.addWidget(driver)
		if window: window.Properties.append(driver)
		return driver

class List(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText("").setToolTip("").setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
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
		self.uid = super().setUID(uid)
		return self.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def hbox(self) -> 'HBox':
		hbox = HBox()
		self.uid = hbox.setUID(self.uid)
		self.Container.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox()
		self.uid = vbox.setUID(self.uid)
		self.Container.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List()
		self.uid = list.setUID(self.uid)
		self.Container.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree()
		self.uid = tree.setUID(self.uid)
		self.Container.addWidget(tree)
		return tree
	def driver(self, type: DRIVER_Type, window = None) -> Union[I_DRIVER, F_DRIVER, B_DRIVER, E_DRIVER, P_DRIVER]:
		if type == DRIVER_Type.I:
			driver = I_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.F:
			driver = F_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.B:
			driver = B_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.E:
			driver = E_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.P:
			driver = P_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		if window: window.Properties.append(driver)
		return driver

class Tree(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
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
		self.uid = super().setUID(uid)
		return self.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_DOWN.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))
	def hbox(self) -> 'HBox':
		hbox = HBox()
		self.uid = hbox.setUID(self.uid)
		self.Container.addWidget(hbox)
		return hbox
	def vbox(self) -> 'VBox':
		vbox = VBox()
		self.uid = vbox.setUID(self.uid)
		self.Container.addWidget(vbox)
		return vbox
	def list(self) -> 'List':
		list = List()
		self.uid = list.setUID(self.uid)
		self.Container.addWidget(list)
		return list
	def tree(self) -> 'Tree':
		tree = Tree()
		self.uid = tree.setUID(self.uid)
		self.Container.addWidget(tree)
		return tree
	def driver(self, type: DRIVER_Type, window = None) -> Union[I_DRIVER, F_DRIVER, B_DRIVER, E_DRIVER, P_DRIVER]:
		if type == DRIVER_Type.I:
			driver = I_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.F:
			driver = F_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.B:
			driver = B_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.E:
			driver = E_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		elif type == DRIVER_Type.P:
			driver = P_DRIVER()
			self.uid = driver.setUID(self.uid)
			self.Container.addWidget(driver)
		if window: window.Properties.append(driver)
		return driver