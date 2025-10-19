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
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

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
"         \n"
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

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
"         background-color: #3d59a1;\n"
"         color: white;\n"
"         border: none;\n"
"         border-radius: 6px;\n"
"         padding: 6px 12px;\n"
"        }\n"
"        QPushButton:hover {\n"
"         background-color: #7aa2f7;\n"
"        }\n"
"       ")
        self.mainContentLayout = QVBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setObjectName(u"mainContentLayout")
        self.stackedWidget = QStackedWidget(self.mainContentFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.dashboardLayout = QVBoxLayout(self.pageDashboard)
        self.dashboardLayout.setObjectName(u"dashboardLayout")
        self.headerFrame = QFrame(self.pageDashboard)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setStyleSheet(u"\n"
"               QFrame {\n"
"                background-color: #1f2335;\n"
"                border-bottom: 1px solid #3b4261;\n"
"               }\n"
"               QLabel {\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"                color: #7aa2f7;\n"
"               }\n"
"              ")
        self.headerLayout = QHBoxLayout(self.headerFrame)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerTitle = QLabel(self.headerFrame)
        self.headerTitle.setObjectName(u"headerTitle")

        self.headerLayout.addWidget(self.headerTitle)

        self.headerSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.refreshButton = QPushButton(self.headerFrame)
        self.refreshButton.setObjectName(u"refreshButton")

        self.headerLayout.addWidget(self.refreshButton)


        self.dashboardLayout.addWidget(self.headerFrame)

        self.statsFrame = QFrame(self.pageDashboard)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsFrame.setStyleSheet(u"\n"
"               QFrame {\n"
"                background: transparent;\n"
"               }\n"
"               QLabel {\n"
"                color: #c0caf5;\n"
"                font-size: 13px;\n"
"               }\n"
"              ")
        self.statsLayout = QHBoxLayout(self.statsFrame)
        self.statsLayout.setObjectName(u"statsLayout")
        self.cardNetwork = QFrame(self.statsFrame)
        self.cardNetwork.setObjectName(u"cardNetwork")
        self.cardNetwork.setStyleSheet(u"\n"
"                  QFrame {\n"
"                   background-color: rgba(255,255,255,0.05);\n"
"                   border-radius: 10px;\n"
"                   padding: 20px;\n"
"                   border: 1px solid #3b4261;\n"
"                  }\n"
"                  QLabel { color: #c0caf5; font-size: 13px; }\n"
"                 ")
        self.networkCardLayout = QVBoxLayout(self.cardNetwork)
        self.networkCardLayout.setObjectName(u"networkCardLayout")
        self.labelNetworkTitle = QLabel(self.cardNetwork)
        self.labelNetworkTitle.setObjectName(u"labelNetworkTitle")

        self.networkCardLayout.addWidget(self.labelNetworkTitle)

        self.labelNetworkValue = QLabel(self.cardNetwork)
        self.labelNetworkValue.setObjectName(u"labelNetworkValue")

        self.networkCardLayout.addWidget(self.labelNetworkValue)


        self.statsLayout.addWidget(self.cardNetwork)

        self.cardTraffic = QFrame(self.statsFrame)
        self.cardTraffic.setObjectName(u"cardTraffic")
        self.cardTraffic.setStyleSheet(u"\n"
"                  QFrame {\n"
"                   background-color: rgba(255,255,255,0.05);\n"
"                   border-radius: 10px;\n"
"                   padding: 20px;\n"
"                   border: 1px solid #3b4261;\n"
"                  }\n"
"                 ")
        self.trafficCardLayout = QVBoxLayout(self.cardTraffic)
        self.trafficCardLayout.setObjectName(u"trafficCardLayout")
        self.labelTrafficTitle = QLabel(self.cardTraffic)
        self.labelTrafficTitle.setObjectName(u"labelTrafficTitle")

        self.trafficCardLayout.addWidget(self.labelTrafficTitle)

        self.labelTrafficValue = QLabel(self.cardTraffic)
        self.labelTrafficValue.setObjectName(u"labelTrafficValue")

        self.trafficCardLayout.addWidget(self.labelTrafficValue)


        self.statsLayout.addWidget(self.cardTraffic)

        self.cardHealth = QFrame(self.statsFrame)
        self.cardHealth.setObjectName(u"cardHealth")
        self.cardHealth.setStyleSheet(u"\n"
"                  QFrame {\n"
"                   background-color: rgba(255,255,255,0.05);\n"
"                   border-radius: 10px;\n"
"                   padding: 20px;\n"
"                   border: 1px solid #3b4261;\n"
"                  }\n"
"                 ")
        self.healthCardLayout = QVBoxLayout(self.cardHealth)
        self.healthCardLayout.setObjectName(u"healthCardLayout")
        self.labelHealthTitle = QLabel(self.cardHealth)
        self.labelHealthTitle.setObjectName(u"labelHealthTitle")

        self.healthCardLayout.addWidget(self.labelHealthTitle)

        self.labelHealthValue = QLabel(self.cardHealth)
        self.labelHealthValue.setObjectName(u"labelHealthValue")

        self.healthCardLayout.addWidget(self.labelHealthValue)


        self.statsLayout.addWidget(self.cardHealth)


        self.dashboardLayout.addWidget(self.statsFrame)

        self.chartFrame = QFrame(self.pageDashboard)
        self.chartFrame.setObjectName(u"chartFrame")
        self.chartFrame.setStyleSheet(u"\n"
"               QFrame {\n"
"                background-color: #1f2335;\n"
"                border-radius: 10px;\n"
"                padding: 20px;\n"
"                border: 1px solid #3b4261;\n"
"               }\n"
"               QLabel { color: #9aa5ce; }\n"
"              ")
        self.chartLayout = QVBoxLayout(self.chartFrame)
        self.chartLayout.setObjectName(u"chartLayout")
        self.chartTitle = QLabel(self.chartFrame)
        self.chartTitle.setObjectName(u"chartTitle")

        self.chartLayout.addWidget(self.chartTitle)

        self.graphWidget = QWidget(self.chartFrame)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(400, 250))

        self.chartLayout.addWidget(self.graphWidget)


        self.dashboardLayout.addWidget(self.chartFrame)

        self.stackedWidget.addWidget(self.pageDashboard)
        self.pageNotifications = QWidget()
        self.pageNotifications.setObjectName(u"pageNotifications")
        self.notifLayout = QVBoxLayout(self.pageNotifications)
        self.notifLayout.setObjectName(u"notifLayout")
        self.labelNotif = QLabel(self.pageNotifications)
        self.labelNotif.setObjectName(u"labelNotif")

        self.notifLayout.addWidget(self.labelNotif)

        self.stackedWidget.addWidget(self.pageNotifications)
        self.pageNetwork = QWidget()
        self.pageNetwork.setObjectName(u"pageNetwork")
        self.networkLayout = QVBoxLayout(self.pageNetwork)
        self.networkLayout.setObjectName(u"networkLayout")
        self.labelNetwork = QLabel(self.pageNetwork)
        self.labelNetwork.setObjectName(u"labelNetwork")

        self.networkLayout.addWidget(self.labelNetwork)

        self.stackedWidget.addWidget(self.pageNetwork)
        self.pageControls = QWidget()
        self.pageControls.setObjectName(u"pageControls")
        self.controlsLayout = QVBoxLayout(self.pageControls)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.labelControls = QLabel(self.pageControls)
        self.labelControls.setObjectName(u"labelControls")

        self.controlsLayout.addWidget(self.labelControls)

        self.stackedWidget.addWidget(self.pageControls)
        self.pageRules = QWidget()
        self.pageRules.setObjectName(u"pageRules")
        self.rulesLayout = QVBoxLayout(self.pageRules)
        self.rulesLayout.setObjectName(u"rulesLayout")
        self.labelRules = QLabel(self.pageRules)
        self.labelRules.setObjectName(u"labelRules")

        self.rulesLayout.addWidget(self.labelRules)

        self.stackedWidget.addWidget(self.pageRules)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.reportsLayout = QVBoxLayout(self.pageReports)
        self.reportsLayout.setObjectName(u"reportsLayout")
        self.labelReports = QLabel(self.pageReports)
        self.labelReports.setObjectName(u"labelReports")

        self.reportsLayout.addWidget(self.labelReports)

        self.stackedWidget.addWidget(self.pageReports)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.settingsLayout = QVBoxLayout(self.pageSettings)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.labelSettings = QLabel(self.pageSettings)
        self.labelSettings.setObjectName(u"labelSettings")

        self.settingsLayout.addWidget(self.labelSettings)

        self.stackedWidget.addWidget(self.pageSettings)

        self.mainContentLayout.addWidget(self.stackedWidget)


        self.mainLayout.addWidget(self.mainContentFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Veil IPS/IDS Dashboard", None))
        self.menuTitle.setText(QCoreApplication.translate("MainWindow", u"VEIL Dashboard", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnNotifications.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.btnNetwork.setText(QCoreApplication.translate("MainWindow", u"Network Traffic", None))
        self.btnControls.setText(QCoreApplication.translate("MainWindow", u"Prevention & Response", None))
        self.btnRules.setText(QCoreApplication.translate("MainWindow", u"Rules Management", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Report Analytics", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.headerTitle.setText(QCoreApplication.translate("MainWindow", u"Dashboard Overview", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.labelNetworkTitle.setText(QCoreApplication.translate("MainWindow", u"Network Status", None))
        self.labelNetworkValue.setText(QCoreApplication.translate("MainWindow", u"Stable", None))
        self.labelTrafficTitle.setText(QCoreApplication.translate("MainWindow", u"Traffic Load", None))
        self.labelTrafficValue.setText(QCoreApplication.translate("MainWindow", u"245 Mbps", None))
        self.labelHealthTitle.setText(QCoreApplication.translate("MainWindow", u"System Health", None))
        self.labelHealthValue.setText(QCoreApplication.translate("MainWindow", u"Good", None))
        self.chartTitle.setText(QCoreApplication.translate("MainWindow", u"Network Activity (Last 24 Hours)", None))
        self.labelNotif.setText(QCoreApplication.translate("MainWindow", u"Notifications content goes here.", None))
        self.labelNetwork.setText(QCoreApplication.translate("MainWindow", u"Network Traffic Analysis content here.", None))
        self.labelControls.setText(QCoreApplication.translate("MainWindow", u"Prevention & Response content here.", None))
        self.labelRules.setText(QCoreApplication.translate("MainWindow", u"Rules Management content here.", None))
        self.labelReports.setText(QCoreApplication.translate("MainWindow", u"Report Analytics content here.", None))
        self.labelSettings.setText(QCoreApplication.translate("MainWindow", u"Settings content here.", None))
    # retranslateUi

