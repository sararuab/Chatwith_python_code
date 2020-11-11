from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Diario_1(object):
    def setupUi(self, Diario_1):
        Diario_1.setObjectName("Diario_1")
        Diario_1.resize(380, 812)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        Diario_1.setFont(font)
        Diario_1.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/images/images/fondo.png);\n"
"}\n"
"QFrame#Escribe{\n"
"background: #EDCAC5;\n"
"border-radius: 15px;\n"
"}\n"
"QToolButton#guardar{\n"
"background: #51C55D;\n"
"border-radius: 15px;\n"
"}\n"
"QFrame#graba{\n"
"background: #EFE9B0;\n"
"border-radius: 15px;\n"
"}\n"
"QToolButton#voz{\n"
"background: #EFE9B0;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit#Escribediario{\n"
"background: #EFC8C2;\n"
"border:  #EFC8C2;\n"
"}\n"
"QTextBrowser#Diario_2{\n"
"background: #FFFEEA;\n"
"border:  #FFFEEA;\n"
"}\n"
"QToolButton#anotaciones{\n"
"background: #DED482;\n"
"border-radius: 15px;\n"
"}\n"
"QLabel#graba_2{\n"
"color: black;\n"
"background: #EFE9B0;\n"
"}\n"
"QToolButton#atras{\n"
"background: #FFFEEA;\n"
"border-radius: 15px;\n"
"}\n"
"QFrame#wifi{\n"
"background: #FFFEEA;\n"
"border-radius: 15px;\n"
"image: url(:/images/images/hora.png);\n"
"}")
        Diario_1.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(Diario_1)
        self.centralwidget.setObjectName("centralwidget")
        self.Escribe = QtWidgets.QFrame(self.centralwidget)
        self.Escribe.setGeometry(QtCore.QRect(20, 240, 331, 301))
        self.Escribe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Escribe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Escribe.setObjectName("Escribe")
        self.Escribediario = QtWidgets.QPlainTextEdit(self.Escribe)
        self.Escribediario.setGeometry(QtCore.QRect(30, 20, 281, 261))
        self.Escribediario.setObjectName("Escribediario")
        self.guardar = QtWidgets.QToolButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(100, 670, 181, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.guardar.setFont(font)
        self.guardar.setObjectName("guardar")
        self.graba = QtWidgets.QFrame(self.centralwidget)
        self.graba.setGeometry(QtCore.QRect(30, 560, 311, 61))
        self.graba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graba.setObjectName("graba")
        self.voz = QtWidgets.QToolButton(self.graba)
        self.voz.setGeometry(QtCore.QRect(260, 20, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/voz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voz.setIcon(icon)
        self.voz.setIconSize(QtCore.QSize(35, 35))
        self.voz.setObjectName("voz")
        self.graba_2 = QtWidgets.QLabel(self.graba)
        self.graba_2.setGeometry(QtCore.QRect(30, 20, 51, 16))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graba_2.setFont(font)
        self.graba_2.setObjectName("graba_2")
        self.Diario_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Diario_2.setGeometry(QtCore.QRect(10, 100, 321, 121))
        self.Diario_2.setObjectName("Diario_2")
        self.anotaciones = QtWidgets.QToolButton(self.centralwidget)
        self.anotaciones.setGeometry(QtCore.QRect(130, 750, 110, 31))
        self.anotaciones.setObjectName("anotaciones")
        self.atras = QtWidgets.QToolButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(10, 50, 61, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/atrás.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atras.setIcon(icon1)
        self.atras.setIconSize(QtCore.QSize(80, 80))
        self.atras.setObjectName("atras")
        self.wifi = QtWidgets.QFrame(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.wifi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wifi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wifi.setObjectName("wifi")
        Diario_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Diario_1)
        QtCore.QMetaObject.connectSlotsByName(Diario_1)

    def retranslateUi(self, Diario_1):
        _translate = QtCore.QCoreApplication.translate
        Diario_1.setWindowTitle(_translate("Diario_1", "Diario"))
        self.Escribediario.setPlainText(_translate("Diario_1", "Escribe"))
        self.guardar.setText(_translate("Diario_1", "Guardar"))
        self.voz.setText(_translate("Diario_1", "..."))
        self.graba_2.setText(_translate("Diario_1", "Graba"))
        self.Diario_2.setHtml(_translate("Diario_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt; font-weight:600;\">Diario</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Plasma tus emociones</span></p></body></html>"))
        self.anotaciones.setText(_translate("Diario_1", "Ver anotaciones"))
        self.atras.setText(_translate("Diario_1", "..."))
import source5


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Diario_1 = QtWidgets.QMainWindow()
    ui = Ui_Diario_1()
    ui.setupUi(Diario_1)
    Diario_1.show()
    sys.exit(app.exec_())
