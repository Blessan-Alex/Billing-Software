from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
                                           "    background-color: rgb(56, 58, 89);    \n"
                                           "    color: rgb(220, 220, 220);\n"
                                           "    border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 90, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(44, 121, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 150, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    \n"
                                       "    background-color: rgb(98, 114, 164);\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(0, 100, 199, 255), stop:1 rgba(170, 150, 255, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(0, 320, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(20, 350, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate(
            "SplashScreen", "<strong>BILLING</strong> SOFTWARE"))
        self.label_description.setText(_translate(
            "SplashScreen", "<strong>APP</strong> DESCRIPTION"))
        self.label_loading.setText(_translate("SplashScreen", "Loading..."))
