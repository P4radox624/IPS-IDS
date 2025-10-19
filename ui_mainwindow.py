# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QHBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.sidebarFrame = QFrame(self.centralwidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setStyleSheet(u"\n"
"        QFrame {\n"
"         background-color: #1a1b26;\n"
"         color: #c0caf5;\n"
"        }\n"
"        QPushButton {\n"
"         background-color: transparent;\n"
"         color: #c0caf5;\n"
"         text-align: left;\n"
"         padding: 8px 20px;\n"
"         border: none;\n"
"         font-size: 14px;\n"
"         border-radius: 6px;\n"
"        }\n"
"        QPushButton:hover {\n"
"         background-color: #292e42;\n"
"        }\n"
"        QLabel {\n"
"         color: #7aa2f7;\n"
"         padding: 12px;\n"
"         font-weight: bold;\n"
"         font-size: 15px;\n"
"        }\n"
"       ")
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.menuTitle = QLabel(self.sidebarFrame)
        self.menuTitle.setObjectName(u"menuTitle")

        self.sidebarLayout.addWidget(self.menuTitle)

        self.btnDashboard = QPushButton(self.sidebarFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")

        self.sidebarLayout.addWidget(self.btnDashboard)

        self.btnNotifications = QPushButton(self.sidebarFrame)
        self.btnNotifications.setObjectName(u"btnNotifications")

        self.sidebarLayout.addWidget(self.btnNotifications)

        self.btnNetwork = QPushButton(self.sidebarFrame)
        self.btnNetwork.setObjectName(u"btnNetwork")

        self.sidebarLayout.addWidget(self.btnNetwork)

        self.btnControls = QPushButton(self.sidebarFrame)
        self.btnControls.setObjectName(u"btnControls")

        self.sidebarLayout.addWidget(self.btnControls)

        self.btnRules = QPushButton(self.sidebarFrame)
        self.btnRules.setObjectName(u"btnRules")

        self.sidebarLayout.addWidget(self.btnRules)

        self.btnReports = QPushButton(self.sidebarFrame)
        self.btnReports.setObjectName(u"btnReports")

        self.sidebarLayout.addWidget(self.btnReports)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.verticalSpacer)

        self.btnSettings = QPushButton(self.sidebarFrame)
        self.btnSettings.setObjectName(u"btnSettings")

        self.sidebarLayout.addWidget(self.btnSettings)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.mainContentFrame = QFrame(self.centralwidget)
        self.mainContentFrame.setObjectName(u"mainContentFrame")
        self.mainContentFrame.setStyleSheet(u"\n"
"        QFrame {\n"
"         background-color: #24283b;\n"
"         color: #c0caf5;\n"
"        }\n"
"        QLabel {\n"
"         color: #c0caf5;\n"
"         font-size: 14px;\n"
"        }\n"
"        QPushButton {\n"
"         background-color: #7aa2f7;\n"
"         color: white;\n"
"         border: none;\n"
"         border-radius: 6px;\n"
"         padding: 6px 12px;\n"
"        }\n"
"        QPushButton:hover {\n"
"         background-color: #89b4fa;\n"
"        }\n"
"        QHeaderView::section {\n"
"         background-color: #414868;\n"
"         color: #c0caf5;\n"
"         font-weight: bold;\n"
"         padding: 6px;\n"
"         border: none;\n"
"        }\n"
"        QTableWidget {\n"
"         background-color: #1f2335;\n"
"         gridline-color: #3b4261;\n"
"         border: 1px solid #3b4261;\n"
"        }\n"
"       ")
        self.mainContentLayout = QVBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setObjectName(u"mainContentLayout")
        self.headerFrame = QFrame(self.mainContentFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"\n"
"           QFrame {\n"
"            background-color: #1f2335;\n"
"            border-bottom: 1px solid #3b4261;\n"
"           }\n"
"           QLabel {\n"
"            font-size: 16px;\n"
"            font-weight: bold;\n"
"            color: #7aa2f7;\n"
"           }\n"
"          ")
        self.headerLayout = QHBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerTitle = QLabel(self.headerFrame)
        self.headerTitle.setObjectName(u"headerTitle")

        self.headerLayout.addWidget(self.headerTitle)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.refreshButton = QPushButton(self.headerFrame)
        self.refreshButton.setObjectName(u"refreshButton")

        self.headerLayout.addWidget(self.refreshButton)


        self.mainContentLayout.addWidget(self.headerFrame)

        self.statsLayout = QHBoxLayout()
        self.statsLayout.setObjectName(u"statsLayout")
        self.stat1 = QFrame(self.mainContentFrame)
        self.stat1.setObjectName(u"stat1")
        self.stat1.setStyleSheet(u"QFrame { background-color: #1f2335; border-radius: 8px; padding: 12px; }")
        self.vboxLayout = QVBoxLayout(self.stat1)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.lblNetworkStatus = QLabel(self.stat1)
        self.lblNetworkStatus.setObjectName(u"lblNetworkStatus")

        self.vboxLayout.addWidget(self.lblNetworkStatus)


        self.statsLayout.addWidget(self.stat1)

        self.stat2 = QFrame(self.mainContentFrame)
        self.stat2.setObjectName(u"stat2")
        self.stat2.setStyleSheet(u"QFrame { background-color: #1f2335; border-radius: 8px; padding: 12px; }")
        self.vboxLayout1 = QVBoxLayout(self.stat2)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lblTraffic = QLabel(self.stat2)
        self.lblTraffic.setObjectName(u"lblTraffic")

        self.vboxLayout1.addWidget(self.lblTraffic)


        self.statsLayout.addWidget(self.stat2)

        self.stat3 = QFrame(self.mainContentFrame)
        self.stat3.setObjectName(u"stat3")
        self.stat3.setStyleSheet(u"QFrame { background-color: #1f2335; border-radius: 8px; padding: 12px; }")
        self.vboxLayout2 = QVBoxLayout(self.stat3)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.lblSystemHealth = QLabel(self.stat3)
        self.lblSystemHealth.setObjectName(u"lblSystemHealth")

        self.vboxLayout2.addWidget(self.lblSystemHealth)


        self.statsLayout.addWidget(self.stat3)


        self.mainContentLayout.addLayout(self.statsLayout)

        self.graphWidget = QWidget(self.mainContentFrame)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(400, 250))
        self.graphWidget.setStyleSheet(u"\n"
"           QWidget {\n"
"            background-color: #1f2335;\n"
"            border-radius: 8px;\n"
"            border: 1px solid #3b4261;\n"
"           }\n"
"          ")
        self.graphLayout = QVBoxLayout(self.graphWidget)
        self.graphLayout.setObjectName(u"graphLayout")
        self.graphLayout.setContentsMargins(0, 0, 0, 0)

        self.mainContentLayout.addWidget(self.graphWidget)

        self.widget = QWidget(self.mainContentFrame)
        self.widget.setObjectName(u"widget")

        self.mainContentLayout.addWidget(self.widget)

        self.statusLabel = QLabel(self.mainContentFrame)
        self.statusLabel.setObjectName(u"statusLabel")

        self.mainContentLayout.addWidget(self.statusLabel)


        self.mainLayout.addWidget(self.mainContentFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zeek IPS/IDS Dashboard", None))
        self.menuTitle.setText(QCoreApplication.translate("MainWindow", u" VEIL Dashboard", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.btnNotifications.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.btnNetwork.setText(QCoreApplication.translate("MainWindow", u"Network Traffic", None))
        self.btnControls.setText(QCoreApplication.translate("MainWindow", u" Prevention & Response", None))
        self.btnRules.setText(QCoreApplication.translate("MainWindow", u"Rules Management", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Report Analytics", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"\u2699 Settings", None))
        self.headerTitle.setText(QCoreApplication.translate("MainWindow", u"Network Overview", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u27f3 Refresh", None))
        self.lblNetworkStatus.setText(QCoreApplication.translate("MainWindow", u"Network Status: Stable", None))
        self.lblTraffic.setText(QCoreApplication.translate("MainWindow", u" Real-Time Traffic: Active", None))
        self.lblSystemHealth.setText(QCoreApplication.translate("MainWindow", u"System Health: Good", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status: Ready", None))
    # retranslateUi

