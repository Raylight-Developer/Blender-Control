# Blender Control
 
<style>
	* {
		font-family: 'Courier New', monospace;
		background: transparent;
		color: rgb(155,220,255);
	}
	h1 {
		margin-left: 2.5%;
		color: rgb(255,255,255);
	}
	h2 {
		border-top-left-radius: 10px;
		border-top-right-radius: 10px;
		background: rgb(0,0,0);
		margin: 0px;
		margin-left: 5%;
		padding: 10px;
		tab-size: 4;
		white-space: pre-wrap;
	}
	body {
		background: rgb(15,15,15);
	}
	pre {
		padding: 30px;
		padding-top: 15px;
		padding-bottom: 15px;
		margin-top: 0px;
		margin-left: 5%;
		border-bottom-left-radius: 10px;
		border-bottom-right-radius: 10px;
		background: rgb(30,30,30);
		font-size: 16px;
		font-weight: 700;
		tab-size: 4;
		white-space: pre-wrap;
		word-wrap: break-word;
	}
	desc {
		color:rgb(255,255,255);
		font-size: 16px;
		font-weight: 500;
	}
	class {
		color: rgb(80, 200, 175);
	}
	def {
		color: rgb(220, 220, 170);
	}
	func {
		color: rgb(200, 135, 190);
	}
	brck {
		color: rgb(255,215,0);
	}
	enum {
		color: rgb(185, 160, 245);
	}
	opt {
		color: rgb(255, 115, 115);
	}
	req {
		color: rgb(115, 255, 120);
	}
	str {
		color: rgb(205, 145, 120);
	}
	type {
		color: rgb(85, 155, 215);
	}
</style>
<body>
<h1>Enum</h1>
<h2><func>Enum</func> <class>Prop_Type</class></h2>
<pre>
<enum>INT
BOOL
FLOAT
ENUM</enum>
</pre>

<h2><func>Enum</func> <class>Icon</class></h2>
<pre>
<enum>SEARCH</enum>
</pre>

<h1>Layout Items</h1>

<h2><class>Row</class></h2>
<pre>
<desc>Layout to add items horizontally.</desc>
</pre>

<h2><class>Column</class></h2>
<pre>
<desc>Layout to add items vertically.</desc>
</pre>

<h2><class>Box</class></h2>
<pre>
<desc>Layout to add items vertically, while adding an outline.</desc>
</pre>

<h2><class>Dropdown</class></h2>
<pre>
<desc>Layout to add items vertically. Can be expanded and collapsed.</desc>

<def>.setLabel</def><brck>(</brck> text : <class>String</class> <brck>)</brck>
	<desc>Set the labels and the tooltips text.</desc>
</pre>

<h2><class>Search_List</class></h2>
<pre>
<desc>Layout to add items vertically. Can be expanded and collapsed. Has a Searchbar.</desc>

<def>.setLabel</def><brck>(</brck> text : <class>String</class> <brck>)</brck>
	<desc>Set the labels and the tooltips text.</desc>
</pre>

<h1>Layout Operators</h1>

<h2><def>row</def></h2>
<pre>
<def>.row</def><brck>()</brck>
<func>return</func> <class>Row</class>
</pre>

<h2><def>column</def></h2>
<pre>
<def>.column</def><brck>()</brck>
<func>return</func> <class>Column</class>
</pre>

<h2><def>box</def></h2>
<pre>
<def>.box</def><brck>()</brck>
<func>return</func> <class>Box</class>
</pre>

<h2><def>dropdown</def></h2>
<pre>
<def>.dropdown</def><brck>(</brck>
	text <opt>(optional)</opt> : <class>String</class>
<brck>)</brck>
<func>return</func> <class>Dropdown</class>
</pre>

<h2><def>list</def></h2>
<pre>
<def>.list</def><brck>(</brck>
	text <opt>(optional)</opt> : <class>String</class>
<brck>)</brck>
<func>return</func> <class>Search_List</class>
</pre>

<h2><def>prop</def></h2>
<pre>
<def>.prop</def><brck>(</brck>
	prop_type <req>(required)</req> : <class>Prop_Type.</class><enum>ENUM</enum>
	register  <opt>(optional)</opt> : <class>self</class>
<brck>)</brck>
<func>return</func> <class>[ IntProperty | BoolProperty | FloatProperty | EnumProperty ]</class>

prop_type : <desc>Type of the driver, set from the Enum.</desc>
register  : <desc>If set to self, the property will be refreshed with the changes made in blender. Else its value will not change in sync with blender.</desc>
</pre>

<h1>Properties</h1>

<h2><class>IntProperty </class></h2>
<pre>
<def>.setLabelIsVisible</def><brck>(</brck>visible : <class>Boolean</class><brck>)</brck>
	<desc>Whether the label should be visible.</desc>

<def>.setLabel</def><brck>(</brck> text : <class>String</class> <brck>)</brck>
	<desc>Set the labels and the tooltips text.</desc>

<def>.setIcon</def><brck>(</brck> icon : <class>Icon.</class><enum>ENUM</enum> <brck>)</brck>
	<desc>Set the Icon of the label.</desc>

<def>.setMin</def><brck>(</brck> min : <class>Int</class> <brck>)</brck>
	<desc>Set Absolute Min.</desc>

<def>.setMax</def><brck>(</brck> max : <class>Int</class> <brck>)</brck>
	<desc>Set Absolute Max.</desc>

<def>.setSoftMin</def><brck>(</brck> soft_min : <class>Int</class> <brck>)</brck>
	<desc>Set Slider Min.</desc>

<def>.setSoftMax</def><brck>(</brck> soft_max : <class>Int</class> <brck>)</brck>
	<desc>Set Slider Max.</desc>
</pre>

<h2><class>FloatProperty </class></h2>
<pre>
<def>.setLabelIsVisible</def><brck>(</brck>visible : <class>Boolean</class><brck>)</brck>
	<desc>Whether the label should be visible.</desc>

<def>.setLabel</def><brck>(</brck> text : <class>String</class> <brck>)</brck>
	<desc>Set the labels and the tooltips text.</desc>

<def>.setIcon</def><brck>(</brck> icon : <class>Icon.</class><enum>ENUM</enum> <brck>)</brck>
	<desc>Set the icon of the label.</desc>

<def>.setMin</def><brck>(</brck> min : <class>Float</class> <brck>)</brck>
	<desc>Set absolute min.</desc>

<def>.setMax</def><brck>(</brck> max : <class>Float</class> <brck>)</brck>
	<desc>Set absolute max.</desc>

<def>.setSoftMin</def><brck>(</brck> soft_min : <class>Float</class> <brck>)</brck>
	<desc>Set slider Min.</desc>

<def>.setSoftMax</def><brck>(</brck> soft_max : <class>Float</class> <brck>)</brck>
	<desc>Set slider Max.</desc>

<def>.setDecimals</def><brck>(</brck> decimals : <class>Int</class> <brck>)</brck>
	<desc>Set displayed decimal places.</desc>
</pre>

<h2><class>BoolProperty </class></h2>
<pre>
</pre>

<h2><class>EnumProperty</class></h2>
<pre>
</pre>
</body>