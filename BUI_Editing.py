from typing import *
from enum import Enum

class Type(Enum):
	INT = 0
	BOOL = 1
	FLOAT = 2

class Icon(Enum):
	NONE = 0

class IntProperty():
	def expression(expression: str = ""): pass
	def min(value : int = 0): pass
	def max(value : int = 1): pass
	def soft_limits(value : bool = True): pass
	def soft_min(value : int = 0): pass
	def soft_max(value : int = 1): pass
	def step(value : int = 1): pass

class BoolProperty():
	def expression(expression: str = ""): pass

class FloatProperty():
	def expression(expression: str = ""): pass
	def min(value : float = 0.0): pass
	def max(value : float = 1.0): pass
	def soft_limits(value : bool = True): pass
	def soft_min(value : float = 0.0): pass
	def soft_max(value : float = 1.0): pass
	def step(value : float = 0.1): pass
	def precision(value: int = 4): pass

class Row():
	def column(align: bool = False) -> 'Column': pass
	def prop(type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]: pass

class Column():
	def row(align: bool = False) -> 'Row': pass
	def prop(type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]: pass

layout = Column()