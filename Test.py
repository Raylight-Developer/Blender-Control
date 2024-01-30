import sys
from BUI import *

class Central_Layout(QSplitter):
	def __init__(self):
		super().__init__()
		super().setOrientation(Qt.Orientation.Vertical)
		Exit_Analyzer = QPushButton()
		Exit_Analyzer.setText("❌")
		Exit_Analyzer.setFixedSize(30,30)
		Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = Column()
		self.BUI_Header.setFixedHeight(30)
		self.BUI_Header.setContentsMargins(0,0,0,0)
		self.BUI_Header.Layout.addWidget(Exit_Analyzer, 1, Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()

		self.setContentsMargins(0,0,0,0)
		self.addWidget(self.BUI_Header)
		self.addWidget(self.BUI_Layout)
		self.setStyleSheet("background:rgb(50,50,50)")
		self.setHandleWidth(5)

		self.processUI()

	def processUI(self):
		for i in range(self.BUI_Layout.Layout.count()):
			self.BUI_Layout.Layout.itemAt(i).widget().deleteLater()
		layout = self.BUI_Layout
		code = open("UI.bui", "r", -1, "utf-8").read().replace("from BUI_Editing import *\n", "")
		print(code)
		exec(code)

	def eventFilter(self, source, event):
		if source == self.BUI_Header and event.type() == QEvent.Type.MouseButtonPress:
			if event.button() == Qt.MouseButton.RightButton:
				self.initial_pos = event.globalPos()
				self.mouse_pressed = True
		elif source == self.BUI_Header and event.type() == QEvent.Type.MouseMove and self.mouse_pressed:
			delta = event.globalPos() - self.initial_pos
			pos = self.pos() + delta
			self.move(pos.x(), pos.y())
			self.initial_pos = event.globalPos()
		elif event.type() == QEvent.Type.MouseButtonRelease and event.button() == Qt.MouseButton.RightButton:
			self.mouse_pressed = False
		return super().eventFilter(source, event)
	
	def quit(self):
		self.close()
		QCoreApplication.quit()
		QCoreApplication.exit()
		QCoreApplication.instance().quit()
		QCoreApplication.instance().exit()

App = QApplication()
Window = Central_Layout()
Window.setWindowFlags(Qt.WindowType.CustomizeWindowHint)
Window.show()
sys.exit(App.exec())