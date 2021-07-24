from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber, QTableWidget, QTableWidgetItem, QListWidget
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
		
		self.create_listwidget()
		self.show()
		
	def create_listwidget(self):
		vbox = QVBoxLayout()
		
		self.list = QListWidget()
		self.list.insertItem(0, "Apple")
		self.list.insertItem(1, "Banana")
		self.list.insertItem(2, "Orange")
		
		self.list.clicked.connect(self.listview_clicked)
		
		self.label = QLabel()
		self.label.setFont(QFont("Times New Roman", 13))
		
		vbox.addWidget(self.list)
		vbox.addWidget(self.label)
		self.setLayout(vbox)
		
	def listview_clicked(self):
		item = self.list.currentItem()
		self.label.setText("Current item: " + str(item.text()))
		self.label.setStyleSheet('color:red')
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())