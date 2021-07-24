from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QComboBox, QTextEdit, QMainWindow, QSpinBox, QCheckBox, QCalendarWidget, QPlainTextEdit, QMessageBox
import sys
from PyQt5.QtGui import QIcon, QFont
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
		self.plain_textedit = QPlainTextEdit()
		self.plain_textedit.setPlaceholderText('Enter your message')
		#self.plain_textedit.setReadOnly(True)
		
		text = "My message: "
		self.plain_textedit.appendPlainText(text+str(dir(self.plain_textedit)))
		
		QPushButton( "Buy", self).clicked.connect(self.alert)
		
		vbox.addWidget(self.plain_textedit)
		self.setLayout(vbox)
		self.show()
		
	def alert(self):
		pass
		QMessageBox.information(self, "I", str(self.plain_textedit.toPlainText()))
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())