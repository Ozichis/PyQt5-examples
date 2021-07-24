#Modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
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
		self.grid_layout()
		self.show()
		
	def grid_layout(self):
		gpbox = QGroupBox('Do you know  your pin')
		gpbox.setFont(QFont('Times New Roman', 12))
		
		grid = QGridLayout()
		vbox = QVBoxLayout()
		
		btn = QPushButton('Enter Pin', self)
		btn.setIcon(QIcon('/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg'))
		btn.setIconSize(QSize(40,50))
		grid.addWidget(btn, 0,0)
		
		btn1 = QPushButton('Skip Pin', self)
		btn1.setIcon(QIcon('/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg'))
		btn1.setIconSize(QSize(40,50))
		grid.addWidget(btn1, 0,1)
		
		btn2 = QPushButton('Hit Pin', self)
		btn2.setIcon(QIcon('/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg'))
		btn2.setIconSize(QSize(40,50))
		grid.addWidget(btn2, 1,0)
		
		gpbox.setLayout(grid)
		
		vbox.addWidget(gpbox)
		self.setLayout(vbox)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())
	