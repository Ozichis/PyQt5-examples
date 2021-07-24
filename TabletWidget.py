from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber, QTableWidget, QTableWidgetItem
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
		self.create_table()
		self.show()
		
	def create_table(self):
		vbox = QVBoxLayout()
		table = QTableWidget()
		
		table.setRowCount(5)
		table.setColumnCount(3)
		
		table.setItem(0, 0, QTableWidgetItem( "Name"))
		table.setItem(0, 1,  QTableWidgetItem('Email'))
		table.setItem(0, 2, QTableWidgetItem('Phone'))
		
		table.setItem(1, 0, QTableWidgetItem('Ozichi'))
		table.setItem(1, 1, QTableWidgetItem('orieozichi@gmail.com'))
		table.setItem(1, 2, QTableWidgetItem('0479494793'))
		
		vbox.addWidget(table)
		self.setLayout(vbox)
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())