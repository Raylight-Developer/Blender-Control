from BUI import *

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
	def executePythonExpression(self, driver: str):
		if self.python_driver_expression:
			try: exec(self.python_driver_expression)
			except Exception as error: print(error)
	def executeBlenderFetch(self):
		if self.blender_fetch_expression:
			try: exec(self.blender_fetch_expression)
			except Exception as error: print(error)