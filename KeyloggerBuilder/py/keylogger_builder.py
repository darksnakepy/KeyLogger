from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 417)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/images/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #121212;")
        self.username_field = QtWidgets.QTextEdit(MainWindow)
        self.username_field.setGeometry(QtCore.QRect(70, 150, 171, 31))
        self.username_field.setStyleSheet("QTextEdit {\n"
        "border: 1px solid #cfcfcf;\n"
        "border-radius: 15px;\n"
        "color: #fff;\n"
        "}\n"
        "\n"
        "QTextEdit::Text {\n"
        "    color: #fff;\n"
        "}")
        self.username_field.setObjectName("username_field")
        self.username_field_2 = QtWidgets.QTextEdit(MainWindow)
        self.username_field_2.setGeometry(QtCore.QRect(70, 210, 171, 31))
        self.username_field_2.setStyleSheet("border: 1px solid #cfcfcf;\n"
        "border-radius: 15px;\n"
        "color: #fff;")
        self.username_field_2.setObjectName("username_field_2")
        self.login_button = QtWidgets.QPushButton(MainWindow)
        self.login_button.setGeometry(QtCore.QRect(154, 290, 81, 31))
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.login_button.setStyleSheet("QPushButton {\n"
        "    background-color: #9200b3;\n"
        "    border-radius: 15px;\n"
        "    color: #cfcfcf;\n"
        "    font-weight: bold;\n"
# ìèà4
        "}\n"
        "\n"
        "\n"
        "\n"
        "QPushButton:hover {\n"
        "    color: #fff;\n"
        "    background-color: #6f0387;\n"
        "}")
        self.login_button.setObjectName("login_button")
        self.login_text = QtWidgets.QLabel(MainWindow)
        self.login_text.setGeometry(QtCore.QRect(70, 50, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.login_text.setFont(font)
        self.login_text.setStyleSheet("color: #cfcfcf;")
        self.login_text.setAlignment(QtCore.Qt.AlignCenter)
        self.login_text.setObjectName("login_text")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.username_field.setPlaceholderText(_translate("MainWindow", "Username"))
        self.username_field_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.login_text.setText(_translate("MainWindow", "Login"))

if __name__ == "__main__": 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    giglo = QtWidgets.QMainWindow()
    frame = Ui_MainWindow()
    frame.setupUi(giglo)
    giglo.show()
    sys.exit(app.exec_())