import sys, bpy, pip

bl_info = {
	"name": "Blender DRIVER",
	"description": "",
	"author": "Pekoyo",
	"version": (0, 0, 1, 0),
	"blender": (4, 0, 2),
	"warning": "",
	"doc_url": "",
	"category": "User Interface",
}

pip.main(["install", "PySide6", "--user"])

#--------------------------------------------------------------------------------------------------
from .BUI import *
#--------------------------------------------------------------------------------------------------
class DRIVER_Program_Window(QT_Window):
	def __init__(self):
		super().__init__()
		self.setStyleSheet(open("./Resources/Stylesheet.css", "r", encoding="utf-8").read())

		self.mouse_pressed = False
		Reload_Analyzer = QT_Button().setStyle("Icon").setFixedWidth(24).setIcon(QIcon("./Resources/file_refresh.svg")).setFixedSize(30,30)
		Reload_Analyzer.clicked.connect(self.processUI)

		Exit_Analyzer = QT_Button().setStyle("Icon").setFixedWidth(24).setIcon(QIcon("./Resources/panel_close.svg")).setFixedSize(30,30)
		Exit_Analyzer.clicked.connect(self.quit)

		self.BUI_Header = Row()
		self.BUI_Header.setFixedHeight(24)
		self.BUI_Header.Linear_Layout.setAlignment(Qt.AlignmentFlag.AlignRight)
		self.BUI_Header.addWidget(Reload_Analyzer).addWidget(Exit_Analyzer)
		self.BUI_Header.installEventFilter(self)

		self.BUI_Layout = Column()

		BUI_Splitter = QT_Splitter().addWidget(self.BUI_Header).addWidget(self.BUI_Layout)
		
		self.setCentralWidget(BUI_Splitter).setWindowTitle("DRIVER").setWindowIcon(QIcon("./Resources/shapekey_data.svg"))
		self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.CustomizeWindowHint)
		self.show()
		if not bpy.data.texts.get("DRIVER"):
			new_text_block = bpy.data.texts.new(name="DRIVER")
			new_text_block.write("row = layout.row()")
		self.processUI()

	def processUI(self):
		self.BUI_Layout.clear()
		layout = self.BUI_Layout
		code = bpy.data.texts.get("DRIVER").as_string()
		exec(code)

	def eventFilter(self, source, event: QEvent | QMouseEvent | QKeyEvent):
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
	
	def quit(self):
		self.close()
		QCoreApplication.quit()
		QCoreApplication.exit()
		QCoreApplication.instance().quit()
		QCoreApplication.instance().exit()

#--------------------------------------------------------------------------------------------------

class DRIVER_Qt_Window_Event_Loop(bpy.types.Operator):
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

class DRIVER_Blender_Functions(DRIVER_Qt_Window_Event_Loop):
	bl_idname = 'driver.open'
	bl_label = 'Control'

	def __init__(self):
		super().__init__(DRIVER_Program_Window)
		
class DRIVER_Blender_Interface(bpy.types.Panel):
	bl_label = "Blender Controls"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "scene"

	def draw(self, context):
		self.layout.row().operator("driver.open", text = "CONTROLS")

Classes = [
	DRIVER_Blender_Interface,
	DRIVER_Blender_Functions,
	DRIVER_Qt_Window_Event_Loop
]

def register():
	for Class in Classes:
		bpy.utils.register_class(Class)


def unregister():
	for Class in Classes:
		bpy.utils.unregister_class(Class)


if __name__ == "__main__":
	register()