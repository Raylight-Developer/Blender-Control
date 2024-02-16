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