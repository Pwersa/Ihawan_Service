##### Ihawan Service - CASHIER SYSTEM #####

from win32printing import Printer
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Reporting_System import Ui_report

class database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Admin123",
        )
        self.mycursor = self.mydb.cursor()

    def create(self):
        try:
            self.mycursor.execute("CREATE DATABASE ihawan")
            return "Database Succesfully Created"
        except mysql.connector.Error as err:
            print(err)

DB = database()
DB.create()

class Ui_cashier_window(object):

    def connection(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin123",
            database="ihawan",
        )
        self.mycursor = self.mydb.cursor()

    def setupUi(self, cashier_window):
        self.cashier = cashier_window
        cashier_window.setObjectName("cashier_window")
        cashier_window.setWindowModality(QtCore.Qt.WindowModal)
        cashier_window.resize(1154, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cashier_window.sizePolicy().hasHeightForWidth())
        cashier_window.setSizePolicy(sizePolicy)
        cashier_window.setMinimumSize(QtCore.QSize(0, 0))
        cashier_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 181, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 57, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 47, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 25, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 181, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 57, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 47, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 25, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 57, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 47, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 25, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 19, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 38, 15))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        cashier_window.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/Barbecue-grill-BBQ-food-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cashier_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(cashier_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(1031, 70))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(351, 461))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 800))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(494, 320))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.transaction_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction_label.sizePolicy().hasHeightForWidth())
        self.transaction_label.setSizePolicy(sizePolicy)
        self.transaction_label.setMinimumSize(QtCore.QSize(161, 21))
        self.transaction_label.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.transaction_label.setFont(font)
        self.transaction_label.setObjectName("transaction_label")
        self.gridLayout_2.addWidget(self.transaction_label, 2, 0, 1, 1)
        self.product_table2 = QtWidgets.QTableWidget(self.frame_2)
        self.product_table2.setToolTipDuration(-1)
        self.product_table2.setAutoFillBackground(False)
        self.product_table2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.product_table2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.product_table2.setObjectName("product_table2")
        self.product_table2.setColumnCount(4)
        self.product_table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.product_table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table2.setHorizontalHeaderItem(3, item)
        self.product_table2.horizontalHeader().setDefaultSectionSize(100)
        self.product_table2.horizontalHeader().setHighlightSections(True)
        self.product_table2.horizontalHeader().setMinimumSectionSize(39)
        self.product_table2.horizontalHeader().setSortIndicatorShown(False)
        self.product_table2.horizontalHeader().setStretchLastSection(False)
        self.product_table2.verticalHeader().setCascadingSectionResizes(False)
        self.product_table2.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.product_table2, 3, 0, 1, 3)
        self.products = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.products.sizePolicy().hasHeightForWidth())
        self.products.setSizePolicy(sizePolicy)
        self.products.setMinimumSize(QtCore.QSize(171, 22))
        self.products.setMaximumSize(QtCore.QSize(16777215, 22))
        self.products.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.products.setObjectName("products")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/676723.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.products.addItem(icon1, "")
        self.gridLayout_2.addWidget(self.products, 1, 0, 1, 1)
        self.quantity = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantity.sizePolicy().hasHeightForWidth())
        self.quantity.setSizePolicy(sizePolicy)
        self.quantity.setMinimumSize(QtCore.QSize(72, 23))
        self.quantity.setMaximumSize(QtCore.QSize(16777215, 23))
        self.quantity.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.quantity.setMinimum(0)
        self.quantity.setMaximum(5)
        self.quantity.setSingleStep(1)
        self.quantity.setProperty("value", 0)
        self.quantity.setDisplayIntegerBase(10)
        self.quantity.setObjectName("quantity")
        self.gridLayout_2.addWidget(self.quantity, 1, 1, 1, 1)
        self.enter_button = QtWidgets.QPushButton(self.frame_2)
        self.enter_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_button.sizePolicy().hasHeightForWidth())
        self.enter_button.setSizePolicy(sizePolicy)
        self.enter_button.setMinimumSize(QtCore.QSize(70, 24))
        self.enter_button.setMaximumSize(QtCore.QSize(16777215, 24))
        self.enter_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_button.setObjectName("enter_button")
        self.gridLayout_2.addWidget(self.enter_button, 1, 2, 1, 1)
        self.enterqty_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterqty_label.sizePolicy().hasHeightForWidth())
        self.enterqty_label.setSizePolicy(sizePolicy)
        self.enterqty_label.setMinimumSize(QtCore.QSize(81, 21))
        self.enterqty_label.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enterqty_label.setFont(font)
        self.enterqty_label.setObjectName("enterqty_label")
        self.gridLayout_2.addWidget(self.enterqty_label, 0, 1, 1, 1)
        self.enter_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_label.sizePolicy().hasHeightForWidth())
        self.enter_label.setSizePolicy(sizePolicy)
        self.enter_label.setMinimumSize(QtCore.QSize(141, 21))
        self.enter_label.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_label.setFont(font)
        self.enter_label.setObjectName("enter_label")
        self.gridLayout_2.addWidget(self.enter_label, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(351, 161))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 161))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.waiting_label_6 = QtWidgets.QLabel(self.frame_3)
        self.waiting_label_6.setGeometry(QtCore.QRect(190, 10, 266, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waiting_label_6.sizePolicy().hasHeightForWidth())
        self.waiting_label_6.setSizePolicy(sizePolicy)
        self.waiting_label_6.setMinimumSize(QtCore.QSize(251, 21))
        self.waiting_label_6.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.waiting_label_6.setFont(font)
        self.waiting_label_6.setObjectName("waiting_label_6")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 141, 99))
        self.label_3.setMinimumSize(QtCore.QSize(141, 99))
        self.label_3.setMaximumSize(QtCore.QSize(141, 99))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/LOGO.png"))
        self.label_3.setObjectName("label_3")
        self.time_label = QtWidgets.QLabel(self.frame_3)
        self.time_label.setGeometry(QtCore.QRect(335, 36, 100, 36))
        self.time_label.setMinimumSize(QtCore.QSize(100, 36))
        self.time_label.setMaximumSize(QtCore.QSize(100, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.waiting_label_7 = QtWidgets.QLabel(self.frame_3)
        self.waiting_label_7.setGeometry(QtCore.QRect(235, 48, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waiting_label_7.sizePolicy().hasHeightForWidth())
        self.waiting_label_7.setSizePolicy(sizePolicy)
        self.waiting_label_7.setMinimumSize(QtCore.QSize(71, 21))
        self.waiting_label_7.setMaximumSize(QtCore.QSize(94, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.waiting_label_7.setFont(font)
        self.waiting_label_7.setObjectName("waiting_label_7")
        self.total_label_3 = QtWidgets.QLabel(self.frame_3)
        self.total_label_3.setGeometry(QtCore.QRect(210, 70, 261, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_label_3.sizePolicy().hasHeightForWidth())
        self.total_label_3.setSizePolicy(sizePolicy)
        self.total_label_3.setMinimumSize(QtCore.QSize(261, 21))
        self.total_label_3.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_label_3.setFont(font)
        self.total_label_3.setObjectName("total_label_3")
        self.price_label = QtWidgets.QLabel(self.frame_3)
        self.price_label.setGeometry(QtCore.QRect(336, 95, 100, 36))
        self.price_label.setMinimumSize(QtCore.QSize(100, 36))
        self.price_label.setMaximumSize(QtCore.QSize(100, 36))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(24)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.php_label_3 = QtWidgets.QLabel(self.frame_3)
        self.php_label_3.setGeometry(QtCore.QRect(280, 110, 31, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.php_label_3.sizePolicy().hasHeightForWidth())
        self.php_label_3.setSizePolicy(sizePolicy)
        self.php_label_3.setMinimumSize(QtCore.QSize(31, 21))
        self.php_label_3.setMaximumSize(QtCore.QSize(31, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.php_label_3.setFont(font)
        self.php_label_3.setObjectName("php_label_3")
        self.gridLayout_2.addWidget(self.frame_3, 4, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.product_table1 = QtWidgets.QTableWidget(self.frame_4)
        self.product_table1.setMinimumSize(QtCore.QSize(0, 0))
        self.product_table1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.product_table1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.product_table1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.product_table1.setObjectName("product_table1")
        self.product_table1.setColumnCount(4)
        self.product_table1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.product_table1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.product_table1.setHorizontalHeaderItem(3, item)
        self.product_table1.horizontalHeader().setCascadingSectionResizes(False)
        self.product_table1.horizontalHeader().setDefaultSectionSize(100)
        self.product_table1.horizontalHeader().setStretchLastSection(False)
        self.product_table1.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.product_table1, 1, 0, 1, 1)
        self.product_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_label.sizePolicy().hasHeightForWidth())
        self.product_label.setSizePolicy(sizePolicy)
        self.product_label.setMinimumSize(QtCore.QSize(461, 31))
        self.product_label.setMaximumSize(QtCore.QSize(461, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.product_label.setFont(font)
        self.product_label.setObjectName("product_label")
        self.gridLayout_4.addWidget(self.product_label, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(579, 51))
        self.frame_5.setMaximumSize(QtCore.QSize(481, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(194, 31))
        self.pushButton_3.setMaximumSize(QtCore.QSize(194, 31))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 2, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)
        self.waiting_label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waiting_label_3.sizePolicy().hasHeightForWidth())
        self.waiting_label_3.setSizePolicy(sizePolicy)
        self.waiting_label_3.setMinimumSize(QtCore.QSize(251, 21))
        self.waiting_label_3.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.waiting_label_3.setFont(font)
        self.waiting_label_3.setObjectName("waiting_label_3")
        self.gridLayout.addWidget(self.waiting_label_3, 2, 0, 1, 1)
        self.payment = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.payment.setMinimumSize(QtCore.QSize(231, 41))
        self.payment.setMaximumSize(QtCore.QSize(231, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.payment.setFont(font)
        self.payment.setPrefix("")
        self.payment.setMaximum(9999.0)
        self.payment.setSingleStep(1.0)
        self.payment.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.payment.setObjectName("payment")
        self.gridLayout.addWidget(self.payment, 2, 2, 2, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(142, 41))
        self.pushButton_2.setMaximumSize(QtCore.QSize(142, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 2, 1)
        self.edit_inventory_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_inventory_2.sizePolicy().hasHeightForWidth())
        self.edit_inventory_2.setSizePolicy(sizePolicy)
        self.edit_inventory_2.setMinimumSize(QtCore.QSize(138, 23))
        self.edit_inventory_2.setMaximumSize(QtCore.QSize(138, 23))
        self.edit_inventory_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_inventory_2.setObjectName("edit_inventory_2")
        self.gridLayout.addWidget(self.edit_inventory_2, 3, 0, 1, 1)
        self.waiting_label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waiting_label_8.sizePolicy().hasHeightForWidth())
        self.waiting_label_8.setSizePolicy(sizePolicy)
        self.waiting_label_8.setMinimumSize(QtCore.QSize(251, 21))
        self.waiting_label_8.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.waiting_label_8.setFont(font)
        self.waiting_label_8.setObjectName("waiting_label_8")
        self.gridLayout.addWidget(self.waiting_label_8, 3, 1, 1, 1)
        cashier_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(cashier_window)
        QtCore.QMetaObject.connectSlotsByName(cashier_window)

        ########################## Stretch all columns un Product_Table1 ############
        header = self.product_table1.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        ######################### Stretch all columns un Product_Table2 ##############
        header = self.product_table2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        ######################### button connections #################################
        self.enter_button.clicked.connect(self.enter_details)
        self.pushButton_2.clicked.connect(self.transaction)
        self.pushButton_3.clicked.connect(self.report)
        self.product_table2.doubleClicked.connect(self.removerow)
        self.edit_inventory_2.clicked.connect(self.refresh_window)

        ######################### guide for table widget #############################
        self.product1 = []
        self.product2 = []
        self.quantity1 = []
        self.quantity2 = []
        self.price1 = []
        self.price2 = []
        self.price3 = []
        self.time1 = []
        self.time2 = []
        self.time3 = []
        self.time_label1 = []
        self.time_label2 = []
        self.price_label1 = []
        self.price_label2 = []
        self.receipt = []

        ######################## DATABASE functions ##########################
        self.connection()
        self.createTable()
        self.displayData()
        self.productslist()

    def retranslateUi(self, cashier_window):
        _translate = QtCore.QCoreApplication.translate
        cashier_window.setWindowTitle(_translate("cashier_window", "Cashier System"))
        self.title_label.setText(_translate("cashier_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">&quot;CASHIER (Worker)&quot;</span></p></body></html>"))
        self.transaction_label.setText(_translate("cashier_window", "Transaction Details:"))
        item = self.product_table2.horizontalHeaderItem(0)
        item.setText(_translate("cashier_window", "Product Name"))
        item = self.product_table2.horizontalHeaderItem(1)
        item.setText(_translate("cashier_window", "Quantity"))
        item = self.product_table2.horizontalHeaderItem(2)
        item.setText(_translate("cashier_window", "Total Price"))
        item = self.product_table2.horizontalHeaderItem(3)
        item.setText(_translate("cashier_window", "Time to Cook (MM)"))
        self.products.setItemText(0, _translate("cashier_window", "-- Please select an item --"))
        self.quantity.setSuffix(_translate("cashier_window", " Qty"))
        self.enter_button.setText(_translate("cashier_window", "Enter"))
        self.enterqty_label.setText(_translate("cashier_window", "Enter Quantity:"))
        self.enter_label.setText(_translate("cashier_window", "Select a Product:"))
        self.waiting_label_6.setText(_translate("cashier_window", "Estimate time of waiting of order:"))
        self.time_label.setText(_translate("cashier_window", "<html><head/><body><p>0</p></body></html>"))
        self.waiting_label_7.setText(_translate("cashier_window", "<html><head/><body><p>TIME (MM)</p></body></html>"))
        self.total_label_3.setText(_translate("cashier_window", "Total Price of the transaction:"))
        self.price_label.setText(_translate("cashier_window", "<html><head/><body><p>0.0</p></body></html>"))
        self.php_label_3.setText(_translate("cashier_window", "<html><head/><body><p>PHP</p><p><br/></p></body></html>"))
        item = self.product_table1.horizontalHeaderItem(0)
        item.setText(_translate("cashier_window", "Product Name"))
        item = self.product_table1.horizontalHeaderItem(1)
        item.setText(_translate("cashier_window", "Stocks Left"))
        item = self.product_table1.horizontalHeaderItem(2)
        item.setText(_translate("cashier_window", "Price"))
        item = self.product_table1.horizontalHeaderItem(3)
        item.setText(_translate("cashier_window", "Cooking Time (MM) "))
        self.product_label.setText(_translate("cashier_window", "<html><head/><body><p>Products:</p></body></html>"))
        self.pushButton_3.setText(_translate("cashier_window", "Open Reporting System"))
        self.waiting_label_3.setText(_translate("cashier_window", "<html><head/><body><p><span style=\" font-size:11pt;\">Data not loading correctly? Click this button:</span></p></body></html>"))
        self.payment.setSuffix(_translate("cashier_window", " PHP"))
        self.pushButton_2.setText(_translate("cashier_window", "Confirm Transaction"))
        self.edit_inventory_2.setText(_translate("cashier_window", "Refresh"))
        self.waiting_label_8.setText(_translate("cashier_window", "<html><head/><body><p align=\"right\"><span style=\" font-size:11pt;\">Enter Payment: </span></p></body></html>"))


############# SHORCUT KEYS #############
        self.enter_button.setShortcut(_translate("Ui_cashier_window", "Return"))
        self.pushButton_2.setShortcut(_translate("Ui_cashier_window", "Ctrl+P"))
        self.pushButton_3.setShortcut(_translate("Ui_cashier_window", "Ctrl+R"))
        self.edit_inventory_2.setShortcut("Ctrl+F")



# FUCNTIONS

    def enter_details(self):
        if self.products.currentIndex() == 0 and self.quantity.value() == 0:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error")
            msg.setText("No values has been Added.")
            msg.exec_()

        elif self.products.currentIndex() == 0:

            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Warning)
            msg1.setWindowTitle("Error in Item Name")
            msg1.setText("Please select a Product.")
            msg1.exec_()

        elif self.quantity.value() == 0:
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Warning)
            msg2.setWindowTitle("Error in Item Name")
            msg2.setText("Please input a value.")
            msg2.exec_()

        else:
            self.insert_database()


    def insert_database(self):

        self.connection()
        self.mycursor.execute("SELECT DISTINCT products FROM transaction")
        self.result90 = self.mycursor.fetchall()
        self.column1 = [item[0] for item in self.result90]

        sql = "SELECT quantity FROM inventory WHERE productname = %s"
        value = (self.products.currentText(), )
        self.mycursor.execute(sql, value)
        self.result91 = self.mycursor.fetchone()[0]

        if self.result91 == 0:
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Warning)
            msg1.setWindowTitle("Error, No more stocks")
            msg1.setText("Please add more stock to this product: " + self.products.currentText())
            msg1.exec_()

        elif self.quantity.value() > self.result91:
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Warning)
            msg1.setWindowTitle("Error, Insufficient stock")
            msg1.setText("Insufficient stock, please enter what's left")
            msg1.exec_()

        else:

            if self.products.currentText() not in self.column1:

                self.product_combobox = self.products.currentText()
                self.quantity_spinbox = self.quantity.value()

                sql = "SELECT price FROM inventory WHERE productname = %s"
                value = (self.product_combobox,)
                self.mycursor.execute(sql, value)
                self.result1 = self.mycursor.fetchone()[0]
                self.price_result = self.result1

                self.price_multi = self.price_result * self.quantity_spinbox
                self.price_multi1 = self.price_multi

                sql1 = "SELECT minutes FROM inventory WHERE productname = %s"
                value1 = (self.product_combobox,)
                self.mycursor.execute(sql1, value1)
                self.result2 = self.mycursor.fetchone()[0]
                self.time_result1 = self.result2

                self.sql2 = "INSERT INTO transaction (products, quantities, individualprices) VALUES (%s, %s, %s)"
                self.value2 = (self.product_combobox, self.quantity_spinbox, self.price_multi1)
                self.mycursor.execute(self.sql2, self.value2)
                self.mydb.commit()

                sql3 = "SELECT quantity FROM inventory WHERE productname = %s"
                value3 = (self.product_combobox,)
                self.mycursor.execute(sql3, value3)
                self.result3 = self.mycursor.fetchone()[0]
                self.inventory_q = self.result3

                self.update_inventory = self.inventory_q - self.quantity_spinbox
                self.update_inventory1 = self.update_inventory

                sql4 = "UPDATE inventory SET quantity = %s WHERE productname = %s"
                value4 = (self.update_inventory1, self.product_combobox)
                self.mycursor.execute(sql4, value4)
                self.mydb.commit()

                self.mycursor.execute("SELECT * FROM inventory")
                self.result = self.mycursor.fetchall()
                self.numcols = len(self.result[0])
                self.numrows = len(self.result)
                self.product_table1.setColumnCount(self.numcols)
                self.product_table1.setRowCount(self.numrows)
                for row in range(self.numrows):
                    for column in range(self.numcols):
                        self.product_table1.setItem(row, column, QTableWidgetItem(str(self.result[row][column])))

                self.price2.append(self.price_multi1)
                self.time2.append(self.time_result1)
                self.insert_table()

            else:

                self.quantity_spinbox1 = self.quantity.value()
                self.product_combobox1 = self.products.currentText()

                sql = "SELECT quantities FROM transaction WHERE products = %s"
                value = (self.product_combobox1,)
                self.mycursor.execute(sql, value)
                self.result3 = self.mycursor.fetchone()[0]
                self.quantity_get = self.result3

                self.update_quantity = self.quantity_get + self.quantity_spinbox1
                self.update_quantity1 = self.update_quantity

                sql1 = "UPDATE transaction SET quantities = %s WHERE products = %s"
                value1 = (self.update_quantity1, self.product_combobox1)
                self.mycursor.execute(sql1, value1)
                self.mydb.commit()

                sql2 = "SELECT price FROM inventory WHERE productname = %s"
                value2 = (self.product_combobox1,)
                self.mycursor.execute(sql2, value2)
                self.result4 = self.mycursor.fetchone()[0]
                self.price_result = self.result4

                self.price_multi = self.price_result * self.quantity_spinbox1
                self.price_multi1 = self.price_multi

                sql3 = "SELECT individualprices FROM transaction WHERE products = %s"
                value3 = (self.product_combobox1,)
                self.mycursor.execute(sql3, value3)
                self.result5 = self.mycursor.fetchone()[0]
                self.price_result1 = self.result5

                self.price_multi2 = self.price_result1 + self.price_multi1
                self.price_multi3 = self.price_multi2

                sql4 = "UPDATE transaction SET individualprices = %s WHERE products = %s"
                value4 = (self.price_multi3, self.product_combobox1)
                self.mycursor.execute(sql4, value4)
                self.mydb.commit()

                sql5 = "SELECT quantity FROM inventory WHERE productname = %s"
                value5 = (self.product_combobox1,)
                self.mycursor.execute(sql5, value5)
                self.result6 = self.mycursor.fetchone()[0]
                self.inventory_q = self.result6

                self.update_inventory = self.inventory_q - self.quantity_spinbox1
                self.update_inventory1 = self.update_inventory

                sql6 = "UPDATE inventory SET quantity = %s WHERE productname = %s"
                value6 = (self.update_inventory1, self.product_combobox1)
                self.mycursor.execute(sql6, value6)
                self.mydb.commit()

                sql7 = "SELECT minutes FROM inventory WHERE productname = %s"
                value7 = (self.product_combobox1,)
                self.mycursor.execute(sql7, value7)
                self.result7 = self.mycursor.fetchone()[0]
                self.time_result1 = self.result7

                self.mycursor.execute("SELECT * FROM inventory")
                self.result = self.mycursor.fetchall()
                self.numcols = len(self.result[0])
                self.numrows = len(self.result)
                self.product_table1.setColumnCount(self.numcols)
                self.product_table1.setRowCount(self.numrows)
                for row in range(self.numrows):
                    for column in range(self.numcols):
                        self.product_table1.setItem(row, column, QTableWidgetItem(str(self.result[row][column])))

                self.price2.append(self.price_multi1)
                self.time2.append(self.time_result1)

                self.insert_table()


    def insert_table(self):
        self.connection()

        self.products_1 = self.products.currentText()
        self.quantity_1 = self.quantity.value()
        try:

            if self.products.currentText() not in self.product1:
                self.product1.append(self.products_1)
                self.quantity1.append(self.quantity_1)
                self.price1.append(self.price_multi1)
                self.time1.append(self.time_result1)

                self.product_table2.setRowCount(0)
                for product, quantity, individual, time in zip(self.product1, self.quantity1, self.price1, self.time1):
                    self.rowcount1 = self.product_table2.rowCount()
                    self.product_table2.setRowCount(self.rowcount1 + 1)
                    self.product_table2.setItem(self.rowcount1, 0, QtWidgets.QTableWidgetItem(product))
                    self.product_table2.setItem(self.rowcount1, 1, QtWidgets.QTableWidgetItem(str(quantity)))
                    self.product_table2.setItem(self.rowcount1, 2, QtWidgets.QTableWidgetItem(str(individual)))
                    self.product_table2.setItem(self.rowcount1, 3, QtWidgets.QTableWidgetItem(str(time)))

                lastrow = self.product_table2.rowCount()
                self.receipt.insert(lastrow, [self.products_1, self.quantity_1, self.price_multi1])

            else:
                self.index1 = self.product1.index(self.products.currentText())
                self.quantity1_update = self.quantity1[self.index1] + self.quantity_1
                self.quantity1.pop(self.index1)
                self.quantity1.insert(self.index1, self.quantity1_update)

                sql = "SELECT price FROM inventory WHERE productname = %s"
                value = (self.products_1,)
                self.mycursor.execute(sql, value)
                self.result = self.mycursor.fetchone()[0]

                self.price_update = self.result * self.quantity_1
                self.price_update1 = self.price_update + self.price1[self.index1]
                self.price_update2 = self.price_update1
                self.price1.pop(self.index1)
                self.price1.insert(self.index1, self.price_update2)

                sql1 = "SELECT minutes FROM inventory WHERE productname = %s"
                value1 = (self.products_1,)
                self.mycursor.execute(sql1, value1)
                self.result1 = self.mycursor.fetchone()[0]

                self.time_update = self.result1 + self.time1[self.index1]
                self.time_update1 = self.time_update
                self.time1.pop(self.index1)
                self.time1.insert(self.index1, self.time_update1)

                self.product_table2.setRowCount(0)
                for product, quantity, individual, time in zip(self.product1, self.quantity1, self.price1, self.time1):
                    self.rowcount1 = self.product_table2.rowCount()
                    self.product_table2.setRowCount(self.rowcount1 + 1)
                    self.product_table2.setItem(self.rowcount1, 0, QtWidgets.QTableWidgetItem(product))
                    self.product_table2.setItem(self.rowcount1, 1, QtWidgets.QTableWidgetItem(str(quantity)))
                    self.product_table2.setItem(self.rowcount1, 2, QtWidgets.QTableWidgetItem(str(individual)))
                    self.product_table2.setItem(self.rowcount1, 3, QtWidgets.QTableWidgetItem(str(time)))

                lastrow = self.product_table2.rowCount()
                self.receipt.insert(lastrow, [self.products_1, self.quantity_1, self.price_multi1])

            self.sum_totalprice = float(sum(self.price1))
            self.sum_estimatetime = (sum(self.time1))
            self.sum_quantity = (sum(self.quantity1))
            self.price_label1.append(float(self.sum_totalprice))
            self.time_label1.append(self.sum_estimatetime)

            self.price_label2.insert(0, float(self.sum_totalprice))
            self.time_label2.insert(0, int(self.sum_estimatetime))

            self.price_label.setText(str(self.price_label1[0]))
            self.time_label.setText(str(self.time_label1[0]))

            self.price_label1.pop(0)
            self.time_label1.pop(0)

            self.price_label2.pop(1)
            self.time_label2.pop(1)

        except:
            print("TEST")

    def displayData(self):
        self.mycursor.execute("SELECT DISTINCT productname FROM inventory")
        self.result92 = self.mycursor.fetchall()

        self.column3 = [item[0] for item in self.result92]

        if len(self.column3) == 0:
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setWindowTitle("First Start")
            msg2.setText("Hello, it feels like this is your first time running the program since the database is empty. "
                         "We would like to load all preloaded data for this program. ")
            msg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg2.buttonClicked.connect(self.answer)
            msg2.exec_()

        else:
            self.mycursor.execute("SELECT * FROM inventory")
            self.result = self.mycursor.fetchall()

            self.numcols = len(self.result[0])
            self.numrows = len(self.result)

            self.product_table1.setColumnCount(self.numcols)
            self.product_table1.setRowCount(self.numrows)

            for row in range(self.numrows):
                for column in range(self.numcols):
                    self.product_table1.setItem(row, column, QTableWidgetItem(str(self.result[row][column])))


    def answer(self, i):
        if i.text() == '&Yes':
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setWindowTitle("First Start")
            msg2.setText("Great!, Let's start")
            msg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg2.exec_()
            self.preloaddata()
        if i.text() == '&No':
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Information)
            msg2.setWindowTitle("First Start")
            msg2.setText("Alright!, You may explore on your own.")
            msg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg2.exec_()

    def createTable(self):
        try:
            self.mycursor.execute("CREATE TABLE inventory (productname VARCHAR(20) PRIMARY KEY, quantity INT NOT NULL, price FLOAT NOT NULL, minutes INT DEFAULT 0)")
            self.mycursor.execute(
                "CREATE TABLE transaction (products VARCHAR(20) PRIMARY KEY, quantities INT NOT NULL, individualprices FLOAT NOT NULL)")

        except:
            print("Table is already created")

    def productslist(self):
        self.mycursor.execute("SELECT productname FROM inventory")
        self.myresult = self.mycursor.fetchall()
        for i in self.myresult:
            self.products.addItems(i)

    def transaction(self):

        self.rowcount = self.product_table2.rowCount()

        if self.rowcount == 0 and self.payment.value() == 0:
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Warning)
            msg3.setWindowTitle("Error")
            msg3.setText("Transaction Table is empty, please start a transaction. ")
            msg3.exec_()

        elif self.rowcount == 0:
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Warning)
            msg3.setWindowTitle("Error")
            msg3.setText("No products has been inputted. ")
            msg3.exec_()

        elif self.payment.value() == 0:
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Warning)
            msg3.setWindowTitle("Error")
            msg3.setText("Please enter the payment. ")
            msg3.exec_()

        else:
            if self.price_label2[0] > self.payment.value():
                msg4 = QMessageBox()
                msg4.setWindowTitle("Error")
                msg4.setText("Total price is higher than the payment.")
                msg4.setIcon(QMessageBox.Warning)
                msg4.exec_()

            else:

                self.change = self.payment.value() - self.price_label2[0]
                msg4 = QMessageBox()
                msg4.setWindowTitle("Transaction Success")
                msg4.setText("Transaction is completed, here is your change: " + "PHP " + str(self.change))
                msg4.setIcon(QMessageBox.Information)
                msg4.exec_()

                print("PRINTING")
                font = {"height": 12,}
                print(self.time_label2[0])
                self.gettime = self.time_label2[0]

                with Printer(linegap=0) as printer:
                    printer.text("> Ihawan Service <" + "\n" + "Official Receipt" + "\n" +
                                 "############################################" + "\n", align="center", font_config=font)
                    printer.text("::DETAILS:: " + "\n", align="center", font_config=font)
                    printer.text("Estimate Waiting Time: "+ str(self.sum_estimatetime) + " (In minutes)" + "\n", align="center", font_config=font)
                    printer.text("Total Products: " + str(self.sum_quantity) + " Piece/s" + "\n", align="center", font_config=font)
                    printer.text("Total Price: " + str(self.sum_totalprice) + " PHP" + "\n", align="center", font_config=font)
                    printer.text("Amount Paid: " + str(self.payment.value()) + " PHP" + "\n", align="center", font_config=font)
                    printer.text("Change: " + str(self.change) + " PHP" + "\n", align="center", font_config=font)
                    printer.text("############################################" + "\n", align="center", font_config=font)
                    printer.text("::PRODUCTS BOUGHT:: " + "\n", align="center", font_config=font)

                    for items in self.product1:
                        printer.text(''.join([str(x)for x in items]), align="center", font_config=font)

                    printer.text("\n", align="center", font_config=font)
                    printer.text("############################################", align="center", font_config=font)
                    printer.text("Thank You for buying at Ihawan Service.", align="center", font_config=font)

                self.product_table2.setRowCount(0)
                self.products.setCurrentIndex(0)
                self.quantity.setValue(0)
                self.price_label.setText("0.0")
                self.time_label.setText("0")
                self.payment.setValue(0)
                self.product1.clear()
                self.quantity1.clear()
                self.price1.clear()
                self.time1.clear()

    def removerow(self):
        cursor = (self.product_table2.selectionModel().currentIndex())
        product = (cursor.siblingAtColumn(0).data())
        quantity = (cursor.siblingAtColumn(1).data())
        price = (cursor.siblingAtColumn(2).data())
        time = (cursor.siblingAtColumn(3).data())
        self.product2.append(product)
        self.quantity2.append(int(quantity))
        self.price3.append(float(price))
        self.time3.append(int(time))
        self.getproduct = self.product2[0]
        self.getquantity = self.quantity2[0]
        self.getprice = self.price3[0]
        self.gettime = self.time3[0]

        sql = "SELECT quantity FROM inventory WHERE productname = %s"
        value = (self.getproduct,)
        self.mycursor.execute(sql, value)
        self.got4 = self.mycursor.fetchone()[0]

        sql1 = "SELECT quantities FROM transaction WHERE products = %s"
        value1 = (self.getproduct,)
        self.mycursor.execute(sql1, value1)
        self.got5 = self.mycursor.fetchone()[0]

        sql2 = "SELECT individualprices FROM transaction WHERE products = %s"
        value2 = (self.getproduct,)
        self.mycursor.execute(sql2, value2)
        self.got6 = self.mycursor.fetchone()[0]

        self.deduct = self.got4 + self.getquantity
        self.deductcopy = self.deduct
        self.add = self.got5 - self.getquantity
        self.addcopy = self.add
        self.deduct1 = self.got6 - int(self.getprice)
        self.deduct1copy = self.deduct1

        updatedatabase1 = "UPDATE inventory SET quantity = %s WHERE productname = %s"
        data1 = (self.deductcopy, self.getproduct)

        self.mycursor.execute(updatedatabase1, data1)
        self.mydb.commit()

        updatedatabase2 = "UPDATE transaction SET quantities = %s WHERE products = %s"
        data2 = (self.addcopy, self.getproduct)
        self.mycursor.execute(updatedatabase2, data2)
        self.mydb.commit()
        updatedatabase3 = "UPDATE transaction SET individualprices = %s WHERE products = %s"
        data3 = (self.deduct1copy, self.getproduct)
        self.mycursor.execute(updatedatabase3, data3)
        self.mydb.commit()

        self.mycursor.execute("SELECT * FROM inventory")
        self.result = self.mycursor.fetchall()
        self.numcols = len(self.result[0])
        self.numrows = len(self.result)
        self.product_table1.setColumnCount(self.numcols)
        self.product_table1.setRowCount(self.numrows)
        for row in range(self.numrows):
            for column in range(self.numcols):
                self.product_table1.setItem(row, column, QTableWidgetItem(str(self.result[row][column])))

        self.index2 = self.product1.index(product)

        self.product1.pop(self.index2)
        self.quantity1.pop(self.index2)
        self.price1.pop(self.index2)
        self.time1.pop(self.index2)

        self.price_label3 = self.price_label2[0] - self.getprice
        self.price_label2.pop(0)
        self.price_label2.insert(0, self.price_label3)

        self.time_label3 = self.time_label2[0] - self.gettime
        self.time_label2.pop(0)
        self.time_label2.insert(0, self.time_label3)

        self.time3.pop(0)
        self.time2.clear()
        self.price3.pop(0)
        self.price2.clear()
        self.product2.pop(0)
        self.quantity2.pop(0)
        self.time_label.setText(str(self.time_label2[0]))
        self.price_label.setText(str(self.price_label2[0]))
        self.product_table2.removeRow(self.product_table2.currentRow())


    def report(self):
        msg3 = QMessageBox()
        msg3.setIcon(QMessageBox.Information)
        msg3.setWindowTitle("Opening window...")
        msg3.setText("Reporting System Window will open")
        msg3.exec_()

        self.window = QtWidgets.QMainWindow()
        self.window = closeWindow()
        self.ui = Ui_report()
        self.ui.setupUi(self.window)
        self.window.show()


    def refresh_window(self):

        self.connection()

        self.mycursor.execute("SELECT * FROM inventory")
        self.result = self.mycursor.fetchall()

        self.numcols = len(self.result[0])
        self.numrows = len(self.result)

        self.product_table1.setColumnCount(self.numcols)
        self.product_table1.setRowCount(self.numrows)

        for row in range(self.numrows):
            for column in range(self.numcols):
                self.product_table1.setItem(row, column, QTableWidgetItem(str(self.result[row][column])))

        self.products.clear()
        self.products.addItem("-- Please select an item --")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/676723.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.products.setItemIcon(0, icon1)
        self.mycursor.execute("SELECT productname FROM inventory")
        self.myresult = self.mycursor.fetchall()
        for i in self.myresult:
            self.products.addItems(i)

        msg3 = QMessageBox()
        msg3.setIcon(QMessageBox.Information)
        msg3.setWindowTitle("Success")
        msg3.setText("Data has been refreshed.")
        msg3.exec_()

    def preloaddata(self):

        data = "INSERT INTO inventory (productname, quantity, price, minutes) VALUES (%s, %s, %s, %s)"
        data1 = [("Pork BBQ", "20", "25", "15"),
                 ("Chicken BBQ", "20", "25", "12"),
                 ("Bulaklak", "20", "20", "10"),
                 ("Tenga", "20", "20", "9"),
                 ("Pindonggo", "20", "18", "10"),
                 ("Pork Liver", "20", "18", "8"),
                 ("Hotdog", "20", "18", "5"),
                 ("Chicken Head", "20", "12", "12"),
                 ("Chicken Feet", "20", "12", "8"),
                 ("Pork Intestine", "20", "10", "8"),
                 ("Chicken Skin", "20", "10", "5"),
                 ("Pork Skin", "20", "10", "8"),
                 ("Pork Lamad", "20", "10", "8"),
                 ("Pork Kidney", "20", "10", "10"),
                 ("Chicken Isaw (S)", "20", "7", "5"),
                 ("Chicken Isaw (L)", "20", "10", "3"),
                 ("Betamax", "20", "6", "8")]

        #data2 = [item[0] for item in data1]

        self.mycursor.executemany(data, data1)
        self.mydb.commit()
        self.displayData()

cashier = Ui_cashier_window

class closeWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Cashier System', 'Are you sure you want to exit?''  ',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cashier_window = QtWidgets.QMainWindow()
    cashier_window = closeWindow()
    ui = Ui_cashier_window()
    ui.setupUi(cashier_window)
    cashier_window.show()
    sys.exit(app.exec_())

