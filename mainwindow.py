import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtGui import QPainter
from ui_mainwindow import Ui_MainWindow


class NewFormWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnDashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageDashboard))
        self.ui.btnNotifications.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageNotifications))
        self.ui.btnNetwork.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageNetwork))
        self.ui.btnControls.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageControls))
        self.ui.btnRules.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageRules))
        self.ui.btnReports.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageReports))
        self.ui.btnSettings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageSettings))



        def add_static_graph(self):
            from PySide6.QtWidgets import QVBoxLayout

            # Create a simple data series
            series = QLineSeries()
            series.append(0, 6)
            series.append(2, 4)
            series.append(3, 8)
            series.append(7, 4)
            series.append(10, 5)

            # Create the chart
            chart = QChart()
            chart.addSeries(series)
            chart.setTitle("Network Activity Chart")
            chart.createDefaultAxes()
            chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

            # Create a chart view
            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
            chart_view.setMinimumSize(400, 250)

            # Check if the graph widget has a layout, if not, create one
            layout = self.ui.graphWidget.layout()
            if layout is None:
                layout = QVBoxLayout(self.ui.graphWidget)
                self.ui.graphWidget.setLayout(layout)

            layout.addWidget(chart_view)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewFormWindow()
    window.show()
    sys.exit(app.exec())
