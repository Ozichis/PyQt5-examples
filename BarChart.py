from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries,QBarCatergoryAxis
from PyQt5.QtQui import QPainter
from PyQt5.QtCore import Qt

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle("My Store")
		self.setGeometry(100, 100, 680, 500)
		self.create_bar()
		self.show()
		
	def create_bar(self):
		set0 = QBarSet("Apple")
		set1 = QBarSet("Banana")
		set2 = QBarSet("Orange")
		set3 = QBarSet("Pineapple")
		set4 = QBarSet("Mango")
		
		set0 << 1 << 2 << 3 << 4 << 5 << 6
		set1 << 5 << 0 << 0 << 4 << 0 << 7
		set2 << 3 << 5 << 8 << 13 << 8 << 5
		set3 << 5 << 6 << 7 << 3 << 4 << 5
		set4 << 9 << 7 << 5 << 3 << 1 << 2
		
		series = QPercentBarSeries()
		series.append(set0)
		series.append(set1)
		series.append(set2)
		series.append(set3)
		series.append(set4)
		
		chart = QChart()
		chart.addSeries(series)
		chart.setTitle("Fruits Percentage")
		chart.setAnimationOptions(QChart.SeriesAnimations)
		
		categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
		
		axis = QBarCatergoryAxis()
		axis.append(categories)
		
		chart.createDefaultAxes()
		chart.setAxisX(axis, series)
		
		chartview = QChartView(chart)
		chartview.setRenderHint(QPainter.Antialiasing)
		
		self.setCentralWidget(chartview)
		
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())