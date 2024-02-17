try: from .Layout import *
except: from Layout import *

try: import bpy
except: pass

class DRIVER_Program_Window(QT_Window):
	popout_pos = QPoint()
	initial_pos = QPoint()
	storeState = None
	def __init__(self):
		super().__init__()
		self.uid = 0
		self.uid = self.setUID(self.uid)
		self.mouse_pressed = False

		self.Popout_Mode = QT_Button().setStyleName("Bool_Prop").setCheckable(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/BOOKMARK.svg"))
		self.Popout_Mode.clicked.connect(self.popoutMode)
		self.uid = self.Popout_Mode.setUID(self.uid)

		self.Popout_Analyzer = QT_Floating_Button().setStyleName("Bool_Prop").setCheckable(True).setChecked(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/EXPAND.svg"))
		self.Popout_Analyzer.clicked.connect(self.popout)
		self.uid = self.Popout_Analyzer.setUID(self.uid)

		self.Pin_Analyzer = QT_Button().setStyleName("Bool_Prop").setCheckable(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/PINNED_OFF.svg"))
		self.Pin_Analyzer.clicked.connect(self.pin)
		self.uid = self.Pin_Analyzer.setUID(self.uid)

		self.Reload_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/REFRESH.svg"))
		self.Reload_Analyzer.clicked.connect(self.processUI)

		self.Exit_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/CLOSE.svg"))
		self.Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = HBox()
		self.BUI_Header.setContentsMargins(5,5,5,5)
		self.BUI_Header.setFixedHeight(34)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(self.Popout_Mode).addWidget(self.Pin_Analyzer).addWidget(self.Reload_Analyzer).addWidget(self.Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = VBox()
		self.uid = self.BUI_Layout.setUID(self.uid)
		self.BUI_Layout.setContentsMargins(5,5,5,5)
		self.Properties = []

		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter).setWindowTitle("DRIVER").setWindowIcon(QIcon(PATH+"/Resources/Icons/Data/SHAPEKEY_DATA.svg"))

		self.processUI()
		self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)
		self.show()

	def popoutMode(self, toggle):
		if toggle:
			self.Popout_Analyzer.show()
			self.Reload_Analyzer.hide()
			self.Exit_Analyzer.hide()
		else:
			self.Popout_Analyzer.hide()
			self.Reload_Analyzer.show()
			self.Exit_Analyzer.show()

	def popout(self, toggle):
		if toggle:
			self.Popout_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Window/COLLAPSE.svg"))
			self.show()
			self.restoreGeometry(self.storeState)
		else:
			self.Popout_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Window/EXPAND.svg"))
			self.storeState = self.saveGeometry()
			self.hide()

	def pin(self, toggle):
		if toggle:
			self.Pin_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/PINNED_ON.svg"))
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
		else:
			self.Pin_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/PINNED_OFF.svg"))
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
		self.show()

	def processUI(main):
		QApplication.instance().setStyleSheet(open(PATH+"/Resources/Stylesheet.css","r").read())
		main.BUI_Layout.clear()
		try:
			if not bpy.data.texts.get("DRIVER"):
				new_text_block = bpy.data.texts.new(name="DRIVER")
				new_text_block.write("hbox = main.hbox()")
			if not bpy.data.texts.get("DRIVER Settings"):
				new_text_block = bpy.data.texts.new(name="DRIVER Settings")
				new_text_block.write("{}")
			code: str = bpy.data.texts.get("DRIVER").as_string()
			code = code.replace('\"', '"')
			exec(code)
		except: pass
		for widget in main.Properties:
			try: widget.executeBlenderFetch()
			except Exception as err: print(err)
		main.restore()

	def eventFilter(self, source, event: QEvent | QMouseEvent | QKeyEvent):
		if source == self.BUI_Header and event.type() == QEvent.Type.MouseButtonPress:
			if event.button() == Qt.MouseButton.RightButton or event.button() == Qt.MouseButton.LeftButton:
				self.initial_pos =  event.globalPosition()
				self.mouse_pressed = True
		elif source == self.BUI_Header and event.type() == QEvent.Type.MouseMove and self.mouse_pressed:
			delta = event.globalPosition() - self.initial_pos
			pos = QPointF(self.pos()) + delta
			self.move(pos.x(), pos.y())
			self.initial_pos =  event.globalPosition()
		if event.type() == QEvent.Type.MouseButtonRelease and (event.button() == Qt.MouseButton.RightButton or event.button() == Qt.MouseButton.LeftButton):
			self.mouse_pressed = False
		return super().eventFilter(source, event)

	def mousePressEvent(self, event):
		focused_widget = QApplication.focusWidget()
		if isinstance(focused_widget, QT_Line_Editor):
			focused_widget.clearFocus()
		super().mousePressEvent(event)

	def focusInEvent(self, event: QFocusEvent):
		for widget in self.Properties:
			try: widget.executeBlenderFetch()
			except Exception as err: print(err)

	def quit(self):
		self.save()
		self.close()
		QCoreApplication.quit()
		QCoreApplication.exit()
		QCoreApplication.instance().quit()
		QCoreApplication.instance().exit()

	def saveState(self) -> Dict:
		return {"pos_x": self.pos().x(), "pos_y": self.pos().y(), "size_x": self.size().width(), "size_y": self.size().height()}

	def restoreState(self, state: Dict):
		self.move(state["pos_x"], state["pos_y"])
		self.resize(state["size_x"], state["size_y"])

	def restore(self):
		file = bpy.data.texts.get("DRIVER Settings")
		settings = json.loads(file.as_string())
		for widget in QCoreApplication.instance().allWidgets():
			if widget.whatsThis() != "":
				try:
					if isinstance(widget, List):
						widget: List = widget
						widget.restoreState(settings[f"Dropdown || {widget.whatsThis()}"])
					elif isinstance(widget, QT_Window):
						widget: QT_Window =  widget
						widget.restoreState(settings[f"QT_Window || {widget.whatsThis()}"])
				except: pass

	def save(self):
		settings = {}
		for widget in QCoreApplication.instance().allWidgets():
			if widget.whatsThis() != "":
				try:
					if isinstance(widget, List):
						widget: List = widget
						settings[f"Dropdown || {widget.whatsThis()}"] = widget.saveState()
					elif isinstance(widget, QT_Window):
						widget: QT_Window =  widget
						settings[f"QT_Window || {widget.whatsThis()}"] = widget.saveState()
				except: pass

		file = bpy.data.texts.get("DRIVER Settings")
		file.clear()
		file.write(json.dumps(settings))

	def hbox(self) -> HBox:
		row = self.BUI_Layout.hbox()
		return row
	def vbox(self) -> VBox:
		column = self.BUI_Layout.vbox()
		return column
	def list(self) -> List:
		list = self.BUI_Layout.list()
		return list
	def tree(self) -> Tree:
		tree = self.BUI_Layout.tree()
		return tree
	def driver(self, type: DRIVER_Type) -> Union[I_DRIVER, F_DRIVER, B_DRIVER, E_DRIVER, P_DRIVER]:
		driver = self.BUI_Layout.driver(type)
		self.uid = driver.setUID(self.uid)
		return driver

class Standalone_Window(DRIVER_Program_Window):
	def __init__(self):
		self.App = QApplication.instance()
		if self.App is None:
			self.App = QApplication(sys.argv)
		super().__init__()
		self.App.exec()

	def processUI(main):
		QApplication.instance().setStyleSheet(open(PATH+"/Resources/Stylesheet.css","r").read())
		main.BUI_Layout.clear()

	def restore(self): pass
		#if os.path.exists(PATH+"/Resources/BUI.json"):
		#	with open(PATH+"/Resources/BUI.json", "r", encoding = "utf-8") as file:
		#		settings = json.load(file)
		#		file.close()
#
		#for widget in QCoreApplication.instance().allWidgets():
		#	if widget.whatsThis() != "":
		#		try:
		#			if isinstance(widget, List):
		#				widget: List = widget
		#				widget.restoreState(settings[f"Dropdown || {widget.whatsThis()}"])
		#			elif isinstance(widget, QT_Window):
		#				widget: QT_Window =  widget
		#				widget.restoreState(settings[f"QT_Window || {widget.whatsThis()}"])
		#		except: pass

	def save(self): pass
		#settings = {}
		#for widget in QCoreApplication.instance().allWidgets():
		#	if widget.whatsThis() != "":
		#		try:
		#			if isinstance(widget, List):
		#				widget: List = widget
		#				settings[f"Dropdown || {widget.whatsThis()}"] = widget.saveState()
		#			elif isinstance(widget, QT_Window):
		#				widget: QT_Window =  widget
		#				settings[f"QT_Window || {widget.whatsThis()}"] = widget.saveState()
		#		except: pass
#
		#with open(PATH+"/Resources/BUI.json", "wt", encoding = "utf-8") as file:
		#	json.dump(settings, file)
		#	file.close()