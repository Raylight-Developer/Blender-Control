from QT_Core import *

class Int_Slider(QT_Slider):
	def __init__(self, Vertical: bool = False):
		super().__init__(Vertical)

		self.setRange(0,1)
		self.setStyleSheet("""
QSlider::add-page:horizontal { background: rgb(75,75,75); }
QSlider::sub-page:horizontal { background: rgb(100,100,250); }
QSlider::handle:horizontal { background: transparent; width: 0px;}
""")

	def mousePressEvent(self, event: QMouseEvent):
		if event.button() == Qt.MouseButton.LeftButton and not self.isSliderDown():
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
				Value = self.style().sliderValueFromPosition(self.minimum(), self.maximum(), Pos - Min, Max - Min)
				self.setSliderPosition(Value)
		super().mousePressEvent(event)

	def paintEvent(self, event):
		QSlider.paintEvent(self, event)
		painter = QPainter(self)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painterPath = QPainterPath()
		painterPath.addText(QPointF(self.geometry().width() / 2 - QFontMetrics(self.font()).horizontalAdvance(str(self.value())) / 2, self.geometry().height() * 0.75), self.font() , str(self.value()))
		painter.strokePath(painterPath, QPen(QColor(250,250,250), 0.5))
		painter.fillPath(painterPath, QColor(250,250,250))

class Float_Slider(QT_Slider):
	def __init__(self):
		super().__init__()
		self.precision = 3
		self.divider = 1000

		self.setRange(0, self.divider)

	def mouseMoveEvent(self, event: QMouseEvent):
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
		super().mouseMoveEvent(event)

	def paintEvent(self, event):
		QSlider.paintEvent(self, event)
		painter = QPainter(self)
		painter.setRenderHint(QPainter.RenderHint.Antialiasing)
		painterPath = QPainterPath()
		painterPath.addText(QPointF(self.geometry().width() / 2 - QFontMetrics(self.font()).horizontalAdvance(f"{{:.{self.precision}f}}".format(self.value() / self.precision)) / 2, self.geometry().height() * 0.75), self.font() , f"{{:.{self.precision}f}}".format(self.value() / self.divider))
		painter.strokePath(painterPath, QPen(QColor(250,250,250), 0.5))
		painter.fillPath(painterPath, QColor(250,250,250))

#--------------------------------------------------------------------------------------------------

class Type(Enum):
	INT = 0
	BOOL = 1
	FLOAT = 2

class Icon(Enum):
	NONE = 0

class IntProperty(QWidget):
	def __init__(self, Label: str = "Value"):
		super().__init__(False)

		self.Label = QPushButton()
		self.Label.setText(Label)
		self.Input = Int_Slider().setRange(0,1)
		self.Line = QLineEdit()
		self.Line.setValidator(QIntValidator(0, 1))
		self.Popup_Line = QMenu()
		self.Popup_Line.layout().addWidget(self.Line)

		self.addWidget(self.Label)
		self.addWidget(self.Input)
		#self.setStretch({0:0,1:1})

		self.Label.clicked.connect(self.textEdit)
		self.Line.textChanged.connect(self.updateSlider)
		self.Line.returnPressed.connect(self.updateText)

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

	def setValue(self, Value = 0):
		self.Input.setValue(int(Value))
		return self

	def updateSlider(self):
		self.Input.setValue(int(self.Line.text()))

	def textEdit(self):
		self.Line.setText(str(self.Input.value()))
		self.Line.setFixedSize(self.Input.width(), self.Input.height())
		self.Line.selectAll().setFocus()
		self.Popup_Line.setFixedSize(self.Input.width(), self.Input.height())
		self.Popup_Line.exec(self.mapToGlobal(self.Input.pos()))

	def updateText(self):
		self.Popup_Line.close()

class BoolProperty(QT_Button):
	def __init__(self):
		super().__init__()
		super().setCheckable(True)
	def expression(expression: str = ""): pass
	def execute(self, driver):
		try: exec(self.expr)
		except: pass

class FloatProperty(QT_Linear_Contents):
	def __init__(self):
		super().__init__(False)
		self.driver_expression = ""
		self.keyframe_expression = ""

		self.label = ""
		self.icon = Icon.NONE

		self.min = 0
		self.max = 1

		self.input = QT_Line_Editor().setValidator(QDoubleValidator(0, 1, 10))

		self.slider = Float_Slider()

		self.keyframer = QT_Button().setCheckable(True).setIcon(QIcon("./Resources/keyframe.svg"))

		self.addWidget(self.slider).addWidget(self.input).addWidget(self.keyframer)
		self.input.hide()

		self.slider.valueChanged.connect(self.execute_expression)
		self.keyframer.clicked.connect(lambda clicked: self.execute_keyframe(clicked))

		self.input.editingFinished.connect(self.cancelValueChange)
		self.input.focusOutEvent = self.cancelValueChange

	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.RightButton:
			self.slider.hide()
			self.input.show()
			self.input.setFocus()

	def cancelValueChange(self, event = None):
		self.slider.show()
		self.input.hide()

	def set_driver_expression(self, driver_expression: str = ""):
		self.driver_expression = driver_expression
	def set_keyframe_expression(self, keyframe_expression: str = ""):
		self.keyframe_expression = keyframe_expression
	def set_label(self, value: str = ""):
		self.label = value
	def set_icon(self, value: Icon = Icon.NONE):
		self.icon = value
	def set_min(self, value : float = 0.0):
		self.min = value
		self.input.setValidator(QDoubleValidator(self.min, self.max, 10))
	def set_max(self, value : float = 1.0):
		self.max = value
		self.input.setValidator(QDoubleValidator(self.min, self.max, 10))
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
		else:
			self.keyframer.setIcon(QIcon("./Resources/keyframe.svg"))
		try: exec(self.keyframe_expression)
		except: pass
	def execute_expression(self, driver):
		try: exec(self.driver_expression)
		except: pass

class Row(QT_Linear_Contents):
	def __init__(self):
		super().__init__()
	def column(self, align: bool = False) -> 'Column':
		column = Column()
		self.addWidget(column)
		return column
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			self.addWidget(prop)
		return prop

class Column(QT_Linear_Contents):
	def __init__(self):
		super().__init__(True)
	def row(self, align: bool = False) -> 'Row':
		row = Row()
		self.addWidget(row)
		return row
	def prop(self, type: Type = Type.FLOAT, text: str = '', icon: Icon = Icon.NONE) -> Union[IntProperty, BoolProperty, FloatProperty]:
		if type == Type.FLOAT:
			prop = FloatProperty()
			self.addWidget(prop)
		return prop