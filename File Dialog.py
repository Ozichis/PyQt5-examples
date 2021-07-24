from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QFileDialog 
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
		
		vbox = QVBoxLayout()
		
		btn = QPushButton('Browse Profile Images')
		btn.clicked.connect(self.browse_image)
		vbox.addWidget(btn)
		
		self.label = QLabel("")
		vbox.addWidget(self.label)
		
		self.setLayout(vbox)
		
		self.show()
		
	def browse_image(self):
		fname = QFileDialog.getOpenFileName(self, 'Open File', '/storage/emulated/0', 'Joint Photographic Graphics' ' (*.png)')
		imagePath = fname[0]
		pixmap = QPixmap(imagePath)
		self.label.setPixmap(QPixmap(pixmap))
		self.resize(pixmap.width(), pixmap.height())
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())