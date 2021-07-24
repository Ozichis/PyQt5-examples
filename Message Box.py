from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox
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
		self.setWindowIcon(QIcon('/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg'))
		self.setGeometry(100, 100, 600, 300)
		
		vbox = QVBoxLayout()
		btn = QPushButton('Open Message Box', self)
		btn.clicked.connect(self.create_messagebox)
		
		vbox.addWidget(btn)
		
		self.setLayout(vbox)
		
		self.show()
		
	def create_messagebox(self):
		#message = QMessageBox.about(self, 'Info MessageBox', 'This is a messagebox')
		message = QMessageBox.question(self, 'Chat', 'Are you ready to chat',
																		QMessageBox.Yes | QMessageBox.No)
		if message == QMessageBox.Yes:
			m = QMessageBox.about(self, 'Yaya', 'Ok')
		else:
			m = QMessageBox.about(self, 'Yaya', 'Ok now')
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())