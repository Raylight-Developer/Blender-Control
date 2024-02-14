try: from .QT_Core import *
except: from QT_Core import *

class Int_Slider(QT_Slider):
	def __init__(self):
		super().__init__()

		self.setRange(0, 1)
		self.setStyleName("Int_Slider")

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
	ENUM = 3

class Icon(Enum):
	NONE = 0

# PROPERTY-----------------------------------------------------------------------------------------
class IntProperty(QT_Linear_Contents):
	def __init__(self):
		super().__init__(False)
		self.setFixedHeight(24)

		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.fetch_expression = None
		self.text = ""
		self.icon = Icon.NONE
		self.min = 0
		self.max = 1

		self.label = QT_Label().setText(self.text).setToolTip(self.text).setFixedWidth(120)
		self.input = QT_Line_Editor().setValidator(QIntValidator(0, 1))
		self.slider = Int_Slider().setToolTip(self.text)
		self.keyframer = QT_Button().setStyleName("Key").setFixedWidth(24).setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
		self.decrease = QT_Button().setStyleName("Int_L").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/left_arrow_thin.svg"))
		self.increase = QT_Button().setStyleName("Int_R").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))

		self.addWidget(self.label).addWidget(self.decrease).addWidget(self.slider).addWidget(self.increase).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if self.fetch_expression:
			try:
				exec(f"self.input.setText({self.fetch_expression})")
				exec(f"self.slider.setValue({self.fetch_expression})")
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
		self.label.setText(value).setToolTip(self.text)
		self.slider.setToolTip(self.text)
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
			self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		self.input.setText(f"{driver}")
		try: exec(self.driver_expression)
		except Exception as error: print(error)
	def fetch(self):
		if self.fetch_expression:
			try: exec(self.fetch_expression)
			except Exception as error: print(error)

class FloatProperty(QT_Linear_Contents):
	def __init__(self):
		super().__init__(False)
		self.setFixedHeight(24)

		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.fetch_expression = None
		self.text = ""
		self.icon = Icon.NONE
		self.min = 0
		self.max = 1
		self.label = QT_Label().setText(self.text).setToolTip(self.text).setFixedWidth(120)
		self.input = QT_Line_Editor().setValidator(QDoubleValidator(decimals = 10))
		self.slider = Float_Slider().setToolTip(self.text)
		self.keyframer = QT_Button().setStyleName("Key").setFixedWidth(24).setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg"))

		self.addWidget(self.label).addWidget(self.slider).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if self.fetch_expression:
			try:
				exec(f"self.input.setText({self.fetch_expression})")
				exec(f"self.slider.setValue({self.fetch_expression})")
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
		self.label.setText(value).setToolTip(self.text)
		self.slider.setToolTip(self.text)
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
			self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		self.input.setText(f"{driver / self.slider.divider}")
		driver = float(driver / self.slider.divider)
		try: exec(self.driver_expression)
		except Exception as error: print(error)
	def fetch(self):
		if self.fetch_expression:
			try: exec(self.fetch_expression)
			except Exception as error: print(error)

class BoolProperty(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
		self.setFixedHeight(24)

		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.fetch_expression = None
		self.text = ""
		self.icon = Icon.NONE

		self.input = QT_Button().setStyleName("Bool_Prop").setCheckable(True).setText(self.text).setToolTip(self.text)
		self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg"))

		self.addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.execute_keyframe(clicked))
		self.input.clicked.connect(self.execute_expression)
	def set_label(self, value: str = ""):
		self.text = value
		self.input.setText(value).setToolTip(self.text)
	def set_driver_expression(self, driver_expression: str = ""):
		self.driver_expression = driver_expression
	def set_add_keyframe_expression(self, keyframe_expression: str = ""):
		self.add_keyframe_expression = keyframe_expression
	def set_remove_keyframe_expression(self, keyframe_expression: str = ""):
		self.remove_keyframe_expression = keyframe_expression
	def execute_keyframe(self, keyframe):
		if keyframe:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		try: exec(self.driver_expression)
		except Exception as error: print(error)
	def fetch(self):
		if self.fetch_expression:
			try: exec(self.fetch_expression)
			except Exception as error: print(error)

class EnumProperty(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
		self.setFixedHeight(24)

		self.driver_expression = ""
		self.add_keyframe_expression = ""
		self.remove_keyframe_expression = ""
		self.fetch_expression = None
		self.text = ""
		self.icon = Icon.NONE

		self.label = QT_Label().setText(self.text).setFixedWidth(120).setToolTip(self.text)
		self.input = QT_Option().addItem("Item")
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg"))

		self.addWidget(self.label).addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.execute_keyframe(clicked))

	def set_label(self, value: str = ""):
		self.text = value
		self.label.setText(value).setToolTip(self.text)
	def set_driver_expression(self, driver_expression: str = ""):
		self.driver_expression = driver_expression
	def set_add_keyframe_expression(self, keyframe_expression: str = ""):
		self.add_keyframe_expression = keyframe_expression
	def set_remove_keyframe_expression(self, keyframe_expression: str = ""):
		self.remove_keyframe_expression = keyframe_expression
	def execute_keyframe(self, keyframe):
		if keyframe:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
			try: exec(self.add_keyframe_expression)
			except Exception as error: print(error)
		else:
			self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
			try: exec(self.remove_keyframe_expression)
			except Exception as error: print(error)
	def execute_expression(self, driver):
		try: exec(self.driver_expression)
		except Exception as error: print(error)
	def fetch(self):
		if self.fetch_expression:
			try: exec(self.fetch_expression)
			except Exception as error: print(error)

# LAYOUT-------------------------------------------------------------------------------------------

class Row(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
		self.Linear_Layout.setSpacing(5)
		self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.addWidget(row)
		return row
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.addWidget(column)
		return column
	def box(self, align: bool = False) -> 'Box':
		box = Box()
		self.addWidget(box)
		return box
	def dropdown(self, text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, text: str = "List"):
		list = Search_List(text)
		self.addWidget(list)
		return list
	def prop(self, type: Type, window: 'Central_Layout' = None, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty | EnumProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.BOOL:
			prop = BoolProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.ENUM:
			prop = EnumProperty()
			prop.set_label(text)
			self.addWidget(prop)
		window.Properties.append(prop)
		return prop

class Column(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Linear_Layout.setSpacing(5)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.addWidget(row)
		return row
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.addWidget(column)
		return column
	def box(self, align: bool = False) -> 'Box':
		box = Box()
		self.addWidget(box)
		return box
	def dropdown(self, text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, text: str = "List"):
		list = Search_List(text)
		self.addWidget(list)
		return list
	def prop(self, type: Type, window: 'Central_Layout' = None, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty | EnumProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.BOOL:
			prop = BoolProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.ENUM:
			prop = EnumProperty()
			prop.set_label(text)
			self.addWidget(prop)
		window.Properties.append(prop)
		return prop

class Box(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
		self.Linear_Layout.setSpacing(5)
		self.setStyleName("Box")
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.addWidget(row)
		return row
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.addWidget(column)
		return column
	def box(self, align: bool = False) -> 'Box':
		box = Box()
		self.addWidget(box)
		return box
	def dropdown(self, text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, text: str = "List"):
		list = Search_List(text)
		self.addWidget(list)
		return list
	def prop(self, type: Type, window: 'Central_Layout' = None, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty | EnumProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.BOOL:
			prop = BoolProperty()
			prop.set_label(text)
			self.addWidget(prop)
		elif type == Type.ENUM:
			prop = EnumProperty()
			prop.set_label(text)
			self.addWidget(prop)
		window.Properties.append(prop)
		return prop

class Dropdown(QT_Linear_Contents):
	def __init__(self, text):
		super().__init__(True)
		self.Toggle = QT_Icon_Button().setStyleName("Dropdown").setText(text).setToolTip(text).setCheckable(True).setChecked(True).setFixedHeight(24).setIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Toggle.clicked.connect(self.expandCollapse)
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		else:
			self.Container.hide()
			self.Toggle.setIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.Container.addWidget(row)
		return row
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.Container.addWidget(column)
		return column
	def box(self, align: bool = False) -> 'Box':
		box = Box()
		self.Container.addWidget(box)
		return box
	def dropdown(self, text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(text)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self, text: str = "List"):
		list = Search_List(text)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Type, window: 'Central_Layout' = None, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty | EnumProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.BOOL:
			prop = BoolProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.ENUM:
			prop = EnumProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		window.Properties.append(prop)
		return prop

class Search_List(QT_Linear_Contents):
	def __init__(self, text):
		super().__init__(True)
		self.SearchBar = QT_Line_Editor().setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/viewzoom.svg"))
		self.SearchBar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText(text).setToolTip(text).setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
		self.Container.addWidget(self.SearchBar)
		self.Toggle.clicked.connect(self.expandCollapse)
	def expandCollapse(self, toggle):
		if toggle:
			self.Container.show()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		else:
			self.Container.hide()
			self.Toggle.setLeftIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.Container.addWidget(row)
		return row
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.Container.addWidget(column)
		return column
	def box(self, align: bool = False) -> 'Box':
		box = Box()
		self.Container.addWidget(box)
		return box
	def dropdown(self, text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(text)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self, text: str = "List"):
		list = Search_List(text)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Type, window: 'Central_Layout' = None, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty | EnumProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.INT:
			prop = IntProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.BOOL:
			prop = BoolProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		elif type == Type.ENUM:
			prop = EnumProperty()
			prop.set_label(text)
			self.Container.addWidget(prop)
		window.Properties.append(prop)
		return prop