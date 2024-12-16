from .Layout import *

class DRIVER_Program_Window(QT_Window):
	popout_pos = QPoint()
	initial_pos = QPoint()
	geometryStore: QByteArray = None
	BUI_Header: QT_Linear_Contents = None
	def __init__(self):
		super().__init__()
		self.uid = 0
		self.uid = self.setUID(self.uid)
		self.mouse_pressed = False

		self.Popout_Mode = QT_Button().setStyleName("Header_Button").setCheckable(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/WINDOW_BOOKMARK.svg"))
		self.Popout_Mode.clicked.connect(self.popoutMode)
		self.uid = self.Popout_Mode.setUID(self.uid)

		self.Popout_Analyzer = QT_Floating_Button().setStyleName("Header_Button").setCheckable(True).setChecked(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_EXPAND_ON.svg"))
		self.Popout_Analyzer.clicked.connect(self.popout)
		self.uid = self.Popout_Analyzer.setUID(self.uid)

		self.Pin_Analyzer = QT_Button().setStyleName("Header_Button").setCheckable(True).setChecked(True).setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_PINNED_OFF.svg"))
		self.Pin_Analyzer.clicked.connect(self.pin)
		self.uid = self.Pin_Analyzer.setUID(self.uid)

		self.Reload_Analyzer = QT_Button().setStyleName("Header_Button").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/WINDOW_REFRESH.svg"))
		self.Reload_Analyzer.clicked.connect(self.processUI)

		self.Exit_Analyzer = QT_Button().setStyleName("Header_Button").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Window/WINDOW_CLOSE.svg"))
		self.Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = QT_Linear_Contents()
		self.BUI_Header.setContentsMargins(5,5,5,5)
		self.BUI_Header.setFixedHeight(34)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(self.Popout_Mode).addWidget(self.Pin_Analyzer).addWidget(self.Reload_Analyzer).addWidget(self.Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = VBox(self)
		self.uid = self.BUI_Layout.setUID(self.uid)
		self.BUI_Layout.setContentsMargins(5,5,5,5)
		self.Properties = []

		BUI_Splitter = QT_Splitter().setStyleName("Window").addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter).setWindowTitle("BUI DRIVERS").setWindowIcon(QIcon(PATH+"/Resources/Icons/Workspaces/WORKSPACE_DRIVERS.svg"))

		self.processUI()
		self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
		self.move(0,0)
		self.resize(500, QGuiApplication.primaryScreen().availableGeometry().height())
		self.show()
		self.geometryStore = self.saveGeometry()

	def popoutMode(self, toggle):
		self.geometryStore = self.saveGeometry()
		if toggle:
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
			self.Popout_Analyzer.show()
			self.Reload_Analyzer.hide()
			self.Exit_Analyzer.hide()
			self.Pin_Analyzer.hide()
		else:
			self.Popout_Analyzer.hide()
			self.Reload_Analyzer.show()
			self.Exit_Analyzer.show()
			self.Pin_Analyzer.show()
			if not self.Pin_Analyzer.isChecked():
				self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
		self.show()
		self.restoreGeometry(self.geometryStore)

	def popout(self, toggle):
		self.geometryStore = self.saveGeometry()
		if toggle:
			self.Popout_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_EXPAND_ON.svg"))
			self.show()
			self.restoreGeometry(self.geometryStore)
		else:
			self.Popout_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_EXPAND_OFF.svg"))
			self.hide()

	def pin(self, toggle):
		self.geometryStore = self.saveGeometry()
		if toggle:
			self.Pin_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_PINNED_ON.svg"))
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
		else:
			self.Pin_Analyzer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_PINNED_OFF.svg"))
			self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
		self.show()
		self.restoreGeometry(self.geometryStore)

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
			try:
				if isinstance(widget, I_DRIVER) or isinstance(widget, F_DRIVER) or isinstance(widget, B_DRIVER) or isinstance(widget, E_DRIVER):
					widget.executeBlenderFetch()
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
		if event.type() == QEvent.Type.MouseButtonRelease:
			self.mouse_pressed = False
		return super().eventFilter(source, event)

	def mousePressEvent(self, event):
		focused_widget = QApplication.focusWidget()
		if isinstance(focused_widget, QT_Line_Editor):
			focused_widget.clearFocus()
		super().mousePressEvent(event)

	def focusInEvent(self, event: QFocusEvent):
		print("Refresh")
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

	def saveSettings(self) -> str:
		return self.geometryStore.toBase64().data().decode('utf-8') if self.geometryStore else None

	def restoreSettings(self, state: str):
		self.geometryStore = QByteArray.fromBase64(state.encode('utf-8'))
		self.restoreGeometry(self.geometryStore)

	def restore(self):
		file = bpy.data.texts.get("DRIVER Settings")
		settings = json.loads(file.as_string())
		if "QT_Window" in settings:
			self.restoreSettings(settings["QT_Window"])
		for widget in QCoreApplication.instance().allWidgets():
			if widget.whatsThis() != "":
				try:
					if isinstance(widget, List):
						widget: List = widget
						if f"Dropdown || {widget.whatsThis()}" in settings:
							widget.restoreSettings(settings[f"Dropdown || {widget.whatsThis()}"])
				except: pass

	def save(self):
		settings = {}
		settings[f"QT_Window"] = self.saveSettings()
		for widget in QCoreApplication.instance().allWidgets():
			if widget.whatsThis() != "":
				try:
					if isinstance(widget, List):
						widget: List = widget
						settings[f"Dropdown || {widget.whatsThis()}"] = widget.saveSettings()
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
	def i_driver(self) -> I_DRIVER:
		driver = self.BUI_Layout.i_driver()
		return driver
	def f_driver(self) -> F_DRIVER:
		driver = self.BUI_Layout.f_driver()
		return driver
	def b_driver(self) -> B_DRIVER:
		driver = self.BUI_Layout.b_driver()
		return driver
	def e_driver(self) -> E_DRIVER:
		driver = self.BUI_Layout.e_driver()
		return driver
	def p_driver(self) -> P_DRIVER:
		driver = self.BUI_Layout.p_driver()
		return driver