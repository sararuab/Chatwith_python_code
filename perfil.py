from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Perfil(object):
    def setupUi(self, Perfil):
        Perfil.setObjectName("Perfil")
        Perfil.resize(380, 812)
        Perfil.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"QWidget{\n"
"background-image: url(:/images/images/fondofinal.png);\n"
"}\n"
"QToolButton{\n"
"background: transparent;\n"
"}\n"
"\n"
"QFrame#zorrito{\n"
"background: transparent;\n"
"    image: url(:/images/images/zorro.png);\n"
"}\n"
"QFrame#nivel{\n"
"background: transparent;\n"
"    image: url(:/images/images/nivel sin fondo.png);\n"
"}\n"
"QFrame#contenedor{\n"
"border-radius:15px;\n"
"background: #FACEBB;\n"
"}\n"
"QLabel#nombre{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"}\n"
"QLabel{\n"
"background: transparent;\n"
"font-size: 14px;\n"
"}\n"
"QFrame#one{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#two{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#three{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#four{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#five{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#six{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Perfil)
        self.centralwidget.setObjectName("centralwidget")
        self.zorrito = QtWidgets.QFrame(self.centralwidget)
        self.zorrito.setGeometry(QtCore.QRect(110, 110, 151, 141))
        self.zorrito.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.zorrito.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zorrito.setObjectName("zorrito")
        self.nivel = QtWidgets.QFrame(self.centralwidget)
        self.nivel.setGeometry(QtCore.QRect(240, 60, 131, 91))
        self.nivel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nivel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nivel.setObjectName("nivel")
        self.contenedor = QtWidgets.QFrame(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(40, 310, 311, 441))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.uno = QtWidgets.QLabel(self.contenedor)
        self.uno.setGeometry(QtCore.QRect(60, 30, 171, 31))
        self.uno.setObjectName("uno")
        self.dos = QtWidgets.QLabel(self.contenedor)
        self.dos.setGeometry(QtCore.QRect(60, 100, 191, 21))
        self.dos.setObjectName("dos")
        self.tres = QtWidgets.QLabel(self.contenedor)
        self.tres.setGeometry(QtCore.QRect(60, 120, 111, 31))
        self.tres.setObjectName("tres")
        self.cuatro = QtWidgets.QLabel(self.contenedor)
        self.cuatro.setGeometry(QtCore.QRect(60, 170, 171, 31))
        self.cuatro.setObjectName("cuatro")
        self.cinco = QtWidgets.QLabel(self.contenedor)
        self.cinco.setGeometry(QtCore.QRect(60, 200, 61, 16))
        self.cinco.setObjectName("cinco")
        self.seis = QtWidgets.QLabel(self.contenedor)
        self.seis.setGeometry(QtCore.QRect(60, 250, 211, 21))
        self.seis.setObjectName("seis")
        self.siete = QtWidgets.QLabel(self.contenedor)
        self.siete.setGeometry(QtCore.QRect(60, 310, 241, 21))
        self.siete.setObjectName("siete")
        self.ocho = QtWidgets.QLabel(self.contenedor)
        self.ocho.setGeometry(QtCore.QRect(60, 330, 71, 21))
        self.ocho.setObjectName("ocho")
        self.label = QtWidgets.QLabel(self.contenedor)
        self.label.setGeometry(QtCore.QRect(60, 380, 191, 31))
        self.label.setObjectName("label")
        self.one = QtWidgets.QFrame(self.contenedor)
        self.one.setGeometry(QtCore.QRect(10, 40, 31, 21))
        self.one.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.one.setFrameShadow(QtWidgets.QFrame.Raised)
        self.one.setObjectName("one")
        self.two = QtWidgets.QFrame(self.contenedor)
        self.two.setGeometry(QtCore.QRect(10, 100, 31, 21))
        self.two.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.two.setFrameShadow(QtWidgets.QFrame.Raised)
        self.two.setObjectName("two")
        self.three = QtWidgets.QFrame(self.contenedor)
        self.three.setGeometry(QtCore.QRect(10, 180, 31, 21))
        self.three.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.three.setFrameShadow(QtWidgets.QFrame.Raised)
        self.three.setObjectName("three")
        self.four = QtWidgets.QFrame(self.contenedor)
        self.four.setGeometry(QtCore.QRect(10, 250, 31, 21))
        self.four.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.four.setFrameShadow(QtWidgets.QFrame.Raised)
        self.four.setObjectName("four")
        self.five = QtWidgets.QFrame(self.contenedor)
        self.five.setGeometry(QtCore.QRect(10, 310, 31, 21))
        self.five.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.five.setFrameShadow(QtWidgets.QFrame.Raised)
        self.five.setObjectName("five")
        self.six = QtWidgets.QFrame(self.contenedor)
        self.six.setGeometry(QtCore.QRect(10, 390, 31, 21))
        self.six.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.six.setFrameShadow(QtWidgets.QFrame.Raised)
        self.six.setObjectName("six")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(130, 260, 131, 21))
        self.nombre.setObjectName("nombre")
        self.atras = QtWidgets.QToolButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(10, 50, 71, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/atras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atras.setIcon(icon)
        self.atras.setIconSize(QtCore.QSize(80, 80))
        self.atras.setObjectName("atras")
        Perfil.setCentralWidget(self.centralwidget)

        self.retranslateUi(Perfil)
        QtCore.QMetaObject.connectSlotsByName(Perfil)

    def retranslateUi(self, Perfil):
        _translate = QtCore.QCoreApplication.translate
        Perfil.setWindowTitle(_translate("Perfil", "Perfil"))
        self.uno.setText(_translate("Perfil", "Horas activas: 64 horas"))
        self.dos.setText(_translate("Perfil", "N° mascotas de mascotas "))
        self.tres.setText(_translate("Perfil", "desbloquedas : 1l"))
        self.cuatro.setText(_translate("Perfil", "Temática más recurrente: "))
        self.cinco.setText(_translate("Perfil", "Música"))
        self.seis.setText(_translate("Perfil", "Puntaje obtenido: 120 puntos"))
        self.siete.setText(_translate("Perfil", "Frecuencia de uso de la mascota:"))
        self.ocho.setText(_translate("Perfil", " regular"))
        self.label.setText(_translate("Perfil", "N° de trofeos obtenidos: 1"))
        self.nombre.setText(_translate("Perfil", "Alvaro Sevilla"))
        self.atras.setText(_translate("Perfil", "..."))

import saravic

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Perfil = QtWidgets.QMainWindow()
    ui = Ui_Perfil()s
    ui.setupUi(Perfil)
    Perfil.show()
    sys.exit(app.exec_())
