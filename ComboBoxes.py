#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize
import random
r = random.randint(1, 10000)
#Window

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.create_ui_()
		
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		self.create_combo()
		self.show()
		
	def create_combo(self):
		vbox = QVBoxLayout()
		
		self.combobox = QComboBox()
		self.combobox.addItem('Apple')
		self.combobox.addItem('Banana')
		self.combobox.addItem('Orange')
		self.combobox.addItem('Pineappple')
		self.combobox.addItem('Grapes')
		self.combobox.currentTextChanged.connect(self.combo_changed)
		
		self.label = QLabel()
		self.label.setFont(QFont( "Times New Roman", 14))
		
		
		vbox.addWidget(self.combobox)
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		
	def combo_changed(self):
		text = self.combobox.currentText()
		self.label.setText("You have chosen to buy {}" .format(text))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
	