#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox
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
		self.create_checkbox()
		self.show()
		
	def create_checkbox(self):
		grpox = QGroupBox( "Are you tired of entering pins")
		grpox.setFont(QFont('Times New Roman', 20))
		hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		
		self.check1 = QCheckBox('✔Yes')
		hbox.addWidget(self.check1)
		self.check1.toggled.connect(self.on_toggles)
		self.check2 = QCheckBox('✖No')
		hbox.addWidget(self.check2)
		self.check2.toggled.connect(self.on_toggles)
		
		self.label = QLabel('Hello', self)
		self.label.setFont(QFont('Sanserif', 15))
		vbox.addWidget(self.label)
		
		grpox.setLayout(hbox)
		vbox.addWidget(grpox)
		
		self.setLayout(vbox)
		
	def on_toggles(self):
		if self.check1.isChecked():
			self.label.setText("Your Answer was {}".format(self.check1.text()) + ", But We used it for security")
		if self.check2.isChecked():
			self.label.setText('Your Answer was {}'.format(self.check2.text()))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
	