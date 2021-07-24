from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFontComboBox
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.create_ui_()
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		
		self.l()
		self.show()
		
	def l(self):
		vbox = QVBoxLayout()
		
		font_combo = QFontComboBox()
		
		font_combo.setFontFilters(QFontComboBox.MonospacedFonts)
		
		vbox.addWidget(font_combo)
		
		self.setLayout(vbox)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())