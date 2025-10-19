import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout
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

        self.ui.btnExportCSV = QPushButton("Export CSV")
        self.ui.btnExportPDF = QPushButton("Export PDF")

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

        def export_csv(self):
                import csv
                from PySide6.QtWidgets import QFileDialog

                # Ask the user where to save the CSV
                path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
                if not path:
                        return

                # EXAMPLE DATA: get notif content
                notifications = [
                        {"Date": "2025-10-19", "Message": "Network stable"},
                        {"Date": "2025-10-19", "Message": "New rule added"},
                ]

                # Write CSV
                with open(path, "w", newline="", encoding="utf-8") as csvfile:
                        fieldnames = notifications[0].keys()
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(notifications)

                print(f"CSV exported to: {path}")


        # ReportLab (pip install reportlab)
        def export_pdf(self):
                from reportlab.lib.pagesizes import letter
                from reportlab.pdfgen import canvas

                path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
                if not path:
                        return

                notifications = [
                        {"Date": "2025-10-19", "Message": "Network stable"},
                        {"Date": "2025-10-19", "Message": "New rule added"},
                    ]


                    # ''' path = "report.pdf" -->
                    #c = canvas.Canvas(path, pagesize=letter)
                    #c.drawString(100, 750, "Hello PDF")
                    #c.save()
                    #c.setFont("Helvetica", 12)
                    #y = height - 50

                    #c.drawString(50, y, "Notifications Report")
                    #y -= 3'0

                    #for notif in notifications:
                     #   line = f"{notif['Date']} - {notif['Message']}"
                      #  c.drawString(50, y, line)
                       # y -= 20

                    #c.save()
                    # print(f"PDF exported to: {path}") '''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewFormWindow()
    window.show()
    sys.exit(app.exec())
