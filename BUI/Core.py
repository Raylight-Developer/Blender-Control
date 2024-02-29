import sys, pip, os

pip.main(["install", "PySide6", "--user"])
pip.main(["install", "sympy", "--user"])

from typing import *
from enum import Enum
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import sympy, math, json
import bpy

PATH = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# TYPES--------------------------------------------------------------------------------------------

class Icon(Enum):
	SEARCH = ""
	I_DRIVER = "Drivers/I_DRIVER.svg"
	F_DRIVER = "Drivers/F_DRIVER.svg"
	B_DRIVER = "Drivers/B_DRIVER.svg"
	E_DRIVER = "Drivers/E_DRIVER.svg"
	P_DRIVER = "Drivers/P_DRIVER.svg"

# QT-----------------------------------------------------------------------------------------------

class QT_Icon(QPushButton):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setFixedSize(24,24)
		super().setIconSize(QSize(16,16))
		super().setObjectName("Def_Icon")

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setIcon(self, Icon: Icon):
		super().setIcon(QIcon(PATH + "/Resources/Icons/" + Icon.value))
		return self

	def show(self):
		super().show()
		return self
	
	def hide(self):
		super().hide()
		return self

class QT_Button(QPushButton):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setIconSize(QSize(16,16))
		self.aligned_icon = None

	def setStyleName(self, Style: str):
		super().setObjectName(Style)
		return self

	def setToolTip(self, Tip: str):
		super().setToolTip(Tip)
		return self

	def setText(self, Text: str):
		super().setText(Text)
		return self

	def setCheckable(self, Checkable:bool):
		super().setCheckable(Checkable)
		return self

	def setChecked(self, Checked:bool):
		super().setChecked(Checked)
		return self

	def setIcon(self, Icon: QIcon):
		super().setIcon(Icon)
		return self

	def setFixedSize(self, Width:int, Height:int):
		super().setFixedSize(Width, Height)
		return self

	def setFixedHeight(self, H: int):
		super().setFixedHeight(H)
		return self

	def setFixedWidth(self, W: int):
		super().setFixedWidth(W)
		return self

	def show(self):
		super().show()
		return self
	
	def hide(self):
		super().hide()
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

	def setLeftIcon(self, Icon: QIcon):
		self.aligned_icon = Icon
		self.update()
		return self

	def paintEvent(self, event):
		super().paintEvent(event)
		painter = QPainter(self)
		option = QStyleOption()
		option.initFrom(self)

		if self.aligned_icon:
			left_icon_rect: QRect = option.rect
			left_icon_rect.setSize(QSize(16,16))
			left_icon_rect.translate(5, (self.height()-16)/2)
			self.aligned_icon.paint(painter, left_icon_rect)

class QT_Floating_Button (QPushButton):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setIconSize(QSize(16,16))
		super().setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
		super().setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.WindowStaysOnTopHint)

		self.Drag_Pos = QPoint(0,0)

	def setStyleName(self, Style: str):
		super().setObjectName(Style)
		return self

	def setToolTip(self, Tip: str):
		super().setToolTip(Tip)
		return self

	def setText(self, Text: str):
		super().setText(Text)
		return self

	def setCheckable(self, Checkable:bool):
		super().setCheckable(Checkable)
		return self

	def setChecked(self, Checked:bool):
		super().setChecked(Checked)
		return self

	def setIcon(self, Icon: QIcon):
		super().setIcon(Icon)
		return self

	def setFixedSize(self, Width:int, Height:int):
		super().setFixedSize(Width, Height)
		return self

	def setFixedHeight(self, H: int):
		super().setFixedHeight(H)
		return self

	def setFixedWidth(self, W: int):
		super().setFixedWidth(W)
		return self
	
	def show(self):
		super().show()
		return self
	
	def hide(self):
		super().hide()
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

	def mousePressEvent(self, Event: QMouseEvent):
		if Event.button() == Qt.MouseButton.RightButton:
			self.Drag_Pos = Event.pos()
		super().mousePressEvent(Event)

	def mouseMoveEvent(self, Event: QMouseEvent): 
		if Event.buttons() & Qt.MouseButton.RightButton:
			self.move(self.mapToParent(Event.pos() - self.Drag_Pos))
		super().mouseMoveEvent(Event)

class QT_Option(QComboBox):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
		super().setStyleSheet("QComboBox::down-arrow { image: url(" + PATH +"/Resources/Icons/Directions/ARROW_DOWN.svg); }")

	def setStyleName(self, Style: str):
		super().setObjectName(Style)
		return self

	def setToolTip(self, Tip: str):
		super().setToolTip(Tip)
		return self

	def setText(self, Text: str):
		super().setText(Text)
		return self

	def addItem(self, Text: str):
		super().addItem(Text)
		return self

	def setFixedSize(self, Width:int, Height:int):
		super().setFixedSize(Width, Height)
		return self

	def setFixedHeight(self, H: int):
		super().setFixedHeight(H)
		return self

	def setFixedWidth(self, W: int):
		super().setFixedWidth(W)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Linear_Contents(QWidget):
	def __init__(self, Vertical: bool = False, Aligned: bool = False):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		
		self.Linear_Layout = QT_Linear_Layout(Vertical, Aligned)
		super().setLayout(self.Linear_Layout)

	def addWidget(self, Widget:QWidget):
		self.Linear_Layout.addWidget(Widget)
		return self

	def clear(self):
		for i in range(self.Linear_Layout.count()):
			self.Linear_Layout.itemAt(i).widget().hide()
			self.Linear_Layout.itemAt(i).widget().deleteLater()
		return self

	def setSpacing(self, Spacing: int):
		self.Linear_Layout.setSpacing(Spacing)
		return self

	def children(self):
		return self.Linear_Layout.children()
	
	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Line_Editor(QLineEdit):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		self.aligned_icon = None

	def setText(self, Text: str):
		super().setText(Text)
		return self

	def selectAll(self):
		super().selectAll()
		return self

	def setFocus(self):
		super().setFocus()
		return self

	def setCursorPosition(self, Position: int):
		super().setCursorPosition(Position)
		return self

	def setValidator(self, Validator: QValidator):
		super().setValidator(Validator)
		return self

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def show(self):
		super().show()
		return self
	
	def hide(self):
		super().hide()
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Linear_Layout(QBoxLayout):
	def __init__(self, Vertical: bool = True, Aligned: bool = False):
		if Vertical:
			super().__init__(QBoxLayout.Direction.TopToBottom)
			super().setAlignment(Qt.AlignmentFlag.AlignTop)
		else:
			super().__init__(QBoxLayout.Direction.LeftToRight)
			super().setAlignment(Qt.AlignmentFlag.AlignLeft)

		if Aligned: super().setSpacing(0)
		else: super().setSpacing(4)
		super().setContentsMargins(0,0,0,0)

	def addWidget(self, Widget:QWidget):
		super().addWidget(Widget)
		return self

	def setSpacing(self, Spacing: int):
		super().setSpacing(Spacing)
		return self

	def clear(self):
		for i in range(self.count()):
			self.itemAt(i).widget().hide()
			self.itemAt(i).widget().deleteLater()
		return self

class QT_Scroll_Area(QScrollArea):
	def __init__(self, Vertical: bool = True):
		super().__init__()
		super().setWidgetResizable(True)
		super().setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
		super().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
		self.Contents = QT_Linear_Contents(Vertical)
		self.Contents.setContentsMargins(5,5,5,5)
		self.Contents.Linear_Layout.setSpacing(5)
		self.setWidget(self.Contents)

		if Vertical:
			super().setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
			super().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
		else:
			super().setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
			super().setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

	def addWidget(self, Widget):
		self.Contents.addWidget(Widget)
		return self

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setContentsStyleName(self, Name: str):
		self.Contents.setObjectName(Name)
		return self

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Slider(QSlider):
	def __init__(self, Vertical: bool = False):
		if Vertical: super().__init__(Qt.Orientation.Vertical)
		else: super().__init__(Qt.Orientation.Horizontal)
		super().setContentsMargins(0,0,0,0)

	def setToolTip(self, Tip: str):
		super().setToolTip(Tip)
		return self

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setRange(self, Min: int, Max: int):
		super().setRange(Min, Max)
		return self

	def setValue(self, Value):
		super().setValue(Value)
		return self

	def setMinimum(self, Value: int = 0):
		super().setMinimum(Value)
		return self

	def setMaximum(self, Value: int = 0):
		super().setMaximum(Value)
		return self

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self
	
	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Splitter(QSplitter):
	def __init__(self, Vertical: bool = True):
		if Vertical: super().__init__(Qt.Orientation.Vertical)
		else: super().__init__(Qt.Orientation.Horizontal)
		super().setHandleWidth(2)
		super().setContentsMargins(0,0,0,0)

	def addWidget(self, Widget):
		super().addWidget(Widget)
		return self

	def setHandleWidth(self, Width):
		super().setHandleWidth(Width)
		return self

	def setSizes(self, Sizes):
		super().setSizes(Sizes)
		return self
	
	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Label(QLabel):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(5,0,5,0)
	
	def setLayout(self, Layout: QLayout):
		super().setLayout(Layout)
		return self

	def setText(self, Text: str):
		super().setText(Text)
		return self

	def setToolTip(self, Tip: str):
		super().setToolTip(Tip)
		return self

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setStyleName(self, Name: str):
		super().setObjectName(Name)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Tree(QWidget):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Widget(QWidget):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)

	def setLayout(self, Layout: QLayout):
		super().setLayout(Layout)
		return self

	def setFixedHeight(self, Height: int):
		super().setFixedHeight(Height)
		return self

	def setFixedWidth(self, Width: int):
		super().setFixedWidth(Width)
		return self

	def setFixedSize(self, Width: int, Height: int):
		super().setFixedSize(Width, Height)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Window(QMainWindow):
	def __init__(self):
		super().__init__()
		super().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
		super().setFocusPolicy(Qt.FocusPolicy.StrongFocus)

	def setWindowTitle(self, Title: str):
		super().setWindowTitle(Title)
		return self

	def setWindowIcon(self, Icon: QIcon):
		super().setWindowIcon(Icon)
		return self

	def setBaseSize(self, Width, Height):
		super().setBaseSize(Width ,Height)
		return self

	def setCentralWidget(self, Widget):
		super().setCentralWidget(Widget)
		return self

	def move(self, X, Y):
		super().move(X, Y)
		return self

	def show(self):
		super().show()
		return self

	def setWindowFlags(self, Flags):
		super().setWindowFlags(Flags)
		return self

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class Int_Slider(QT_Slider):
	def __init__(self):
		super().__init__()

		self.setRange(0, 1)

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

		self.setRange(0, 1)

	def setRange(self, min, max):
		super().setRange(int(sympy.sympify(f"{min} * {self.divider}")), int(sympy.sympify(f"{max} * {self.divider}")))

	def setPrecision(self, precision):
		self.precision = precision
		self.divider = int("1"+"0"*self.precision)

	def setValue(self, value):
		super().setValue(int(sympy.sympify(f"{value} * {self.divider}")))

	def val(self):
		return sympy.sympify(f"{self.value()} / {self.divider}")

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
		painterPath.addText(QPointF(self.geometry().width() / 2 - QFontMetrics(self.font()).horizontalAdvance(f"{{:.{self.precision}f}}".format(sympy.sympify(f"({self.value()} / {self.divider}) / {2}"))), self.geometry().height() * 0.75), self.font() , f"{{:.{self.precision}f}}".format(sympy.sympify(f"{self.value()} / {self.divider}")))
		painter.strokePath(painterPath, QPen(QColor(250,250,250), 0.5))
		painter.fillPath(painterPath, QColor(250,250,250))