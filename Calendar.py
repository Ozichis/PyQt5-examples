from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize
import random
r = random.randint(1, 10000)

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.create_ui_()
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		
		vbox = QVBoxLayout()
		calendar = QCalendarWidget()
		calendar.setGridVisible(True)
		
		vbox.addWidget(calendar)
		
		self.setLayout(vbox)
		self.show()
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())