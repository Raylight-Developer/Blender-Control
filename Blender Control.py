import sys, bpy, pip

bl_info = {
	"name": "Blender Controls",
	"description": "",
	"author": "Pekoyo",
	"version": (0, 0, 1, 0),
	"blender": (4, 0, 2),
	"warning": "",
	"doc_url": "",
	"category": "User Interface",
}

pip.main(["install", "PySide6", "--user"])

bpy.context.scene["DRIVER"] = """
row : Row = layout.row()
test_slider: FloatProperty = row.prop(Type.FLOAT, "Test Slider")
test_slider.expression('bpy.data.objects["Cube"].data.shape_keys.key_blocks["Example"].value = driver')
"""
#--------------------------------------------------------------------------------------------------
from BUI import *
#--------------------------------------------------------------------------------------------------
class Program_Window(QMainWindow):
	def __init__(self):
		super().__init__()
		Reload_Analyzer = QPushButton()
		Reload_Analyzer.setText("⟳")
		Reload_Analyzer.setFixedSize(30,30)
		Reload_Analyzer.clicked.connect(self.processUI)

		Exit_Analyzer = QPushButton()
		Exit_Analyzer.setText("❌")
		Exit_Analyzer.setFixedSize(30,30)
		Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = Column()
		self.BUI_Header.setFixedHeight(30)
		self.BUI_Header.setContentsMargins(0,0,0,0)
		self.BUI_Header.Layout.addWidget(Reload_Analyzer, 1, Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.Layout.addWidget(Exit_Analyzer, 1, Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()

		BUI_Splitter  = QSplitter()
		BUI_Splitter.setOrientation(Qt.Orientation.Vertical)

		BUI_Splitter.setContentsMargins(0,0,0,0)
		BUI_Splitter.addWidget(self.BUI_Header)
		BUI_Splitter.addWidget(self.BUI_Layout)
		BUI_Splitter.setStyleSheet("background:rgb(50,50,50)")
		BUI_Splitter.setHandleWidth(5)
		
		self.setCentralWidget(BUI_Splitter)
		self.setWindowTitle("Analyzer")
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.CustomizeWindowHint)
		self.show()
		self.processUI()

	def processUI(self):
		for i in range(self.BUI_Layout.Layout.count()):
			self.BUI_Layout.Layout.itemAt(i).widget().deleteLater()
		layout = self.BUI_Layout
		code = bpy.context.scene["DRIVER"]
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

#--------------------------------------------------------------------------------------------------

class Qt_Window_Event_Loop(bpy.types.Operator):
	bl_idname = 'screen.qt_event_loop'
	bl_label = 'Qt Event Loop'

	def __init__(self, widget, *args, **kwargs):
		self._widget = widget
		self._args = args
		self._kwargs = kwargs

	def modal(self, context, event):
		Window_Manager = context.window_manager

		if not self.Widget.isVisible():
			Window_Manager.event_timer_remove(self._timer)
			return {'FINISHED'}
		else:
			self.Event_Loop.processEvents()
			self.App.sendPostedEvents(None, 0)

		return {'PASS_THROUGH'}

	def execute(self, context):

		self.App = QApplication.instance()
		if not self.App:
			self.App = QApplication(sys.argv)

		self.Event_Loop = QEventLoop()
		self.Widget = self._widget(*self._args, **self._kwargs)

		self._timer = context.window_manager.event_timer_add(1 / 120, window=context.window)
		context.window_manager.modal_handler_add(self)

		return {'RUNNING_MODAL'}

class Blender_Functions(Qt_Window_Event_Loop):
	bl_idname = 'screen.blender_control'
	bl_label = 'Control'

	def __init__(self):
		super().__init__(Program_Window)
		
class Blender_Interface(bpy.types.Panel):
	bl_label = "Blender Controls"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "scene"

	def draw(self, context):
		self.layout.row().operator("screen.blender_control", text = "CONTROLS")

Classes = [
	Blender_Interface,
	Blender_Functions,
	Qt_Window_Event_Loop
]

def register():
	for Class in Classes:
		bpy.utils.register_class(Class)


def unregister():
	for Class in Classes:
		bpy.utils.unregister_class(Class)


if __name__ == "__main__":
	register()