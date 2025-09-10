from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 431)
        self.load_user_data = QAction(MainWindow)
        self.load_user_data.setObjectName(u"load_user_data")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 541, 371))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.username_textbox = QLineEdit(self.horizontalLayoutWidget)
        self.username_textbox.setObjectName(u"username_textbox")
        self.username_textbox.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.username_textbox)

        self.token_textbox = QLineEdit(self.horizontalLayoutWidget)
        self.token_textbox.setObjectName(u"token_textbox")
        self.token_textbox.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.token_textbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.account_button = QPushButton(self.horizontalLayoutWidget)
        self.account_button.setObjectName(u"account_button")

        self.verticalLayout.addWidget(self.account_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.graph_detail_button = QPushButton(self.horizontalLayoutWidget)
        self.graph_detail_button.setObjectName(u"graph_detail_button")

        self.gridLayout.addWidget(self.graph_detail_button, 2, 0, 1, 1)

        self.int_type = QRadioButton(self.horizontalLayoutWidget)
        self.int_type.setObjectName(u"int_type")
        self.int_type.setChecked(True)

        self.gridLayout.addWidget(self.int_type, 2, 1, 1, 1)

        self.colors_dropdown = QComboBox(self.horizontalLayoutWidget)
        self.colors_dropdown.addItem("")
        self.colors_dropdown.addItem("")
        self.colors_dropdown.addItem("")
        self.colors_dropdown.addItem("")
        self.colors_dropdown.addItem("")
        self.colors_dropdown.addItem("")
        self.colors_dropdown.setObjectName(u"colors_dropdown")

        self.gridLayout.addWidget(self.colors_dropdown, 0, 0, 1, 1)

        self.graph_unit_text = QLineEdit(self.horizontalLayoutWidget)
        self.graph_unit_text.setObjectName(u"graph_unit_text")

        self.gridLayout.addWidget(self.graph_unit_text, 1, 1, 1, 1)

        self.graph_name_text = QLineEdit(self.horizontalLayoutWidget)
        self.graph_name_text.setObjectName(u"graph_name_text")

        self.gridLayout.addWidget(self.graph_name_text, 0, 1, 1, 1)

        self.float_type = QRadioButton(self.horizontalLayoutWidget)
        self.float_type.setObjectName(u"float_type")

        self.gridLayout.addWidget(self.float_type, 3, 1, 1, 1)

        self.graph_id_box = QLineEdit(self.horizontalLayoutWidget)
        self.graph_id_box.setObjectName(u"graph_id_box")
        self.graph_id_box.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.graph_id_box, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.date_widget = QDateEdit(self.horizontalLayoutWidget)
        self.date_widget.setObjectName(u"date_widget")
        self.date_widget.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.date_widget)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.quantity = QSlider(self.horizontalLayoutWidget)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setMaximum(9)
        self.quantity.setSingleStep(1)
        self.quantity.setValue(5)
        self.quantity.setSliderPosition(5)
        self.quantity.setOrientation(Qt.Horizontal)
        self.quantity.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.quantity)

        self.slider_value = QLabel(self.horizontalLayoutWidget)
        self.slider_value.setObjectName(u"slider_value")
        font = QFont()
        font.setPointSize(8)
        self.slider_value.setFont(font)

        self.horizontalLayout_2.addWidget(self.slider_value)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.update_graph_button = QPushButton(self.horizontalLayoutWidget)
        self.update_graph_button.setObjectName(u"update_graph_button")

        self.verticalLayout.addWidget(self.update_graph_button)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.response_output_box = QTextBrowser(self.horizontalLayoutWidget)
        self.response_output_box.setObjectName(u"response_output_box")
        self.response_output_box.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.response_output_box)

        self.edit_account_button = QPushButton(self.horizontalLayoutWidget)
        self.edit_account_button.setObjectName(u"edit_account_button")

        self.verticalLayout_5.addWidget(self.edit_account_button)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, 0)
        self.save_button = QPushButton(self.horizontalLayoutWidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_3.addWidget(self.save_button)

        self.load_button = QPushButton(self.horizontalLayoutWidget)
        self.load_button.setObjectName(u"load_button")

        self.horizontalLayout_3.addWidget(self.load_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(25, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 565, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.load_user_data)

        self.retranslateUi(MainWindow)
        self.quantity.valueChanged.connect(self.slider_value.setNum)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_user_data.setText(QCoreApplication.translate("MainWindow", u"Load User Data", None))
        self.username_textbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.token_textbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.account_button.setText(QCoreApplication.translate("MainWindow", u"Create Account/Authenticate Account", None))
        self.graph_detail_button.setText(QCoreApplication.translate("MainWindow", u"Enter Graph Details", None))
        self.int_type.setText(QCoreApplication.translate("MainWindow", u"Int", None))
        self.colors_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"ajisai", None))
        self.colors_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"shibafu", None))
        self.colors_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"momiji", None))
        self.colors_dropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"sora", None))
        self.colors_dropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"ichou", None))
        self.colors_dropdown.setItemText(5, QCoreApplication.translate("MainWindow", u"kuro", None))

        self.graph_unit_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Unit To Measure (Km, g, sec, etc)", None))
        self.graph_name_text.setText("")
        self.graph_name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Graph Name", None))
        self.float_type.setText(QCoreApplication.translate("MainWindow", u"Float", None))
        self.graph_id_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Id or leave empty", None))
        self.slider_value.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.update_graph_button.setText(QCoreApplication.translate("MainWindow", u"Add Info To Graph", None))
        self.edit_account_button.setText(QCoreApplication.translate("MainWindow", u"Edit Account Detials", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

