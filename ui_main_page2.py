# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_3_complete.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 646)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("QPushButton {\n"
                                      "    background-position: center;\n"
                                      "    background-repeat: no-reperat;\n"
                                      "    border: none;\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(33, 37, 43);\n"
                                      "}\n"
                                      "QPushButton:pressed {    \n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.Btn_Toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/24x24/cil-menu.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QtCore.QSize(24, 24))
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(
            "background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/24x24/cil-home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_1.setIcon(icon1)
        self.btn_page_1.setIconSize(QtCore.QSize(24, 24))
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/24x24/database-24.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_2.setIcon(icon2)
        self.btn_page_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(35, 35, 35);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}")
        self.btn_page_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/24x24/cil-user.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_3.setIcon(icon3)
        self.btn_page_3.setIconSize(QtCore.QSize(24, 24))
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(
            self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ledit_productname = QtWidgets.QLineEdit(self.frame)
        self.ledit_productname.setMinimumSize(QtCore.QSize(0, 30))
        self.ledit_productname.setStyleSheet("QLineEdit {\n"
                                             "    background-color: rgb(27, 29, 35);\n"
                                             "    border-radius: 5px;\n"
                                             "    border: 2px solid rgb(27, 29, 35);\n"
                                             "    padding-left: 10px;\n"
                                             "   color:rgb(100, 255, 255)\n"
                                             "}\n"
                                             "QLineEdit:hover {\n"
                                             "    border: 2px solid rgb(64, 71, 88);\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(91, 101, 124);\n"
                                             "}\n"
                                             "")
        self.ledit_productname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ledit_productname.setObjectName("ledit_productname")
        self.verticalLayout_9.addWidget(self.ledit_productname)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem3)
        self.ledit_price = QtWidgets.QLineEdit(self.frame)
        self.ledit_price.setMinimumSize(QtCore.QSize(0, 30))
        self.ledit_price.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(27, 29, 35);\n"
                                       "    border-radius: 5px;\n"
                                       "    border: 2px solid rgb(27, 29, 35);\n"
                                       "    padding-left: 10px;\n"
                                       "    \n"
                                       "    color: rgb(100, 255, 255);\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    border: 2px solid rgb(64, 71, 88);\n"
                                       "}\n"
                                       "QLineEdit:focus {\n"
                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                       "}")
        self.ledit_price.setObjectName("ledit_price")
        self.verticalLayout_9.addWidget(self.ledit_price)
        self.btn_checkdb = QtWidgets.QPushButton(self.frame)
        self.btn_checkdb.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/24x24/cil-x-circle.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_checkdb.setIcon(icon4)
        self.btn_checkdb.setIconSize(QtCore.QSize(30, 30))
        self.btn_checkdb.setFlat(True)
        self.btn_checkdb.setObjectName("btn_checkdb")
        self.verticalLayout_9.addWidget(self.btn_checkdb)
        self.btn_insertdata = QtWidgets.QPushButton(self.frame)
        self.btn_insertdata.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btn_insertdata.setFont(font)
        self.btn_insertdata.setStyleSheet("QPushButton {\n"
                                          "    border: 2px solid rgb(52, 59, 72);\n"
                                          "    border-radius: 5px;    \n"
                                          "    background-color: rgb(52, 59, 72);\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(57, 65, 80);\n"
                                          "    border: 2px solid rgb(61, 70, 86);\n"
                                          "}\n"
                                          "QPushButton:pressed {    \n"
                                          "    background-color: rgb(35, 40, 49);\n"
                                          "    border: 2px solid rgb(43, 50, 61);\n"
                                          "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            "icons/16x16/cil-cloud-upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_insertdata.setIcon(icon5)
        self.btn_insertdata.setObjectName("btn_insertdata")
        self.verticalLayout_9.addWidget(self.btn_insertdata)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem5)
        self.btn_showdatabase = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_showdatabase.setFont(font)
        self.btn_showdatabase.setStyleSheet("QPushButton {\n"
                                            "    border: 2px solid rgb(52, 59, 72);\n"
                                            "    border-radius: 5px;    \n"
                                            "    background-color: rgb(52, 59, 72);\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(57, 65, 80);\n"
                                            "    border: 2px solid rgb(61, 70, 86);\n"
                                            "}\n"
                                            "QPushButton:pressed {    \n"
                                            "    background-color: rgb(35, 40, 49);\n"
                                            "    border: 2px solid rgb(43, 50, 61);\n"
                                            "}")
        self.btn_showdatabase.setIcon(icon2)
        self.btn_showdatabase.setIconSize(QtCore.QSize(14, 14))
        self.btn_showdatabase.setObjectName("btn_showdatabase")
        self.verticalLayout_9.addWidget(self.btn_showdatabase)
        self.table_data = QtWidgets.QTableWidget(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 44, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(210, 210, 210, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.table_data.setPalette(palette)
        self.table_data.setStyleSheet("QTableWidget {    \n"
                                      "    background-color: rgb(39, 44, 54);\n"
                                      "    padding: 10px;\n"
                                      "    border-radius: 5px;\n"
                                      "    gridline-color: rgb(44, 49, 60);\n"
                                      "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item{\n"
                                      "    border-color: rgb(44, 49, 60);\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-right: 5px;\n"
                                      "    gridline-color: rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::item:selected{\n"
                                      "    background-color: rgb(85, 170, 255);\n"
                                      "}\n"
                                      "QScrollBar:horizontal {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    height: 14px;\n"
                                      "    margin: 0px 21px 0 21px;\n"
                                      "    border-radius: 0px;\n"
                                      "}\n"
                                      " QScrollBar:vertical {\n"
                                      "    border: none;\n"
                                      "    background: rgb(52, 59, 72);\n"
                                      "    width: 14px;\n"
                                      "    margin: 21px 0 21px 0;\n"
                                      "    border-radius: 0px;\n"
                                      " }\n"
                                      "QHeaderView::section{\n"
                                      "    Background-color: rgb(39, 44, 54);\n"
                                      "    max-width: 30px;\n"
                                      "    border: 1px solid rgb(44, 49, 60);\n"
                                      "    border-style: none;\n"
                                      "    border-bottom: 1px solid rgb(44, 49, 60);\n"
                                      "    border-right: 1px solid rgb(44, 49, 60);\n"
                                      "}\n"
                                      "QTableWidget::horizontalHeader {    \n"
                                      "    background-color: rgb(81, 255, 0);\n"
                                      "}\n"
                                      "QHeaderView::section:horizontal\n"
                                      "{\n"
                                      "    border: 1px solid rgb(32, 34, 42);\n"
                                      "    background-color: rgb(27, 29, 35);\n"
                                      "    padding: 3px;\n"
                                      "    border-top-left-radius: 7px;\n"
                                      "    border-top-right-radius: 7px;\n"
                                      "}\n"
                                      "QHeaderView::section:vertical\n"
                                      "{\n"
                                      "    border: 1px solid rgb(44, 49, 60);\n"
                                      "}")
        self.table_data.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_data.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.table_data.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.table_data.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_data.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_data.setAlternatingRowColors(False)
        self.table_data.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.table_data.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.table_data.setShowGrid(True)
        self.table_data.setGridStyle(QtCore.Qt.SolidLine)
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(3)
        self.table_data.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        item.setFont(font)
        self.table_data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(100, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(100, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(100, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_data.setItem(0, 1, item)
        self.table_data.horizontalHeader().setVisible(False)
        self.table_data.horizontalHeader().setCascadingSectionResizes(True)
        self.table_data.horizontalHeader().setDefaultSectionSize(200)
        self.table_data.horizontalHeader().setStretchLastSection(True)
        self.table_data.verticalHeader().setVisible(False)
        self.table_data.verticalHeader().setCascadingSectionResizes(False)
        self.table_data.verticalHeader().setHighlightSections(False)
        self.table_data.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_9.addWidget(self.table_data)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFF;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ledit_productname.setPlaceholderText(
            _translate("MainWindow", "Product Name"))
        self.ledit_price.setPlaceholderText(
            _translate("MainWindow", "Product Price"))
        self.btn_insertdata.setText(_translate("MainWindow", "Insert Data"))
        self.btn_showdatabase.setText(
            _translate("MainWindow", "Show Database"))
        self.table_data.setSortingEnabled(False)
        item = self.table_data.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.table_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        __sortingEnabled = self.table_data.isSortingEnabled()
        self.table_data.setSortingEnabled(False)
        self.table_data.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "PAGE 3"))
#import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
