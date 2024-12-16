import bpy, pip

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
try: from .Window_Env import *
except: from Window_Env import *
try: from .Kerzenlicht import *
except: from Kerzenlicht import *
#--------------------------------------------------------------------------------------------------

class DRIVER_Qt_Window_Event_Loop(bpy.types.Operator):
	bl_idname = 'screen.qt_event_loop'
	bl_label = 'Qt Event Loop'

	def __init__(self, widget, *args, **kwargs):
		self._widget: QWidget = widget
		self._args = args
		self._kwargs = kwargs

		self.Widget: QWidget
		self.Event_Loop: QEventLoop
		self.App: QApplication = None

	def modal(self, context: bpy.types.Context, event):
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

	def draw(self, context: bpy.types.Context):
		row = self.layout.row()
		row.operator("driver.open", text = "CONTROLS")
		row = self.layout.row()
		row.operator("wm.toggle_system_console", icon = 'CONSOLE')

class DRIVER_Console_Toggle(bpy.types.Operator):
	bl_idname = "wm.toggle_system_console"
	bl_label = "Toggle Console"

	def execute(self, context: bpy.types.Context):
		bpy.ops.wm.console_toggle()
		return {"FINISHED"}

Classes = [
	DRIVER_Blender_Interface,
	DRIVER_Blender_Functions,
	DRIVER_Qt_Window_Event_Loop,
	DRIVER_Console_Toggle
]

def register():
	for Class in Classes:
		bpy.utils.register_class(Class)

def unregister():
	for Class in Classes:
		bpy.utils.unregister_class(Class)

if __name__ == "__main__":
	register()