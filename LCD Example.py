from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
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
		
		self.lcd_number()
		self.show()
		
	def lcd_number(self):
		vbox = QVBoxLayout()
		self.lcd = QLCDNumber()
		self.lcd.setStyleSheet('background-color:red')
		vbox.addWidget(self.lcd)
		
		btn = QPushButton('Random Number Generator')
		btn.setStyleSheet('background-color:green')
		btn.clicked.connect(self.lcd_handler)
		vbox.addWidget(btn)
		
		self.setLayout(vbox)
		
	def lcd_handler(self):
		import random
		rando = random.randint(1, 200)
		self.lcd.display(rando)
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())