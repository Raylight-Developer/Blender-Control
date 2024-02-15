from BUI import *

class Central_Layout(QT_Window):
	def __init__(self):
		super().__init__()
		self.uid = 0
		self.uid = self.setUID(self.uid)

		self.mouse_pressed = False
		Reload_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/file_refresh.svg"))
		Reload_Analyzer.clicked.connect(lambda: self.processUI())

		Exit_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/panel_close.svg"))
		Exit_Analyzer.clicked.connect(lambda: self.quit())

		self.BUI_Header = Row()
		self.BUI_Header.setContentsMargins(5,5,5,5)
		self.BUI_Header.setFixedHeight(34)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(Reload_Analyzer).addWidget(Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()
		self.uid = self.BUI_Layout.setUID(self.uid)
		self.BUI_Layout.setContentsMargins(5,5,5,5)
		self.Properties = []

		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter)

		self.processUI()
		self.loadSettings()

	def loadSettings(self):
		self.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
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
			with open(PATH+"/Resources/BUI.json", "r", encoding = "utf-8") as file:
				settings = json.load(file)
				file.close()
				for widget in QCoreApplication.instance().allWidgets():
					if widget.whatsThis() != "":
						try:
							if type(widget) == Dropdown:
								widget: Dropdown = widget
								widget.restoreState(settings[f"{widget.whatsThis()}"])
							elif type(widget) == Search_List:
								widget: Search_List = widget
								widget.restoreState(settings[f"{widget.whatsThis()}"])
						except Exception as err: print(err)

	def save(self):
		settings = {}
		for widget in QCoreApplication.instance().allWidgets():
			if widget.whatsThis() != "":
				try:
					if type(widget) == Dropdown:
						widget: Dropdown = widget
						settings[f"{widget.whatsThis()}"] = widget.saveState()
					elif type(widget) == Search_List:
						widget: Search_List = widget
						settings[f"{widget.whatsThis()}"] = widget.saveState()
				except Exception as err: print(err)

		print(settings)
		with open(PATH+"/Resources/BUI.json", "wt", encoding = "utf-8") as file:
			json.dump(settings, file)
			file.close()

	def row(self) -> Row:
		row = self.BUI_Layout.row()
		self.uid +=1
		return row
	def column(self) -> Column:
		column = self.BUI_Layout.column()
		self.uid +=1
		return column
	def box(self) -> Box:
		box = self.BUI_Layout.box()
		self.uid +=1
		return box
	def dropdown(self) -> Dropdown:
		dropdown = self.BUI_Layout.dropdown()
		self.uid +=1
		return dropdown
	def list(self) -> Search_List:
		list = self.BUI_Layout.list()
		self.uid +=1
		return list