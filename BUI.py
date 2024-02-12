try: from .QT_Core import *
except: from QT_Core import *

class Int_Slider(QT_Slider):
	def __init__(self):
		super().__init__()

		self.setRange(0, 1)
		self.setStyle("Int_Slider")

	def setValue(self, value):
		super().setValue(int(value))

	def mousePressEvent(self, event: QMouseEvent):
		if event.button() == Qt.MouseButton.LeftButton and not self.isSliderDown():
			Option = QStyleOptionSlider()
			self.initStyleOption(Option)
			Slider_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderHandle, self)
			if event.pos() not in Slider_Size.getCoords() and self.underMouse():
				Handle_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderGroove, self)
				Center = Slider_Size.center() - Slider_Size.topLeft()
				Pos = event.pos() - Center
				Length = Slider_Size.width()
				Min = Handle_Size.x()
				Max = Handle_Size.right() - Length + 1
				Pos = Pos.x()
				Value = self.style().sliderValueFromPosition( self.minimum(), self.maximum(), Pos - Min, Max - Min)
				self.setSliderPosition(Value)

	def mouseMoveEvent(self, event: QMouseEvent):
		if event.buttons() & Qt.MouseButton.LeftButton and self.underMouse():
			Option = QStyleOptionSlider()
			self.initStyleOption(Option)
			Slider_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderHandle, self)
			if event.pos():
				Handle_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderGroove, self)
				Center = Slider_Size.center() - Slider_Size.topLeft()
				Pos = event.pos() - Center
				Length = Slider_Size.width()
				Min = Handle_Size.x()
				Max = Handle_Size.right() - Length + 1
				Pos = Pos.x()
				Value = self.style().sliderValueFromPosition(self.minimum(), self.maximum(), Pos - Min, Max - Min)
				self.setSliderPosition(Value)

	def paintEvent(self, event):
		QSlider.paintEvent(self, event)
		painter = QPainter(self)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painterPath = QPainterPath()
		painterPath.addText(QPointF(self.geometry().width() / 2 - QFontMetrics(self.font()).horizontalAdvance(str(self.value())) / 2, self.geometry().height() * 0.75), self.font() ,str(self.value()))
		painter.strokePath(painterPath, QPen(QColor(250,250,250), 0.5))
		painter.fillPath(painterPath, QColor(250,250,250))

class Float_Slider(QT_Slider):
	def __init__(self):
		super().__init__()
		self.precision = 3
		self.divider = 1000

		self.setRange(0, self.divider)

	def setValue(self, value):
		super().setValue(int(value * self.divider))

	def mousePressEvent(self, event: QMouseEvent):
		if event.button() == Qt.MouseButton.LeftButton and not self.isSliderDown() and self.underMouse():
			Option = QStyleOptionSlider()
			self.initStyleOption(Option)
			Slider_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderHandle, self)
			if event.pos() not in Slider_Size.getCoords():
				Handle_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderGroove, self)
				Center = Slider_Size.center() - Slider_Size.topLeft()
				Pos = event.pos() - Center
				Length = Slider_Size.width()
				Min = Handle_Size.x()
				Max = Handle_Size.right() - Length + 1
				Pos = Pos.x()
				Value = self.style().sliderValueFromPosition( self.minimum(), self.maximum(), Pos - Min, Max - Min)
				self.setSliderPosition(Value)

	def mouseMoveEvent(self, event: QMouseEvent):
		if event.buttons() & Qt.MouseButton.LeftButton and self.underMouse():
			Option = QStyleOptionSlider()
			self.initStyleOption(Option)
			Slider_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderHandle, self)
			if event.pos():
				Handle_Size = self.style().subControlRect(QStyle.ComplexControl.CC_Slider, Option, QStyle.SubControl.SC_SliderGroove, self)
				Center = Slider_Size.center() - Slider_Size.topLeft()
				Pos = event.pos() - Center
				Length = Slider_Size.width()
				Min = Handle_Size.x()
				Max = Handle_Size.right() - Length + 1
				Pos = Pos.x()
				Value = self.style().sliderValueFromPosition(self.minimum(), self.maximum(), Pos - Min, Max - Min)
				self.setSliderPosition(Value)

	def paintEvent(self, event):
		QSlider.paintEvent(self, event)
		painter = QPainter(self)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painterPath = QPainterPath()
		painterPath.addText(QPointF(self.geometry().width() / 2 - QFontMetrics(self.font()).horizontalAdvance(f"{{:.{self.precision}f}}".format(self.value() / self.precision)) / 2, self.geometry().height() * 0.75), self.font() , f"{{:.{self.precision}f}}".format(self.value() / self.divider))
		painter.strokePath(painterPath, QPen(QColor(250,250,250), 0.5))
		painter.fillPath(painterPath, QColor(250,250,250))

# TYPES--------------------------------------------------------------------------------------------

class Type(Enum):
	INT = 0
	BOOL = 1
	FLOAT = 2

class Icon(Enum):
	NONE = 0

# PROPERTY-----------------------------------------------------------------------------------------
class IntProperty(QT_Linear_Contents):
	def __init__(self, fetch):
		super().__init__(False)
		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.text = ""
		self.icon = Icon.NONE
		self.min = 0
		self.max = 1
		self.label = QT_Label().setText(self.text)
		self.input = QT_Line_Editor().setValidator(QIntValidator(0, 1))
		self.slider = Int_Slider()
		self.keyframer = QT_Button().setCheckable(True).setIcon(QIcon("./Resources/keyframe.svg"))
		self.decrease = QT_Button().setStyle("Int_L").setIcon(QIcon("./Resources/left_arrow_thin.svg"))
		self.increase = QT_Button().setStyle("Int_R").setIcon(QIcon("./Resources/right_arrow_thin.svg"))

		self.addWidget(self.label).addWidget(self.decrease).addWidget(self.slider).addWidget(self.increase).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if fetch:
			try:
				exec(f"self.input.setText({fetch})")
				exec(f"self.slider.setValue({fetch})")
			except Exception as error: print(error)
		self.slider.valueChanged.connect(self.execute_expression)
		self.keyframer.clicked.connect(lambda clicked: self.execute_keyframe(clicked))
		self.input.editingFinished.connect(self.cancelValueChange)
		self.input.returnPressed.connect(self.changeValue)
		self.input.focusOutEvent = self.cancelValueChange
		self.decrease.clicked.connect(lambda: self.slider.setValue(self.slider.value()-1))
		self.increase.clicked.connect(lambda: self.slider.setValue(self.slider.value()+1))
	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.RightButton:
			self.slider.hide()
			self.input.show()
			self.input.setFocus()
	def cancelValueChange(self, event = None):
		self.slider.show()
		self.input.hide()
	def changeValue(self):
		val = int(self.input.text())
		if val > self.max: val = self.max
		elif val < self.min: val = self.min
		self.slider.setValue(val)
	def set_driver_expression(self, driver_expression: str = ""):
		self.driver_expression = driver_expression
	def set_add_keyframe_expression(self, keyframe_expression: str = ""):
		self.add_keyframe_expression = keyframe_expression
	def set_remove_keyframe_expression(self, keyframe_expression: str = ""):
		self.remove_keyframe_expression = keyframe_expression
	def set_label(self, value: str = ""):
		self.text = value
		self.label.setText(value)
	def set_icon(self, value: Icon = Icon.NONE):
		self.icon = value
	def set_min(self, value : int = 0):
		self.min = value
		self.input.setValidator(QDoubleValidator(value, self.max))
	def set_max(self, value : int = 1):
		self.max = value
		self.input.setValidator(QIntValidator(self.min, value))
	def set_use_soft_limits(self, value : bool = True): pass
	def set_soft_min(self, value : int = 0):
		self.slider.setRange(value, self.slider.maximum())
	def set_soft_max(self, value : int = 1):
		self.slider.setRange(self.slider.minimum(), value)
	def set_step(self, value : int = 1): pass
	def execute_keyframe(self, keyframe):
		if keyframe:
			self.keyframer.setIcon(QIcon("./Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon("./Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		self.input.setText(f"{driver}")
		try: exec(self.driver_expression)
		except Exception as error: print(error)

class BoolProperty(QT_Button):
	def __init__(self):
		super().__init__()
		super().setCheckable(True)
	def expression(expression: str = ""): pass
	def execute(self, driver):
		try: exec(self.expr)
		except: pass

class FloatProperty(QT_Linear_Contents):
	def __init__(self, fetch):
		super().__init__(False)
		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.text = ""
		self.icon = Icon.NONE
		self.min = 0
		self.max = 1
		self.label = QT_Label().setText(self.text)
		self.input = QT_Line_Editor().setValidator(QDoubleValidator(decimals = 10))
		self.slider = Float_Slider()
		self.keyframer = QT_Button().setCheckable(True).setIcon(QIcon("./Resources/keyframe.svg"))

		self.addWidget(self.label).addWidget(self.slider).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if fetch:
			try:
				exec(f"self.input.setText({fetch})")
				exec(f"self.slider.setValue({fetch})")
			except Exception as error: print(error)
		self.slider.valueChanged.connect(self.execute_expression)
		self.keyframer.clicked.connect(lambda clicked: self.execute_keyframe(clicked))
		self.input.editingFinished.connect(self.cancelValueChange)
		self.input.returnPressed.connect(self.changeValue)
		self.input.focusOutEvent = self.cancelValueChange
	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.RightButton:
			self.slider.hide()
			self.input.show()
			self.input.setFocus()
	def cancelValueChange(self, event = None):
		self.slider.show()
		self.input.hide()
	def changeValue(self):
		val = float(self.input.text())
		if val > self.max: val = self.max
		elif val < self.min: val = self.min
		self.slider.setValue(val)
	def set_driver_expression(self, driver_expression: str = ""):
		self.driver_expression = driver_expression
	def set_add_keyframe_expression(self, keyframe_expression: str = ""):
		self.add_keyframe_expression = keyframe_expression
	def set_remove_keyframe_expression(self, keyframe_expression: str = ""):
		self.remove_keyframe_expression = keyframe_expression
	def set_label(self, value: str = ""):
		self.text = value
		self.label.setText(value)
	def set_icon(self, value: Icon = Icon.NONE):
		self.icon = value
	def set_min(self, value : float = 0.0):
		self.min = value
		self.input.setValidator(QDoubleValidator(decimals = 10))
	def set_max(self, value : float = 1.0):
		self.max = value
		self.input.setValidator(QDoubleValidator(decimals = 10))
	def set_use_soft_limits(self, value : bool = True): pass
	def set_soft_min(self, value : float = 0.0):
		self.slider.setRange(value, self.slider.maximum())
	def set_soft_max(self, value : float = 1.0):
		self.slider.setRange(self.slider.minimum(), value)
	def set_step(self, value : float = 0.1): pass
	def set_precision(self, value: int = 3):
		self.slider.precision = value
	def execute_keyframe(self, keyframe):
		if keyframe:
			self.keyframer.setIcon(QIcon("./Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon("./Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		self.input.setText(f"{driver / self.slider.divider}")
		driver = float(driver / self.slider.divider)
		try: exec(self.driver_expression)
		except Exception as error: print(error)

# LAYOUT-------------------------------------------------------------------------------------------

class Row(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.addWidget(column)
		return column
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE, fetch: str = None) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty(fetch)
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty(fetch)
			prop.set_label(text)
			self.addWidget(prop)
		return prop

class Column(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.addWidget(row)
		return row
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE, fetch: str = None) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty(fetch)
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty(fetch)
			prop.set_label(text)
			self.addWidget(prop)
		return prop

class Dropdown(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Toggle = QT_Button().setText("E/C").setCheckable(True)
		self.Container = QT_Scroll_Area()
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.Container.addWidget(row)
		return row
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE, fetch: str = None) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty(fetch)
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty(fetch)
			prop.set_label(text)
			self.addWidget(prop)
		return prop