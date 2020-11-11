from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 810)
        MainWindow.setStyleSheet("*{\n"
"font-style: century gothic;\n"
"}\n"
"QWidget#centralwidget{\n"
"background-image: url(:/images/images/fondo config nuevas dimensiones.png);\n"
"}\n"
"QFrame#hora{\n"
"background-image: url(:/images/images/hora nuevas dimensiones.png);\n"
"}\n"
"QPushButton#Atras{\n"
"background: transparent;\n"
"border:none;\n"
"font-size:25px;\n"
"}\n"
"QPushButton#Atras:hover{\n"
"background: transparent;\n"
"border:none;\n"
"font-size:27px;\n"
"font-weigth:bold;\n"
"}\n"
"QLabel#titulo{\n"
"font-size:25px;\n"
"background:transparent;\n"
"}\n"
"QFrame{\n"
"background:#7A0808;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"background:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"font-size:15px;\n"
"background:transparent;\n"
"font-weight:bold;\n"
"}\n"
"QFrame#tuerca{\n"
"background-image: url(:/images/images/Screenshot_1.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hora = QtWidgets.QFrame(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(0, 0, 379, 37))
        self.hora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hora.setObjectName("hora")
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setGeometry(QtCore.QRect(0, 50, 61, 31))
        self.Atras.setObjectName("Atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(90, 60, 201, 71))
        self.titulo.setObjectName("titulo")
        self.puntitos = QtWidgets.QFrame(self.centralwidget)
        self.puntitos.setGeometry(QtCore.QRect(30, 170, 16, 16))
        self.puntitos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos.setObjectName("puntitos")
        self.puntitos_2 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_2.setGeometry(QtCore.QRect(30, 240, 16, 16))
        self.puntitos_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_2.setObjectName("puntitos_2")
        self.puntitos_3 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_3.setGeometry(QtCore.QRect(30, 310, 16, 16))
        self.puntitos_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_3.setObjectName("puntitos_3")
        self.puntitos_4 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_4.setGeometry(QtCore.QRect(30, 380, 16, 16))
        self.puntitos_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_4.setObjectName("puntitos_4")
        self.puntitos_5 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_5.setGeometry(QtCore.QRect(30, 450, 16, 16))
        self.puntitos_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_5.setObjectName("puntitos_5")
        self.puntitos_6 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_6.setGeometry(QtCore.QRect(30, 520, 16, 16))
        self.puntitos_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_6.setObjectName("puntitos_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 310, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 380, 171, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 450, 121, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 520, 101, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tuerca = QtWidgets.QFrame(self.centralwidget)
        self.tuerca.setGeometry(QtCore.QRect(130, 600, 120, 121))
        self.tuerca.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tuerca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tuerca.setObjectName("tuerca")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Atras.setText(_translate("MainWindow", "←"))
        self.titulo.setText(_translate("MainWindow", "CONFIGURACIÓN"))
        self.pushButton.setText(_translate("MainWindow", "Privacidad"))
        self.pushButton_2.setText(_translate("MainWindow", "Configuración de chat"))
        self.pushButton_3.setText(_translate("MainWindow", "Seguridad"))
        self.pushButton_4.setText(_translate("MainWindow", "Términos y condiciones"))
        self.pushButton_5.setText(_translate("MainWindow", "Obetener ayuda"))
        self.pushButton_6.setText(_translate("MainWindow", "Cerrar sesión"))
import sourcecon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
