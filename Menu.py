from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QCompleter, QLineEdit, QMessageBox, QLCDNumber, QTableWidget, QTableWidgetItem, QListWidget, QAction
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QRect, QSize
import random
r = random.randint(1, 10000)

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.create_ui_()
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		
		self.createMenu()
		self.show()
		
	def createMenu(self):
		main_menu = self.menuBar()
		file_menu = main_menu.addMenu("File")
		edit_menu = main_menu.addMenu("Edit")
		view_menu = main_menu.addMenu("View")
		
		copyAction = QAction(QIcon("/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg"), "Copy", self)
		copyAction.setShortcut("CTRL-C")
		file_menu.addAction(copyAction)
		
		saveAction = QAction(QIcon("/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg"), "Save", self)
		saveAction.setShortcut("CTRL-S")
		edit_menu.addAction(saveAction)
		
		exitAction = QAction(QIcon("/storage/emulated/0/Download/Attachments/OZICHI ORIE.jpg"), "Exit", self)
		exitAction.setShortcut("CTRL-X")
		exitAction.triggered.connect(self.exit_window)
		file_menu.addAction(exitAction)
		
		#Toolbar
		self.toolbar = self.addToolBar("Toolbar")
		self.toolbar.addAction(copyAction)
		self.toolbar.addAction(saveAction)
		self.toolbar.addAction(exitAction)
		
	def exit_window(self):
		self.close()
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())