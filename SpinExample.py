#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize
import random
r = random.randint(1, 10000)
#Window

class Window(QSpinBox):
	def __init__(self):
		super().__init__()
		self.create_ui_()
		
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		self.create_spinbox()
		self.show()
	
	def create_spinbox(self):
		vbox = QVBoxLayout()
		
		self.spin = QSpinBox()
		self.spin.valueChanged.connect(self.spin_changed)
		
		self.label = QLabel()
		self.label.setFont(QFont("Times New Roman", 20))
		
		vbox.addWidget(self.spin)
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		
	def spin_changed(self):
		spin_value = self.spin.value()
		self.label.setText('Selected Amount : {}' .format(spin_value))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
	