# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_demo_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(670, 401)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 7)

        self.RadiusCheck = QCheckBox(self.centralwidget)
        self.RadiusCheck.setObjectName(u"RadiusCheck")

        self.gridLayout.addWidget(self.RadiusCheck, 1, 0, 1, 1)

        self.SizeCheck = QCheckBox(self.centralwidget)
        self.SizeCheck.setObjectName(u"SizeCheck")

        self.gridLayout.addWidget(self.SizeCheck, 1, 1, 1, 2)

        self.PositionCheck = QCheckBox(self.centralwidget)
        self.PositionCheck.setObjectName(u"PositionCheck")

        self.gridLayout.addWidget(self.PositionCheck, 1, 3, 1, 2)

        self.RayleighCheck = QCheckBox(self.centralwidget)
        self.RayleighCheck.setObjectName(u"RayleighCheck")

        self.gridLayout.addWidget(self.RayleighCheck, 1, 5, 1, 2)

        self.RadiusSpin = QDoubleSpinBox(self.centralwidget)
        self.RadiusSpin.setObjectName(u"RadiusSpin")
        self.RadiusSpin.setDecimals(3)
        self.RadiusSpin.setMinimum(-1000000000.000000000000000)
        self.RadiusSpin.setMaximum(1000000000.000000000000000)
        self.RadiusSpin.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.RadiusSpin, 2, 0, 1, 1)

        self.SizeSpin = QDoubleSpinBox(self.centralwidget)
        self.SizeSpin.setObjectName(u"SizeSpin")
        self.SizeSpin.setDecimals(3)
        self.SizeSpin.setMinimum(-1000000000.000000000000000)
        self.SizeSpin.setMaximum(1000000000.000000000000000)
        self.SizeSpin.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.SizeSpin, 2, 2, 1, 1)

        self.PositionSpin = QDoubleSpinBox(self.centralwidget)
        self.PositionSpin.setObjectName(u"PositionSpin")
        self.PositionSpin.setDecimals(3)
        self.PositionSpin.setMinimum(-1000000000.000000000000000)
        self.PositionSpin.setMaximum(1000000000.000000000000000)
        self.PositionSpin.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.PositionSpin, 2, 4, 1, 1)

        self.RayleighSpin = QDoubleSpinBox(self.centralwidget)
        self.RayleighSpin.setObjectName(u"RayleighSpin")
        self.RayleighSpin.setDecimals(3)
        self.RayleighSpin.setMinimum(-1000000000.000000000000000)
        self.RayleighSpin.setMaximum(1000000000.000000000000000)

        self.gridLayout.addWidget(self.RayleighSpin, 2, 6, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 7)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 3)

        self.WavelengthSpin = QDoubleSpinBox(self.centralwidget)
        self.WavelengthSpin.setObjectName(u"WavelengthSpin")
        self.WavelengthSpin.setMaximum(100000.000000000000000)

        self.gridLayout.addWidget(self.WavelengthSpin, 5, 0, 1, 3)

        self.DistanceSpin = QDoubleSpinBox(self.centralwidget)
        self.DistanceSpin.setObjectName(u"DistanceSpin")
        self.DistanceSpin.setDecimals(3)
        self.DistanceSpin.setMinimum(-1000000000.000000000000000)
        self.DistanceSpin.setMaximum(1000000000.000000000000000)

        self.gridLayout.addWidget(self.DistanceSpin, 5, 4, 1, 3)

        self.CalculateButton = QPushButton(self.centralwidget)
        self.CalculateButton.setObjectName(u"CalculateButton")

        self.gridLayout.addWidget(self.CalculateButton, 6, 0, 1, 7)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 7)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 8, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 8, 2, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 8, 4, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 8, 6, 1, 1)

        self.RadiusLabel = QLabel(self.centralwidget)
        self.RadiusLabel.setObjectName(u"RadiusLabel")
        self.RadiusLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.RadiusLabel, 9, 0, 1, 1)

        self.SizeLabel = QLabel(self.centralwidget)
        self.SizeLabel.setObjectName(u"SizeLabel")
        self.SizeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.SizeLabel, 9, 2, 1, 1)

        self.PositionLabel = QLabel(self.centralwidget)
        self.PositionLabel.setObjectName(u"PositionLabel")
        self.PositionLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.PositionLabel, 9, 4, 1, 1)

        self.RayleighLabel = QLabel(self.centralwidget)
        self.RayleighLabel.setObjectName(u"RayleighLabel")
        self.RayleighLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.RayleighLabel, 9, 6, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 10, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 10, 3, 1, 2)

        self.WaistLabel = QLabel(self.centralwidget)
        self.WaistLabel.setObjectName(u"WaistLabel")
        self.WaistLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.WaistLabel, 11, 2, 1, 1)

        self.DivergenceLabel = QLabel(self.centralwidget)
        self.DivergenceLabel.setObjectName(u"DivergenceLabel")
        self.DivergenceLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.DivergenceLabel, 11, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 670, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.RadiusCheck, self.SizeCheck)
        QWidget.setTabOrder(self.SizeCheck, self.PositionCheck)
        QWidget.setTabOrder(self.PositionCheck, self.RayleighCheck)
        QWidget.setTabOrder(self.RayleighCheck, self.RadiusSpin)
        QWidget.setTabOrder(self.RadiusSpin, self.SizeSpin)
        QWidget.setTabOrder(self.SizeSpin, self.PositionSpin)
        QWidget.setTabOrder(self.PositionSpin, self.RayleighSpin)
        QWidget.setTabOrder(self.RayleighSpin, self.WavelengthSpin)
        QWidget.setTabOrder(self.WavelengthSpin, self.DistanceSpin)
        QWidget.setTabOrder(self.DistanceSpin, self.CalculateButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Select any two parameters. Unspecified parameters are in mm.", None))
        self.RadiusCheck.setText(QCoreApplication.translate("MainWindow", u"Radius R", None))
        self.SizeCheck.setText(QCoreApplication.translate("MainWindow", u"Size w", None))
        self.PositionCheck.setText(QCoreApplication.translate("MainWindow", u"Position z", None))
        self.RayleighCheck.setText(QCoreApplication.translate("MainWindow", u"Rayleigh range zR", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Wavelength (nm)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Propagation distance (mm)", None))
        self.CalculateButton.setText(QCoreApplication.translate("MainWindow", u"Calculate propagation", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Radius R", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Size w", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Position z", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Rayleigh range zR", None))
        self.RadiusLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.SizeLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.PositionLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.RayleighLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Waist w0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Divergence \u03b8 (mrad)", None))
        self.WaistLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.DivergenceLabel.setText(QCoreApplication.translate("MainWindow", u"___", None))
    # retranslateUi

