#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize
import random
r = random.randint(1, 10000)
#Window

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.create_ui_()
		
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		self.create_text()
		self.show()
		
	def create_text(self):
		text = QTextEdit(self)
		text.setFont(QFont( "Times New Roman" , 14))
		self.setCentralWidget(text)
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
	