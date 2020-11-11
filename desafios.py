from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desafios(object):
    def setupUi(self, desafios):
        desafios.setObjectName("desafios")
        desafios.resize(380, 810)
        desafios.setAutoFillBackground(True)
        desafios.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"background-image: url(:/images/images/fondo amarillo patito.png);\n"
"}\n"
"\n"
"QFrame#jk1{\n"
"image: url(:/images/images/panel central.png);\n"
"border-radius:13px;\n"
"}\n"
"QPushButton#Atras{\n"
"background: transparent;\n"
"font-size:14px;\n"
"color:#494d49;\n"
"border-color: transparent;\n"
"}\n"
"QPushButton#Atras:hover{\n"
"background:transparent;\n"
"font-size:15px;\n"
"color:black;\n"
"border-color: transparent;\n"
"}\n"
"QLabel{\n"
"font-weight:bold;\n"
"color:black;\n"
"}\n"
"QLabel#titulo{\n"
"font-weight:bold;\n"
"color:black;\n"
"font-size:25px;\n"
"}\n"
"QLabel#descripcion{\n"
"color:black;\n"
"font-size:14px;\n"
"}\n"
"\n"
"QPushButton#ad{\n"
"background:#51C55D;\n"
"color:#494d49;\n"
"font-size:15px;\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#ad:hover{\n"
"background:#49b855;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:30px;\n"
"}\n"
"QPushButton{\n"
"background:transparent;\n"
"border-radius:12px;\n"
"border:1px solid;\n"
"}\n"
"QPushButton:hover{\n"
"background:transparent;\n"
"border-radius:12px;\n"
"border:3px solid;\n"
"}\n"
"QPushButton#uv_2{\n"
"background:transparent;\n"
"border-radius:13px;\n"
"border:1px solid;\n"
"}\n"
"QPushButton#uv_2:hover{\n"
"background:transparent;\n"
"border-radius:13px;\n"
"border:3px solid;\n"
"}\n"
"QFramer#hora{\n"
"image: url(:/images/images/hora.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(desafios)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.jk1 = QtWidgets.QFrame(self.centralwidget)
        self.jk1.setGeometry(QtCore.QRect(10, 170, 361, 471))
        self.jk1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.jk1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jk1.setObjectName("jk1")
        self.uv = QtWidgets.QPushButton(self.jk1)
        self.uv.setGeometry(QtCore.QRect(114, 106, 24, 24))
        self.uv.setText("")
        self.uv.setObjectName("uv")
        self.uv_2 = QtWidgets.QPushButton(self.jk1)
        self.uv_2.setGeometry(QtCore.QRect(76, 6, 26, 26))
        self.uv_2.setText("")
        self.uv_2.setObjectName("uv_2")
        self.uv_3 = QtWidgets.QPushButton(self.jk1)
        self.uv_3.setGeometry(QtCore.QRect(39, 86, 24, 24))
        self.uv_3.setText("")
        self.uv_3.setObjectName("uv_3")
        self.uv_4 = QtWidgets.QPushButton(self.jk1)
        self.uv_4.setGeometry(QtCore.QRect(283, 96, 24, 24))
        self.uv_4.setText("")
        self.uv_4.setObjectName("uv_4")
        self.uv_5 = QtWidgets.QPushButton(self.jk1)
        self.uv_5.setGeometry(QtCore.QRect(239, 17, 24, 24))
        self.uv_5.setText("")
        self.uv_5.setObjectName("uv_5")
        self.uv_7 = QtWidgets.QPushButton(self.jk1)
        self.uv_7.setGeometry(QtCore.QRect(63, 219, 24, 24))
        self.uv_7.setText("")
        self.uv_7.setObjectName("uv_7")
        self.uv_6 = QtWidgets.QPushButton(self.jk1)
        self.uv_6.setGeometry(QtCore.QRect(46, 317, 24, 24))
        self.uv_6.setText("")
        self.uv_6.setObjectName("uv_6")
        self.uv_9 = QtWidgets.QPushButton(self.jk1)
        self.uv_9.setGeometry(QtCore.QRect(274, 316, 24, 24))
        self.uv_9.setText("")
        self.uv_9.setObjectName("uv_9")
        self.uv_8 = QtWidgets.QPushButton(self.jk1)
        self.uv_8.setGeometry(QtCore.QRect(160, 298, 24, 24))
        self.uv_8.setText("")
        self.uv_8.setObjectName("uv_8")
        self.uv_10 = QtWidgets.QPushButton(self.jk1)
        self.uv_10.setGeometry(QtCore.QRect(114, 401, 24, 24))
        self.uv_10.setText("")
        self.uv_10.setObjectName("uv_10")
        self.uv_11 = QtWidgets.QPushButton(self.jk1)
        self.uv_11.setGeometry(QtCore.QRect(285, 413, 24, 24))
        self.uv_11.setText("")
        self.uv_11.setObjectName("uv_11")
        self.uv_12 = QtWidgets.QPushButton(self.jk1)
        self.uv_12.setGeometry(QtCore.QRect(259, 175, 24, 24))
        self.uv_12.setText("")
        self.uv_12.setObjectName("uv_12")
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setGeometry(QtCore.QRect(0, 40, 75, 23))
        self.Atras.setObjectName("Atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(130, 60, 111, 41))
        self.titulo.setObjectName("titulo")
        self.descripcion = QtWidgets.QLabel(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(35, 120, 311, 40))
        self.descripcion.setObjectName("descripcion")
        self.ad = QtWidgets.QPushButton(self.centralwidget)
        self.ad.setGeometry(QtCore.QRect(75, 690, 231, 61))
        self.ad.setObjectName("ad")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 380, 51))
        self.frame.setStyleSheet("image: url(:/images/images/hora con nuevas dimensiones.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        desafios.setCentralWidget(self.centralwidget)

        self.retranslateUi(desafios)
        QtCore.QMetaObject.connectSlotsByName(desafios)

    def retranslateUi(self, desafios):
        _translate = QtCore.QCoreApplication.translate
        desafios.setWindowTitle(_translate("desafios", "desafios"))
        self.Atras.setText(_translate("desafios", "← Atrás"))
        self.titulo.setText(_translate("desafios", "Desafíos"))
        self.descripcion.setText(_translate("desafios", "Cumple los retos y desarrolla nuevos hábitos"))
        self.ad.setText(_translate("desafios", "Guardar progreso"))
import source_des


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desafios = QtWidgets.QMainWindow()
    ui = Ui_desafios()
    ui.setupUi(desafios)
    desafios.show()
    sys.exit(app.exec_())
