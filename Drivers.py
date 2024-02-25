try: from .BUI import *
except: from BUI import *
if TYPE_CHECKING:
	from BUI import *

class B_DRIVER(QT_Linear_Contents):
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
		self.label_icon = QT_Icon().hide()
		self.label = QT_Label().setText("Boolean").setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg")).hide()

		self.input = QT_Button().setStyleName("Bool_Prop").setCheckable(True)
		self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

		self.addWidget(self.label_icon).addWidget(self.label).addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))
		self.input.clicked.connect(self.executePythonExpression)

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		if label_icon:
			self.label_icon.setIcon(label_icon)
			self.label_icon.show()
		else: self.label_icon.hide()
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
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_ON.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg"))
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

class E_DRIVER(QT_Linear_Contents):
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
		self.label_icon = QT_Icon().hide()
		self.label = QT_Label().setText("Enum").setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg")).hide()

		self.input = QT_Option().addItem("Item")
		
		self.addWidget(self.label_icon).addWidget(self.label).addWidget(self.input).addWidget(self.keyframer)
		self.keyframer.clicked.connect(lambda clicked: self.executeAddRemoveKeyframe(clicked))

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		if label_icon:
			self.label_icon.setIcon(label_icon)
			self.label_icon.show()
		else: self.label_icon.hide()
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
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_ON.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg"))
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

class F_DRIVER(QT_Linear_Contents):
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
		self.label_icon = QT_Icon().hide()
		self.label = QT_Label().setText("Float").setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg")).hide()

		self.input = QT_Line_Editor().setValidator(QDoubleValidator(decimals = 10)).hide()
		self.slider = Float_Slider().setToolTip(self.label_text)

		self.addWidget(self.label_icon).addWidget(self.label).addWidget(self.slider).addWidget(self.input).addWidget(self.keyframer)
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

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
	def setLabelIcon(self, label_icon: Icon):
		if label_icon:
			self.label_icon.setIcon(label_icon)
			self.label_icon.show()
		else: self.label_icon.hide()
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
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_ON.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg"))
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
	# FloatProperty Methods ---------------------

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
	def setMin(self, value : float = 0.0):
		self.min = value
		self.input.setValidator(QDoubleValidator(decimals = 10))
		self.slider.setRange(value, self.max)
		return self
	def setMax(self, value : float = 1.0):
		self.max = value
		self.input.setValidator(QDoubleValidator(decimals = 10))
		self.slider.setRange(self.min, value)
		return self
	def set_use_soft_limits(self, value : bool = True): pass
	def setSoftMin(self, value : float = 0.0):
		self.slider.setRange(value, self.max)
		return self
	def setSoftMax(self, value : float = 1.0):
		self.slider.setRange(self.min, value)
		return self
	def setStep(self, value : float = 0.1): pass
	def setPrecision(self, value: int = 3):
		self.slider.precision = value

class I_DRIVER(QT_Linear_Contents):
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
		self.label_icon = QT_Icon().hide()
		self.label = QT_Label().setText("Integer").setFixedWidth(120)
		self.keyframer = QT_Button().setFixedWidth(24).setStyleName("Key").setCheckable(True).setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg")).hide()

		self.input = QT_Line_Editor().setValidator(QIntValidator(0, 1))
		self.slider = Int_Slider().setToolTip(self.label_text)
		self.decrease = QT_Button().setStyleName("Int_L").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_LEFT.svg"))
		self.increase = QT_Button().setStyleName("Int_R").setFixedWidth(24).setIcon(QIcon(PATH+"/Resources/Icons/Directions/ARROW_RIGHT.svg"))

		self.addWidget(self.label_icon).addWidget(self.label).addWidget(self.decrease).addWidget(self.slider).addWidget(self.increase).addWidget(self.input).addWidget(self.keyframer)
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

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	# Shared Property Methods -------------------
	def setLabel(self, label: str):
		self.label_text = label
		self.label.setText(label).setToolTip(self.label_text)
		return self
	def setLabelIcon(self, label_icon: Icon):
		if label_icon:
			self.label_icon.setIcon(label_icon)
			self.label_icon.show()
		else: self.label_icon.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
		return self
	def setAddKeyframeExpresssion(self, keyframe_expression: str):
		self.add_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression and self.remove_keyframe_expression: self.keyframer.show()
		return self
	def setRemoveKeyframeExpresssion(self, keyframe_expression: str):
		self.remove_keyframe_expression = keyframe_expression
		if self.add_keyframe_expression and self.remove_keyframe_expression: self.keyframer.show()
		return self
	def executeAddRemoveKeyframe(self, keyframe: bool):
		if self.add_keyframe_expression and self.remove_keyframe_expression:
			if keyframe:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_ON.svg"))
				try: exec(self.add_keyframe_expression)
				except Exception as error: print(error)
			else:
				self.keyframer.setIcon(QIcon(PATH+"/Resources/Icons/Toggles/TOGGLE_KEYFRAME_OFF.svg"))
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
		self.slider.setRange(value, self.slider.maximum())
		self.input.setValidator(QIntValidator(value, self.max))
		return self
	def setMax(self, value : int = 1):
		self.max = value
		self.slider.setRange(self.slider.minimum(), value)
		self.input.setValidator(QIntValidator(self.min, value))
		return self
	def set_use_soft_limits(self, value : bool = True): pass
	def setSoftMin(self, value : int = 0):
		self.slider.setRange(value, self.slider.maximum())
		return self
	def setSoftMax(self, value : int = 1):
		self.slider.setRange(self.slider.minimum(), value)
		return self
	def setStep(self, value : int = 1): pass
	
class P_DRIVER(QT_Linear_Contents):
	python_driver_expression = None
	label_text = None
	label_icon = None
	label_visibility = True

	label : QT_Label

	def __init__(self):
		super().__init__()
		self.setFixedHeight(24)
		self.label_icon = QT_Icon().hide()
		self.label = QT_Label().setText("Python").setFixedWidth(120)
		self.input = QT_Button().setStyleName("Bool_Prop").setText(self.label_text).setToolTip(self.label_text)
		self.input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

		self.addWidget(self.label_icon).addWidget(self.label).addWidget(self.input)
		self.input.clicked.connect(self.executePythonExpression)

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
	# Shared Property Methods -------------------
	def setLabelIcon(self, label_icon: Icon):
		if label_icon:
			self.label_icon.setIcon(label_icon)
			self.label_icon.show()
		else: self.label_icon.hide()
	def setLabelIsVisible(self, visible: bool):
		if visible: self.label.show()
		else: self.label.hide()
	def setPythonDriver(self, python_driver_expression: str):
		self.python_driver_expression = python_driver_expression
	def executePythonExpression(self, driver: bool):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)