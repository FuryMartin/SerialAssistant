# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowcyhBAr.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 457)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.FMODE = QGroupBox(self.widget_2)
        self.FMODE.setObjectName(u"FMODE")
        self.horizontalLayout_8 = QHBoxLayout(self.FMODE)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.FMODE)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10, 0, Qt.AlignRight)

        self.FSK_mode = QRadioButton(self.FMODE)
        self.FSK_mode.setObjectName(u"FSK_mode")

        self.horizontalLayout_8.addWidget(self.FSK_mode, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.FMODE)

        self.FRF = QGroupBox(self.widget_2)
        self.FRF.setObjectName(u"FRF")
        self.horizontalLayout_9 = QHBoxLayout(self.FRF)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.FRF)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.FSK_frequency = QComboBox(self.FRF)
        self.FSK_frequency.addItem("")
        self.FSK_frequency.addItem("")
        self.FSK_frequency.addItem("")
        self.FSK_frequency.setObjectName(u"FSK_frequency")

        self.horizontalLayout_9.addWidget(self.FSK_frequency)


        self.verticalLayout_2.addWidget(self.FRF)

        self.FPW = QGroupBox(self.widget_2)
        self.FPW.setObjectName(u"FPW")
        self.horizontalLayout_12 = QHBoxLayout(self.FPW)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.FPW)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.FSK_power = QComboBox(self.FPW)
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.addItem("")
        self.FSK_power.setObjectName(u"FSK_power")

        self.horizontalLayout_12.addWidget(self.FSK_power)


        self.verticalLayout_2.addWidget(self.FPW)

        self.FBR = QGroupBox(self.widget_2)
        self.FBR.setObjectName(u"FBR")
        self.horizontalLayout_13 = QHBoxLayout(self.FBR)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.FBR)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.FSK_bitrate = QComboBox(self.FBR)
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.addItem("")
        self.FSK_bitrate.setObjectName(u"FSK_bitrate")

        self.horizontalLayout_13.addWidget(self.FSK_bitrate)


        self.verticalLayout_2.addWidget(self.FBR)

        self.FRxBW = QGroupBox(self.widget_2)
        self.FRxBW.setObjectName(u"FRxBW")
        self.horizontalLayout_15 = QHBoxLayout(self.FRxBW)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.FRxBW)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.FSK_bandwidth = QComboBox(self.FRxBW)
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.addItem("")
        self.FSK_bandwidth.setObjectName(u"FSK_bandwidth")

        self.horizontalLayout_15.addWidget(self.FSK_bandwidth)


        self.verticalLayout_2.addWidget(self.FRxBW)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout_6.addWidget(self.widget_2)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LMODE = QGroupBox(self.widget)
        self.LMODE.setObjectName(u"LMODE")
        self.horizontalLayout_7 = QHBoxLayout(self.LMODE)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.LMODE)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7, 0, Qt.AlignRight)

        self.Lora_mode = QRadioButton(self.LMODE)
        self.Lora_mode.setObjectName(u"Lora_mode")

        self.horizontalLayout_7.addWidget(self.Lora_mode, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.LMODE)

        self.LRF = QGroupBox(self.widget)
        self.LRF.setObjectName(u"LRF")
        self.horizontalLayout_3 = QHBoxLayout(self.LRF)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.LRF)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.Lora_frequency = QComboBox(self.LRF)
        self.Lora_frequency.addItem("")
        self.Lora_frequency.addItem("")
        self.Lora_frequency.addItem("")
        self.Lora_frequency.setObjectName(u"Lora_frequency")

        self.horizontalLayout_3.addWidget(self.Lora_frequency)


        self.verticalLayout.addWidget(self.LRF)

        self.LPW = QGroupBox(self.widget)
        self.LPW.setObjectName(u"LPW")
        self.horizontalLayout_5 = QHBoxLayout(self.LPW)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.LPW)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.Lora_power = QComboBox(self.LPW)
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.addItem("")
        self.Lora_power.setObjectName(u"Lora_power")

        self.horizontalLayout_5.addWidget(self.Lora_power)


        self.verticalLayout.addWidget(self.LPW)

        self.LBW = QGroupBox(self.widget)
        self.LBW.setObjectName(u"LBW")
        self.LBW.setStyleSheet(u"")
        self.LBW.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.LBW)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.LBW)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.Lora_bandwidth = QComboBox(self.LBW)
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.addItem("")
        self.Lora_bandwidth.setObjectName(u"Lora_bandwidth")

        self.horizontalLayout_2.addWidget(self.Lora_bandwidth)


        self.verticalLayout.addWidget(self.LBW)

        self.LSF = QGroupBox(self.widget)
        self.LSF.setObjectName(u"LSF")
        self.horizontalLayout_4 = QHBoxLayout(self.LSF)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.LSF)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.Lora_spreadingfactor = QComboBox(self.LSF)
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.addItem("")
        self.Lora_spreadingfactor.setObjectName(u"Lora_spreadingfactor")

        self.horizontalLayout_4.addWidget(self.Lora_spreadingfactor)


        self.verticalLayout.addWidget(self.LSF)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.LRF.raise_()
        self.LMODE.raise_()
        self.LPW.raise_()
        self.LBW.raise_()
        self.LSF.raise_()
        self.pushButton.raise_()

        self.horizontalLayout_6.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.IO_window = QTextEdit(self.centralwidget)
        self.IO_window.setObjectName(u"IO_window")
        self.IO_window.setFrameShape(QFrame.StyledPanel)
        self.IO_window.setFrameShadow(QFrame.Sunken)
        self.IO_window.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.IO_window.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.IO_window.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.IO_window)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 385, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.FMODE.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FSK\u6a21\u5f0f", None))
        self.FSK_mode.setText("")
        self.FRF.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5c04\u9891\u7387", None))
        self.FSK_frequency.setItemText(0, QCoreApplication.translate("MainWindow", u"169 MHz", None))
        self.FSK_frequency.setItemText(1, QCoreApplication.translate("MainWindow", u"433 MHz", None))
        self.FSK_frequency.setItemText(2, QCoreApplication.translate("MainWindow", u"868 MHz", None))

        self.FPW.setTitle("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5c04\u529f\u7387", None))
        self.FSK_power.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.FSK_power.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.FSK_power.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.FSK_power.setItemText(3, QCoreApplication.translate("MainWindow", u"2", None))
        self.FSK_power.setItemText(4, QCoreApplication.translate("MainWindow", u"3", None))
        self.FSK_power.setItemText(5, QCoreApplication.translate("MainWindow", u"4", None))
        self.FSK_power.setItemText(6, QCoreApplication.translate("MainWindow", u"5", None))
        self.FSK_power.setItemText(7, QCoreApplication.translate("MainWindow", u"6", None))
        self.FSK_power.setItemText(8, QCoreApplication.translate("MainWindow", u"7", None))
        self.FSK_power.setItemText(9, QCoreApplication.translate("MainWindow", u"8", None))
        self.FSK_power.setItemText(10, QCoreApplication.translate("MainWindow", u"9", None))
        self.FSK_power.setItemText(11, QCoreApplication.translate("MainWindow", u"10", None))
        self.FSK_power.setItemText(12, QCoreApplication.translate("MainWindow", u"11", None))
        self.FSK_power.setItemText(13, QCoreApplication.translate("MainWindow", u"12", None))
        self.FSK_power.setItemText(14, QCoreApplication.translate("MainWindow", u"13", None))
        self.FSK_power.setItemText(15, QCoreApplication.translate("MainWindow", u"14", None))
        self.FSK_power.setItemText(16, QCoreApplication.translate("MainWindow", u"15", None))
        self.FSK_power.setItemText(17, QCoreApplication.translate("MainWindow", u"16", None))
        self.FSK_power.setItemText(18, QCoreApplication.translate("MainWindow", u"17", None))
        self.FSK_power.setItemText(19, QCoreApplication.translate("MainWindow", u"18", None))
        self.FSK_power.setItemText(20, QCoreApplication.translate("MainWindow", u"19", None))

        self.FBR.setTitle("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u7279\u7387", None))
        self.FSK_bitrate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.FSK_bitrate.setItemText(1, QCoreApplication.translate("MainWindow", u"1200", None))
        self.FSK_bitrate.setItemText(2, QCoreApplication.translate("MainWindow", u"2400", None))
        self.FSK_bitrate.setItemText(3, QCoreApplication.translate("MainWindow", u"4800", None))
        self.FSK_bitrate.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.FSK_bitrate.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.FSK_bitrate.setItemText(6, QCoreApplication.translate("MainWindow", u"76800", None))
        self.FSK_bitrate.setItemText(7, QCoreApplication.translate("MainWindow", u"153600", None))

        self.FRxBW.setTitle("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u5e26\u5bbd", None))
        self.FSK_bandwidth.setItemText(0, QCoreApplication.translate("MainWindow", u"100.0 kHz", None))
        self.FSK_bandwidth.setItemText(1, QCoreApplication.translate("MainWindow", u"2.6 kHz", None))
        self.FSK_bandwidth.setItemText(2, QCoreApplication.translate("MainWindow", u"3.1 kHz", None))
        self.FSK_bandwidth.setItemText(3, QCoreApplication.translate("MainWindow", u"3.9 kHz", None))
        self.FSK_bandwidth.setItemText(4, QCoreApplication.translate("MainWindow", u"5.2 kHz", None))
        self.FSK_bandwidth.setItemText(5, QCoreApplication.translate("MainWindow", u"6.3 kHz", None))
        self.FSK_bandwidth.setItemText(6, QCoreApplication.translate("MainWindow", u"7.8 kHz", None))
        self.FSK_bandwidth.setItemText(7, QCoreApplication.translate("MainWindow", u"10.4 kHz", None))
        self.FSK_bandwidth.setItemText(8, QCoreApplication.translate("MainWindow", u"12.5 kHz", None))
        self.FSK_bandwidth.setItemText(9, QCoreApplication.translate("MainWindow", u"15.6 kHz", None))
        self.FSK_bandwidth.setItemText(10, QCoreApplication.translate("MainWindow", u"20.8 kHz", None))
        self.FSK_bandwidth.setItemText(11, QCoreApplication.translate("MainWindow", u"25.0 kHz", None))
        self.FSK_bandwidth.setItemText(12, QCoreApplication.translate("MainWindow", u"31.3 kHz", None))
        self.FSK_bandwidth.setItemText(13, QCoreApplication.translate("MainWindow", u"41.7 kHz", None))
        self.FSK_bandwidth.setItemText(14, QCoreApplication.translate("MainWindow", u"50.0 kHz", None))
        self.FSK_bandwidth.setItemText(15, QCoreApplication.translate("MainWindow", u"62.5 kHz", None))
        self.FSK_bandwidth.setItemText(16, QCoreApplication.translate("MainWindow", u"83.3 kHz", None))
        self.FSK_bandwidth.setItemText(17, QCoreApplication.translate("MainWindow", u"125.0 kHz", None))
        self.FSK_bandwidth.setItemText(18, QCoreApplication.translate("MainWindow", u"166.7 kHz", None))
        self.FSK_bandwidth.setItemText(19, QCoreApplication.translate("MainWindow", u"200.0 kHz", None))
        self.FSK_bandwidth.setItemText(20, QCoreApplication.translate("MainWindow", u"250.0 kHz", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.LMODE.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lora\u6a21\u5f0f", None))
        self.Lora_mode.setText("")
        self.LRF.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5c04\u9891\u7387", None))
        self.Lora_frequency.setItemText(0, QCoreApplication.translate("MainWindow", u"169 MHz", None))
        self.Lora_frequency.setItemText(1, QCoreApplication.translate("MainWindow", u"433 MHz", None))
        self.Lora_frequency.setItemText(2, QCoreApplication.translate("MainWindow", u"868 MHz", None))

        self.LPW.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5c04\u529f\u7387", None))
        self.Lora_power.setItemText(0, QCoreApplication.translate("MainWindow", u"20", None))
        self.Lora_power.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.Lora_power.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.Lora_power.setItemText(3, QCoreApplication.translate("MainWindow", u"2", None))
        self.Lora_power.setItemText(4, QCoreApplication.translate("MainWindow", u"3", None))
        self.Lora_power.setItemText(5, QCoreApplication.translate("MainWindow", u"4", None))
        self.Lora_power.setItemText(6, QCoreApplication.translate("MainWindow", u"5", None))
        self.Lora_power.setItemText(7, QCoreApplication.translate("MainWindow", u"6", None))
        self.Lora_power.setItemText(8, QCoreApplication.translate("MainWindow", u"7", None))
        self.Lora_power.setItemText(9, QCoreApplication.translate("MainWindow", u"8", None))
        self.Lora_power.setItemText(10, QCoreApplication.translate("MainWindow", u"9", None))
        self.Lora_power.setItemText(11, QCoreApplication.translate("MainWindow", u"10", None))
        self.Lora_power.setItemText(12, QCoreApplication.translate("MainWindow", u"11", None))
        self.Lora_power.setItemText(13, QCoreApplication.translate("MainWindow", u"12", None))
        self.Lora_power.setItemText(14, QCoreApplication.translate("MainWindow", u"13", None))
        self.Lora_power.setItemText(15, QCoreApplication.translate("MainWindow", u"14", None))
        self.Lora_power.setItemText(16, QCoreApplication.translate("MainWindow", u"15", None))
        self.Lora_power.setItemText(17, QCoreApplication.translate("MainWindow", u"16", None))
        self.Lora_power.setItemText(18, QCoreApplication.translate("MainWindow", u"17", None))
        self.Lora_power.setItemText(19, QCoreApplication.translate("MainWindow", u"18", None))
        self.Lora_power.setItemText(20, QCoreApplication.translate("MainWindow", u"19", None))

        self.LBW.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u5bbd", None))
        self.Lora_bandwidth.setItemText(0, QCoreApplication.translate("MainWindow", u"7.8 kHz", None))
        self.Lora_bandwidth.setItemText(1, QCoreApplication.translate("MainWindow", u"10.4 kHz", None))
        self.Lora_bandwidth.setItemText(2, QCoreApplication.translate("MainWindow", u"15.6 kHz", None))
        self.Lora_bandwidth.setItemText(3, QCoreApplication.translate("MainWindow", u"20.8 kHz", None))
        self.Lora_bandwidth.setItemText(4, QCoreApplication.translate("MainWindow", u"31.2 kHz", None))
        self.Lora_bandwidth.setItemText(5, QCoreApplication.translate("MainWindow", u"41.6 kHz", None))
        self.Lora_bandwidth.setItemText(6, QCoreApplication.translate("MainWindow", u"62.5 kHz", None))
        self.Lora_bandwidth.setItemText(7, QCoreApplication.translate("MainWindow", u"125 kHz", None))
        self.Lora_bandwidth.setItemText(8, QCoreApplication.translate("MainWindow", u"250 kHz", None))
        self.Lora_bandwidth.setItemText(9, QCoreApplication.translate("MainWindow", u"500 kHz", None))

        self.LSF.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6269\u9891\u56e0\u5b50", None))
        self.Lora_spreadingfactor.setItemText(0, QCoreApplication.translate("MainWindow", u"64", None))
        self.Lora_spreadingfactor.setItemText(1, QCoreApplication.translate("MainWindow", u"128", None))
        self.Lora_spreadingfactor.setItemText(2, QCoreApplication.translate("MainWindow", u"256", None))
        self.Lora_spreadingfactor.setItemText(3, QCoreApplication.translate("MainWindow", u"512", None))
        self.Lora_spreadingfactor.setItemText(4, QCoreApplication.translate("MainWindow", u"1024", None))
        self.Lora_spreadingfactor.setItemText(5, QCoreApplication.translate("MainWindow", u"2048", None))
        self.Lora_spreadingfactor.setItemText(6, QCoreApplication.translate("MainWindow", u"4096", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
    # retranslateUi

