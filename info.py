from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Informacion(object):
    def setupUi(self, Informacion):
        Informacion.setObjectName("Informacion")
        Informacion.resize(380, 812)
        self.centralwidget = QtWidgets.QWidget(Informacion)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setItalic(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"    \n"
"font-family:century gothic;\n"
"}\n"
"QWidget{\n"
"\n"
"    background-image: url(:/newPrefix/Imagenes/fondo.jpeg);\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"QLabel#salud {\n"
"font-size:24px;\n"
"font-weight:bold; \n"
" \n"
"}\n"
"QLabel#texto {\n"
"align:center;\n"
"\n"
" \n"
"}\n"
"QPushButton{\n"
"background :#51C55D;\n"
"border-radius: 15px;\n"
"}    \n"
"QPushButton:hover{\n"
"background :#3bb547;\n"
"border-radius: 15px;\n"
"font-weight:bold;\n"
"}    \n"
"QLabel#bateria{\n"
"image: url(:/newPrefix/Imagenes/Vector (4).png);\n"
"}\n"
"QLabel#senial{\n"
"    image: url(:/newPrefix/Imagenes/Vector (2).png);\n"
"}\n"
"QLabel#hora{\n"
"    image: url(:/newPrefix/Imagenes/Vector (1).png);\n"
"}\n"
"QLabel#wifi{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Vector (3).png);\n"
"}\n"
"QLabel#contorno{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Border.png);\n"
"}\n"
"QLabel#boton{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Vector (5).png);\n"
"}\n"
"QLabel#boton2{\n"
"    image: url(:/newPrefix/Imagenes/Vector (6).png);\n"
"}\n"
"QLabel#flecha{\n"
"    image: url(:/newPrefix/Imagenes/shape.png);\n"
"}\n"
"QLabel#bateria{\n"
"\n"
"image:    url(:/newPrefix/Imagenes/Captura.PNG);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 550, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.gato = QtWidgets.QLabel(self.centralwidget)
        self.gato.setGeometry(QtCore.QRect(90, 230, 211, 171))
        self.gato.setStyleSheet("image: url(:/newPrefix/Imagenes/undraw_Playful_cat_rchv 1.png)")
        self.gato.setText("")
        self.gato.setObjectName("gato")
        self.texto = QtWidgets.QLabel(self.centralwidget)
        self.texto.setGeometry(QtCore.QRect(50, 420, 291, 91))
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.setObjectName("texto")
        self.salud = QtWidgets.QLabel(self.centralwidget)
        self.salud.setGeometry(QtCore.QRect(120, 160, 161, 41))
        self.salud.setObjectName("salud")
        self.wifi = QtWidgets.QLabel(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(280, 50, 21, 16))
        self.wifi.setText("")
        self.wifi.setObjectName("wifi")
        self.senial = QtWidgets.QLabel(self.centralwidget)
        self.senial.setGeometry(QtCore.QRect(230, 50, 31, 16))
        self.senial.setText("")
        self.senial.setObjectName("senial")
        self.hora = QtWidgets.QLabel(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(30, 50, 55, 16))
        self.hora.setText("")
        self.hora.setObjectName("hora")
        self.boton = QtWidgets.QLabel(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(200, 630, 21, 16))
        self.boton.setText("")
        self.boton.setObjectName("boton")
        self.boton2 = QtWidgets.QLabel(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(170, 630, 16, 16))
        self.boton2.setText("")
        self.boton2.setObjectName("boton2")
        self.flecha = QtWidgets.QLabel(self.centralwidget)
        self.flecha.setGeometry(QtCore.QRect(20, 100, 55, 16))
        self.flecha.setText("")
        self.flecha.setObjectName("flecha")
        self.bateria = QtWidgets.QLabel(self.centralwidget)
        self.bateria.setGeometry(QtCore.QRect(310, 50, 55, 16))
        self.bateria.setText("")
        self.bateria.setObjectName("bateria")
        Informacion.setCentralWidget(self.centralwidget)

        self.retranslateUi(Informacion)
        QtCore.QMetaObject.connectSlotsByName(Informacion)

    def retranslateUi(self, Informacion):
        _translate = QtCore.QCoreApplication.translate
        Informacion.setWindowTitle(_translate("Informacion", "Informacion"))
        self.pushButton.setText(_translate("Informacion", "Más Información"))
        self.texto.setText(_translate("Informacion", "Recuerda que tu salud mental\n"
" es tan importante como tu salud física.\n"
"Si quisieras saber más , presiona el botón."))
        self.salud.setText(_translate("Informacion", "Salud Mental"))
import source50


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Informacion = QtWidgets.QMainWindow()
    ui = Ui_Informacion()
    ui.setupUi(Informacion)
    Informacion.show()
    sys.exit(app.exec_())
