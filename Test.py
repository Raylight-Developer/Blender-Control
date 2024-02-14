import sys
from BUI import *

class Central_Layout(QT_Window):
	def __init__(self):
		super().__init__()
		self.mouse_pressed = False
		Reload_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon("./Resources/file_refresh.svg"))
		Reload_Analyzer.clicked.connect(self.processUI)

		Exit_Analyzer = QT_Button().setStyleName("Icon").setFixedWidth(24).setIcon(QIcon("./Resources/panel_close.svg"))
		Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = Row()
		self.BUI_Header.setContentsMargins(5,5,5,5)
		self.BUI_Header.setFixedHeight(34)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(Reload_Analyzer).addWidget(Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()
		self.BUI_Layout.setContentsMargins(5,5,5,5)
		self.Properties = []

		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter)
		self.processUI()

	def processUI(self):
		QApplication.instance().setStyleSheet(open(PATH+"/Resources/Stylesheet.css","r").read())
		self.BUI_Layout.clear()
		layout = self.BUI_Layout
		
		#exec(code) -----------------------------
		row : Row = layout.row()
		test: FloatProperty = row.prop(Type.FLOAT, self, "Test Float")
		row : Row = layout.row()
		dropdown: Dropdown = layout.dropdown()
		test: IntProperty = dropdown.prop(Type.INT, self, "Test Int")
		test: BoolProperty = dropdown.prop(Type.BOOL, self, "Test Bool")
		test: IntProperty = dropdown.prop(Type.INT, self, "Test Integer Number walalala")
		test: IntProperty = dropdown.prop(Type.INT, self, "Test Int 5")
		row = dropdown.row()
		dropdown: Dropdown = row.dropdown()
		list: Search_List = row.list()
		list.prop(Type.ENUM, self, "Enum")
		#----------------------------------------
		for widget in self.Properties:
			try: widget.fetch()
			except Exception as err: print(err)

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
		self.close()
		QCoreApplication.quit()
		QCoreApplication.exit()
		QCoreApplication.instance().quit()
		QCoreApplication.instance().exit()

	def focusInEvent(self, event: QFocusEvent):
		for widget in self.Properties:
			try: widget.fetch()
			except Exception as err: print(err)

App = QApplication()
Window = Central_Layout()
Window.processUI()
Window.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
Window.show()
sys.exit(App.exec())