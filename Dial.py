from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber, QTableWidget, QTableWidgetItem, QListWidget, QDial
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
		
		self.create_dial()
		self.show()
	
	def create_dial(self):
		hbox = QHBoxLayout()
		
		self.label = QLabel()
		self.label.setFont(QFont("Times New Roman", 15))
		
		self.dial = QDial()
		self.dial.setMinimum(0)
		self.dial.setMaximum(100)
		self.dial.setValue(30)
		self.dial.valueChanged.connect(self.on_dial)
		hbox.addWidget(self.label)
		hbox.addWidget(self.dial)
		
		self.setLayout(hbox)
		
	def on_dial(self):
		value = self.dial.value()
		self.label.setText("Dial Value : {}".format(value))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())