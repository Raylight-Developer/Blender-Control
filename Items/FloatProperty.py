from BUI import *

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

	def setUID(self, uid):
		self.uid = super().setUID(uid)
		return self.uid
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