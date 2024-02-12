import sys
from BUI import *

class Central_Layout(QT_Window):
	def __init__(self):
		super().__init__()
		self.mouse_pressed = False
		Reload_Analyzer = QT_Button().setIcon(QIcon("./Resources/file_refresh.svg"))#.setFixedSize(30,30)
		Reload_Analyzer.clicked.connect(self.processUI)

		Exit_Analyzer = QT_Button().setIcon(QIcon("./Resources/panel_close.svg"))#.setFixedSize(30,30)
		Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = Row()
		self.BUI_Header.setFixedHeight(30)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(Reload_Analyzer).addWidget(Exit_Analyzer)#.setFixedHeight(30)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()
		
		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		self.setCentralWidget(BUI_Splitter)
		self.processUI()

	def processUI(self):
		QApplication.instance().setStyleSheet(open("./Resources/Stylesheet.css","r").read())
		self.BUI_Layout.clear()
		layout = self.BUI_Layout
		
		#exec(code) -----------------------------
		row : Row = layout.row()
		test_slider: FloatProperty = row.prop(Type.FLOAT, "Test Slider", Icon.NONE, "")
		row : Row = layout.row()
		test_slider: IntProperty = row.prop(Type.INT, "Test Slider", Icon.NONE, "")
		#----------------------------------------

	def eventFilter(self, source, event: QEvent):
		if source == self.BUI_Header and event.type() == QEvent.Type.MouseButtonPress:
			if event.button() == Qt.MouseButton.RightButton:
				self.initial_pos =  event.globalPosition()
				self.mouse_pressed = True
		elif source == self.BUI_Header and event.type() == QEvent.Type.MouseMove and self.mouse_pressed:
			delta = event.globalPosition() - self.initial_pos
			pos = QPointF(self.pos()) + delta
			self.move(pos.x(), pos.y())
			self.initial_pos =  event.globalPosition()
		elif event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.RightButton:
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

	def focusInEvent(self, event):
		print("Window is focused")
		event.accept()

App = QApplication()
App.setStyleSheet(open("./Resources/Stylesheet.css","r").read())
Window = Central_Layout()
Window.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint)
Window.show()
sys.exit(App.exec())