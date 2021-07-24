from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber, QTableWidget, QTableWidgetItem, QListWidget, QDial, QDockWidget
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QRect, QSize, Qt
import random
r = random.randint(1, 10000)

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.create_ui_()
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		
		self.create_dock()
		self.show()
		
	def create_dock(self):
		dock = QDockWidget("Dockable", self)
		
		listwidget = QListWidget()
		
		list_items = [ "Orange" , "Banana" , "Apple", "Pineapple", "Mango", "Lemon"]
		
		listwidget.addItems(list_items)
		
		self.setCentralWidget(QTextEdit())
		
		dock.setWidget(listwidget)
		
		self.addDockWidget(Qt.RightDockWidgetArea, dock)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())