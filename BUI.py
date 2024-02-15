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
		self.divider = int("1"+"0"*self.precision)

		self.setRange(0, self.divider)

	def setPrecision(self, precision):
		self.precision = precision
		self.divider = int("1"+"0"*self.precision)

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

class Prop_Type(Enum):
	INT = 0
	BOOL = 1
	FLOAT = 2
	ENUM = 3

class Icon(Enum):
	SEARCH = 0

# PROPERTY-----------------------------------------------------------------------------------------
class IntProperty(QT_Linear_Contents):
	python_driver_expression = None
	blender_fetch_expression = None
	add_keyframe_expression = None
	remove_keyframe_expression = None
	label_text = None
	label_icon = None
	label_visibility = True

	label : QT_Label
	keyframer : QT_Button

	min = 0
	max = 1
	step = 1

	def __init__(self):
		super().__init__(False)
		self.setFixedHeight(24)
		self.label = QT_Label().setText(self.label_text).setToolTip(self.label_text).setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg")).hide()

		self.input = QT_Line_Editor().setValidator(QIntValidator(0, 1))
		self.slider = Int_Slider().setToolTip(self.label_text)
		self.decrease = QT_Button().setStyleName("Int_L").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/left_arrow_thin.svg"))
		self.increase = QT_Button().setStyleName("Int_R").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/right_arrow_thin.svg"))

		self.addWidget(self.label).addWidget(self.decrease).addWidget(self.slider).addWidget(self.increase).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if self.blender_fetch_expression:
			try:
				exec(f"self.input.setText({self.blender_fetch_expression})")
				exec(f"self.slider.setValue({self.blender_fetch_expression})")
			except Exception as error: print(error)
		self.slider.valueChanged.connect(self.executePythonExpression)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))
		self.input.editingFinished.connect(self.cancelValueChange)
		self.input.returnPressed.connect(self.changeValue)
		self.input.focusOutEvent = self.cancelValueChange
		self.decrease.clicked.connect(lambda: self.slider.setValue(self.slider.value()-1))
		self.increase.clicked.connect(lambda: self.slider.setValue(self.slider.value()+1))

	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		self.label.setIcon(QIcon(label_icon))
	def setLabelIsVisible(self, visible: bool):
		if visible: self.label.show()
		else: self.label.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
	def setAddKeyframeExpresssion(self, keyframe_expression: str):
		self.add_keyframe_expression = keyframe_expression
		if self.remove_keyframe_expression: self.keyframer.show()
	def setRemoveKeyframeExpresssion(self, keyframe_expression: str):
		self.remove_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression: self.keyframer.show()
	def executeAddRemoveKeyframe(self, keyframe: bool):
		if self.add_keyframe_expression and self.remove_keyframe_expression:
			if keyframe:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
				try: exec(self.remove_keyframe_expression)
				except Exception as error: print(error)
	def executePythonExpression(self, driver: int):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)
	def executeBlenderFetch(self):
		if self.blender_fetch_expression:
			try: exec(self.blender_fetch_expression)
			except Exception as error: print(error)
	#IntProperty Methods ------------------------

	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.RightButton:
			self.slider.hide()
			self.input.show()
			self.input.setFocus()
	def cancelValueChange(self, event = None):
		self.slider.show()
		self.input.hide()
	def changeValue(self):
		val = int(self.input.label_text())
		if val > self.max: val = self.max
		elif val < self.min: val = self.min
		self.slider.setValue(val)
	def setMin(self, value : int = 0):
		self.min = value
		self.input.setValidator(QDoubleValidator(value, self.max))
	def setMax(self, value : int = 1):
		self.max = value
		self.input.setValidator(QIntValidator(self.min, value))
	def set_use_soft_limits(self, value : bool = True): pass
	def setSoft_min(self, value : int = 0):
		self.slider.setRange(value, self.slider.maximum())
	def setSoft_max(self, value : int = 1):
		self.slider.setRange(self.slider.minimum(), value)
	def setStep(self, value : int = 1): pass

class FloatProperty(QT_Linear_Contents):
	python_driver_expression = None
	blender_fetch_expression = None
	add_keyframe_expression = None
	remove_keyframe_expression = None
	label_text = None
	label_icon = None
	label_visibility = True

	label : QT_Label
	keyframer : QT_Button

	min = 0.0
	max = 1.0
	step = 0.001
	precision = 3

	def __init__(self):
		super().__init__(False)
		self.setFixedHeight(24)
		self.label = QT_Label().setText(self.label_text).setToolTip(self.label_text).setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg")).hide()

		self.input = QT_Line_Editor().setValidator(QDoubleValidator(decimals = 10))
		self.slider = Float_Slider().setToolTip(self.label_text)

		self.addWidget(self.label).addWidget(self.slider).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()
		if self.blender_fetch_expression:
			try:
				exec(f"self.input.setText({self.blender_fetch_expression})")
				exec(f"self.slider.setValue({self.blender_fetch_expression})")
			except Exception as error: print(error)
		self.slider.valueChanged.connect(self.executePythonExpression)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))
		self.input.editingFinished.connect(self.cancelValueChange)
		self.input.returnPressed.connect(self.changeValue)
		self.input.focusOutEvent = self.cancelValueChange

	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		self.label.setIcon(QIcon(label_icon))
	def setLabelIsVisible(self, visible: bool):
		if visible: self.label.show()
		else: self.label.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
	def setAddKeyframeExpresssion(self, keyframe_expression: str):
		self.add_keyframe_expression = keyframe_expression
		if self.remove_keyframe_expression: self.keyframer.show()
	def setRemoveKeyframeExpresssion(self, keyframe_expression: str):
		self.remove_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression: self.keyframer.show()
	def executeAddRemoveKeyframe(self, keyframe: bool):
		if self.add_keyframe_expression and self.remove_keyframe_expression:
			if keyframe:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
				try: exec(self.remove_keyframe_expression)
				except Exception as error: print(error)
	def executePythonExpression(self, driver: float):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)
	def executeBlenderFetch(self):
		if self.blender_fetch_expression:
			try: exec(self.blender_fetch_expression)
			except Exception as error: print(error)
	#

	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.RightButton:
			self.slider.hide()
			self.input.show()
			self.input.setFocus()
	def cancelValueChange(self, event = None):
		self.slider.show()
		self.input.hide()
	def changeValue(self):
		val = float(self.input.label_text())
		if val > self.max: val = self.max
		elif val < self.min: val = self.min
		self.slider.setValue(val)
	def set_label_icon(self, value: Icon = None):
		self.label_icon = value
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

class BoolProperty(QT_Linear_Contents):
	python_driver_expression = None
	blender_fetch_expression = None
	add_keyframe_expression = None
	remove_keyframe_expression = None
	label_text = None
	label_icon = None
	label_visibility = True

	label : QT_Label
	keyframer : QT_Button

	button_text = None
	button_icon = None

	def __init__(self):
		super().__init__()
		self.setFixedHeight(24)
		self.label = QT_Label().setText(self.label_text).setToolTip(self.label_text).setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg")).hide()

		self.input = QT_Button().setStyleName("Bool_Prop").setCheckable(True).setText(self.label_text).setToolTip(self.label_text)
		self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

		self.addWidget(self.label).addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))
		self.input.clicked.connect(self.executePythonExpression)

	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		self.label.setIcon(QIcon(label_icon))
	def setLabelIsVisible(self, visible: bool):
		if visible: self.label.show()
		else: self.label.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
	def setAddKeyframeExpresssion(self, keyframe_expression: str):
		self.add_keyframe_expression = keyframe_expression
		if self.remove_keyframe_expression: self.keyframer.show()
	def setRemoveKeyframeExpresssion(self, keyframe_expression: str):
		self.remove_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression: self.keyframer.show()
	def executeAddRemoveKeyframe(self, keyframe: bool):
		if self.add_keyframe_expression and self.remove_keyframe_expression:
			if keyframe:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
				try: exec(self.remove_keyframe_expression)
				except Exception as error: print(error)
	def executePythonExpression(self, driver: bool):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)
	def executeBlenderFetch(self):
		if self.blender_fetch_expression:
			try: exec(self.blender_fetch_expression)
			except Exception as error: print(error)

class EnumProperty(QT_Linear_Contents):
	python_driver_expression = None
	blender_fetch_expression = None
	add_keyframe_expression = None
	remove_keyframe_expression = None
	label_text = None
	label_icon = None
	label_visibility = True

	label : QT_Label
	keyframer : QT_Button

	dropdown_mode = True

	def __init__(self):
		super().__init__()
		self.setFixedHeight(24)
		self.label = QT_Label().setText(self.label_text).setToolTip(self.label_text).setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/keyframe.svg")).hide()

		self.input = QT_Option().addItem("Item")
		
		self.addWidget(self.label).addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))

	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		self.label.setIcon(QIcon(label_icon))
	def setLabelIsVisible(self, visible: bool):
		if visible: self.label.show()
		else: self.label.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
	def setAddKeyframeExpresssion(self, keyframe_expression: str):
		self.add_keyframe_expression = keyframe_expression
		if self.remove_keyframe_expression: self.keyframer.show()
	def setRemoveKeyframeExpresssion(self, keyframe_expression: str):
		self.remove_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression: self.keyframer.show()
	def executeAddRemoveKeyframe(self, keyframe: bool):
		if self.add_keyframe_expression and self.remove_keyframe_expression:
			if keyframe:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/decorate_keyframe.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/keyframe.svg"))
				try: exec(self.remove_keyframe_expression)
				except Exception as error: print(error)
	def executePythonExpression(self, driver: str):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)
	def executeBlenderFetch(self):
		if self.blender_fetch_expression:
			try: exec(self.blender_fetch_expression)
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
	def dropdown(self, label_text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(label_text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, label_text: str = "List"):
		list = Search_List(label_text)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window: 'DRIVER_Program_Window' = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.addWidget(prop)
		if window: window.Properties.append(prop)
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
	def dropdown(self, label_text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(label_text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, label_text: str = "List"):
		list = Search_List(label_text)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.addWidget(prop)
		if window: window.Properties.append(prop)
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
	def dropdown(self, label_text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(label_text)
		self.addWidget(dropdown)
		return dropdown
	def list(self, label_text: str = "List"):
		list = Search_List(label_text)
		self.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.addWidget(prop)
		if window: window.Properties.append(prop)
		return prop

class Dropdown(QT_Linear_Contents):
	def __init__(self, label_text):
		super().__init__(True)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText(label_text).setToolTip(label_text).setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
		self.Container = QT_Scroll_Area().setStyleName("Box")
		self.Toggle.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.addWidget(self.Toggle)
		self.addWidget(self.Container)
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
	def dropdown(self, label_text: str = "Dropdown") -> 'Dropdown':
		dropdown = Dropdown(label_text)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self, label_text: str = "List"):
		list = Search_List(label_text)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.Container.addWidget(prop)
		if window: window.Properties.append(prop)
		return prop

class Search_List(QT_Linear_Contents):
	def __init__(self, label_text):
		super().__init__(True)
		self.SearchBar = QT_Line_Editor().setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/viewzoom.svg"))
		self.SearchBar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		self.Toggle = QT_Button().setStyleName("Dropdown").setText(label_text).setToolTip(label_text).setCheckable(True).setChecked(True).setFixedHeight(24).setLeftIcon(QIcon(PATH+"/Resources/down_arrow_thin.svg"))
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
	def dropdown(self, label_text: str) -> 'Dropdown':
		dropdown = Dropdown(label_text)
		self.Container.addWidget(dropdown)
		return dropdown
	def list(self, label_text: str):
		list = Search_List(label_text)
		self.Container.addWidget(list)
		return list
	def prop(self, type: Prop_Type, window = None) -> Union[IntProperty, BoolProperty, FloatProperty, EnumProperty]:
		if type == Prop_Type.FLOAT:
			prop = FloatProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.INT:
			prop = IntProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.BOOL:
			prop = BoolProperty()
			self.Container.addWidget(prop)
		elif type == Prop_Type.ENUM:
			prop = EnumProperty()
			self.Container.addWidget(prop)
		if window: window.Properties.append(prop)
		return prop