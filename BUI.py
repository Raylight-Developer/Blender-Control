from typing import *
from enum import Enum
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Type(Enum):
	INT = 0
	BOOL = 1
	FLOAT = 2

class Icon(Enum):
	NONE = 0

class IntProperty(QSlider):
	def __init__(self):
		super().__init__()
	def expression(expression: str = ""): pass
	def min(value : int = 0): pass
	def max(value : int = 1): pass
	def soft_limits(value : bool = True): pass
	def soft_min(value : int = 0): pass
	def soft_max(value : int = 1): pass
	def step(value : int = 1): pass
	def execute(self, driver):
		try: exec(self.expr)
		except: pass

class BoolProperty(QCheckBox):
	def __init__(self):
		super().__init__()
	def expression(expression: str = ""): pass
	def execute(self, driver):
		try: exec(self.expr)
		except: pass

class FloatProperty(QSlider):
	def __init__(self):
		super().__init__()
		super().setOrientation(Qt.Orientation.Horizontal)
		self.expr = ""
		self.valueChanged.connect(self.execute)
	def expression(self, expression: str = ""):
		self.expr = expression
	def min(value : float = 0.0): pass
	def max(value : float = 1.0): pass
	def soft_limits(value : bool = True): pass
	def soft_min(value : float = 0.0): pass
	def soft_max(value : float = 1.0): pass
	def step(value : float = 0.1): pass
	def precision(value: int = 4): pass
	def execute(self, driver):
		try: exec(self.expr)
		except: pass

class Row(QWidget):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		self.Layout = QHBoxLayout()
		self.Layout.setContentsMargins(0,0,0,0)
		super().setLayout(self.Layout)
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.Layout.addWidget(column)
		return column
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			self.Layout.addWidget(prop)
		return prop

class Column(QWidget):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		self.Layout = QVBoxLayout()
		self.Layout.setContentsMargins(0,0,0,0)
		super().setLayout(self.Layout)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.Layout.addWidget(row)
		return row
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			self.Layout.addWidget(prop)
		return prop