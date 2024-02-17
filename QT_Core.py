from typing import Dict, Union
import math, json, sys, os
from enum import Enum
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

PATH = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

class QT_Button(QPushButton):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
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
			left_icon_size = self.aligned_icon.actualSize(left_icon_rect.size())
			left_icon_rect.setWidth(left_icon_size.width())
			left_icon_rect.translate(5,0)
			self.aligned_icon.paint(painter, left_icon_rect)


class QT_Floating_Button (QPushButton):
	def __init__(self):
		super().__init__()
		self.setContentsMargins(0,0,0,0)
		self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
		self.setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.WindowStaysOnTopHint)

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

class QT_Icon_Button(QToolButton):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		super().setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

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

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

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
	def __init__(self, Vertical: bool = False):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
		
		self.Linear_Layout = QT_Linear_Layout(Vertical)
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

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Line_Editor(QLineEdit):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(0,0,0,0)
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
			left_icon_size = self.aligned_icon.actualSize(left_icon_rect.size())
			left_icon_rect.setWidth(left_icon_size.width())
			left_icon_rect.translate(5,0)
			self.aligned_icon.paint(painter, left_icon_rect)

class QT_Linear_Layout(QBoxLayout):
	def __init__(self, Vertical: bool = True):
		if Vertical:
			super().__init__(QBoxLayout.Direction.TopToBottom)
			super().setAlignment(Qt.AlignmentFlag.AlignTop)
		else:
			super().__init__(QBoxLayout.Direction.LeftToRight)
			super().setAlignment(Qt.AlignmentFlag.AlignLeft)

		super().setSpacing(2)
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

	def setUID(self, uid: int):
		super().setWhatsThis(f"UID: {uid}")
		return uid + 1

class QT_Label(QLabel):
	def __init__(self):
		super().__init__()
		super().setContentsMargins(5,0,5,0)
		self.aligned_icon = None
	
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
			left_icon_size = self.aligned_icon.actualSize(left_icon_rect.size())
			left_icon_rect.setWidth(left_icon_size.width())
			left_icon_rect.translate(5,0)
			self.aligned_icon.paint(painter, left_icon_rect)

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