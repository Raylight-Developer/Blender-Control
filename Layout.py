from BUI import *

from Items.IntProperty import *
from Items.BoolProperty import *
from Items.EnumProperty import*
from Items.FloatProperty import*

class Row(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
		self.Linear_Layout.setSpacing(5)
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def row(self) -> 'Row':
		row = Row()
		self.uid = row.setUID(self.uid)
		self.addWidget(row)
		return row
	def column(self) -> 'Column':
		column = Column()
		self.uid = column.setUID(self.uid)
		self.addWidget(column)
		return column
	def box(self) -> 'Box':
		box = Box()
		self.uid = box.setUID(self.uid)
		self.addWidget(box)
		return box
	def dropdown(self) -> 'Dropdown':
		dropdown = Dropdown()
		self.uid = dropdown.setUID(self.uid)
		self.addWidget(dropdown)
		return dropdown
	def list(self):
		list = Search_List()
		self.uid = list.setUID(self.uid)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		if window: window.Properties.append(prop)
		return prop

class Column(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Linear_Layout.setSpacing(5)
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def row(self) -> 'Row':
		row = Row()
		self.uid = row.setUID(self.uid)
		self.addWidget(row)
		return row
	def column(self) -> 'Column':
		column = Column()
		self.uid = column.setUID(self.uid)
		
		self.addWidget(column)
		return column
	def box(self) -> 'Box':
		box = Box()
		self.uid = box.setUID(self.uid)
		self.addWidget(box)
		return box
	def dropdown(self) -> 'Dropdown':
		dropdown = Dropdown()
		self.uid = dropdown.setUID(self.uid)
		self.addWidget(dropdown)
		return dropdown
	def list(self) -> 'Search_List':
		list = Search_List()
		self.uid = list.setUID(self.uid)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union['IntProperty', 'BoolProperty', 'FloatProperty', 'EnumProperty']:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		if window: window.Properties.append(prop)
		
		return prop
	
class Box(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Linear_Layout.setSpacing(5)
		self.setStyleName("Box")
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def row(self) -> 'Row':
		row = Row()
		self.uid = row.setUID(self.uid)
		self.addWidget(row)
		return row
	def column(self) -> 'Column':
		column = Column()
		self.uid = column.setUID(self.uid)
		self.addWidget(column)
		
		return column
	def box(self) -> 'Box':
		box = Box()
		self.uid = box.setUID(self.uid)
		self.addWidget(box)
		return box
	def dropdown(self) -> 'Dropdown':
		dropdown = Dropdown()
		self.uid = dropdown.setUID(self.uid)
		self.addWidget(dropdown)
		return dropdown
	def list(self):
		list = Search_List()
		self.uid = list.setUID(self.uid)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.uid = prop.setUID(self.uid)
			self.addWidget(prop)
		if window: window.Properties.append(prop)
		
		return prop
	
	
class Dropdown(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText("").setToolTip("").setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Toggle.clicked.connect(self.expandCollapse)
	def saveState(self) -> Dict:
		return { "state": self.Toggle.isChecked()}
	def restoreState(self, state: Dict):
		if state["state"]:
			self.Container.show()
			self.Toggle.setChecked(True)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		elif not state["state"] :
			self.Container.hide()
			self.Toggle.setChecked(False)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def row(self) -> 'Row':
		row = Row()
		self.uid = row.setUID(self.uid)
		self.Container.addWidget(row)
		return row
	def column(self) -> 'Column':
		column = Column()
		self.uid = column.setUID(self.uid)
		self.Container.addWidget(column)
		return column
	def box(self) -> 'Box':
		box = Box()
		self.uid = box.setUID(self.uid)
		self.Container.addWidget(box)
		return box
	def dropdown(self) -> 'Dropdown':
		dropdown = Dropdown()
		self.uid = dropdown.setUID(self.uid)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self):
		list = Search_List()
		self.uid = list.setUID(self.uid)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		if window: window.Properties.append(prop)
		return prop

class Search_List(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.SearchBar = QT_Line_Editor().setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/viewzoom.svg"))
		self.SearchBar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText("").setToolTip("").setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Container.addWidget(self.SearchBar)
		self.Toggle.clicked.connect(self.expandCollapse)
	def saveState(self) -> Dict:
		return { "state": self.Toggle.isChecked()}
	def restoreState(self, state: Dict):
		if state["state"]:
			self.Container.show()
			self.Toggle.setChecked(True)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		elif not state["state"] :
			self.Container.hide()
			self.Toggle.setChecked(False)
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def row(self) -> 'Row':
		row = Row()
		self.uid = row.setUID(self.uid)
		self.Container.addWidget(row)
		return row
	def column(self) -> 'Column':
		column = Column()
		self.uid = column.setUID(self.uid)
		self.Container.addWidget(column)
		return column
	def box(self) -> 'Box':
		box = Box()
		self.uid = box.setUID(self.uid)
		self.Container.addWidget(box)
		return box
	def dropdown(self) -> 'Dropdown':
		dropdown = Dropdown()
		self.uid = dropdown.setUID(self.uid)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self):
		list = Search_List()
		self.uid = list.setUID(self.uid)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.uid = prop.setUID(self.uid)
			self.Container.addWidget(prop)
		if window: window.Properties.append(prop)
		
		return prop