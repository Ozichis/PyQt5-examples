from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFontComboBox
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QPen, QBrush, QTextDocument
from PyQt5.QtCore import Qt, QRectF


class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.create_ui_()
	def create_ui_(self):
		self.setWindowTitle('My Store')
		self.setGeometry(100, 100, 600, 300)
		self.show()
		
	def paintEvent(self, QPaintEvent):
		painter = QPainter(self)
		#painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))
		painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
		#painter.drawRect(100, 15, 300, 1000)
		
		painter.drawText(200, 400, "Welcome to my store")
		
		rect = QRectF(160, 450, 250, 25)
		
		painter.drawRect(rect)
		painter.drawEllipse(100, 100, 100, 100)
		painter.drawText(rect, Qt.AlignCenter, "Thanks for coming to our store")
		
		document = QTextDocument()
		rect2 = QRectF(0, 0, 250,250)
		
		document.setTextWidth(rect2.width())
		document.setHtml("<b>Store in GUI</b> <i> Development </i> <font size = '10' color = 'red'>Crash Course</font")
		
		document.drawContents(painter, rect2)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec_())