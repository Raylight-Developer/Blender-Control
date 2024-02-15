from BUI import *

class Central_Layout(QT_Window):
	def __init__(self):
		super().__init__()
		self.uid = 0
		self.uid = self.setUID(self.uid)

		self.mouse_pressed = False
		Reload_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/file_refresh.svg"))
		Reload_Analyzer.clicked.connect(lambda: self.quit())

		Exit_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/panel_close.svg"))
		Exit_Analyzer.clicked.connect(lambda: self.close())

		self.BUI_Header = Row()
		self.BUI_Header.setContentsMargins(5,5,5,5)
		self.BUI_Header.setFixedHeight(34)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(Reload_Analyzer).addWidget(Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()
		self.BUI_Layout.setContentsMargins(5,5,5,5)
		self.uid = self.BUI_Layout.setUID(self.uid)
		self.Properties = []

		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter)

		self.processUI()
		self.loadSettings()

	def loadSettings(self):
		self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
		self.restore()
		self.show()

	def processUI(self) -> Column:
		QApplication.instance().setStyleSheet(open(PATH+"/Resources/Stylesheet.css","r").read())
		self.BUI_Layout.clear()

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
		elif event.type() == QEvent.Type.MouseButtonRelease and (event.button() == Qt.MouseButton.RightButton or event.button() == Qt.MouseButton.LeftButton):
			self.mouse_pressed = False
		return super().eventFilter(source, event)
	
	def mousePressEvent(self, event):
		focused_widget = QApplication.focusWidget()
		if isinstance(focused_widget, QT_Line_Editor):
			focused_widget.clearFocus()
		super().mousePressEvent(event)

	def quit(self):
		self.save()
		self.close()

	def restore(self):
		if os.path.exists(PATH+"/Resources/BUI.json"):
			settings = json.loads(open(PATH+"/Resources/BUI.json", "r", encoding = "utf-8"))
			for widget in QApplication().allWidgets():
				if widget.whatsThis() != "":
					mo = widget.metaObject()
					for i in range(mo.propertyCount()):
						widget.setProperty(settings[f"{widget.whatsThis()}//{mo.property(i).name()}"])

	def save(self):
		settings = {}
		for widget in QApplication().allWidgets():
			if widget.whatsThis() != "":
				mo = widget.metaObject()
				for i in range(mo.propertyCount()):
					settings[f"{widget.whatsThis()}//{mo.property(i).name()}"] = widget.property(mo.property(i).name())
		open(PATH+"/Resources/BUI.json", "w", encoding = "utf-8").write(json.dump(settings))

	def row(self) -> Row:
		return self.BUI_Layout.row()
	def column(self) -> Column:
		return self.BUI_Layout.column()
	def box(self) -> Box:
		return self.BUI_Layout.box()
	def dropdown(self) -> Dropdown:
		return self.BUI_Layout.dropdown()
	def list(self) -> Search_List:
		return self.BUI_Layout.list()