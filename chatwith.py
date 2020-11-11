from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from ui_register import source
import mysql.connector as mc
import mysql.connector
from ui_Perfil import saravic
from DIariofinal import source5
from ui_monitoreo5 import source5
from desafios import source_des
from ui_informacion5 import source50
from ui_principal5 import sourcep


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


class Ui_Monitoreo(object):
    def setupUi(self, Monitoreo):
        Monitoreo.setObjectName("Monitoreo")
        Monitoreo.resize(380, 812)
        Monitoreo.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/images/images/fdeca2.png);\n"
"}\n"
"\n"
"QFrame#cont1{\n"
"background: #ffffff;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame#cont2{\n"
"background: #ffffff;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame#cont3{\n"
"background: #ffffff;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame#cont4{\n"
"background: #ffffff;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QToolButton#icono1{\n"
"background: transparent;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame#mes1{\n"
"background: #3F414E;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QFrame#mes2{\n"
"background: #3F414E;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel#monitoreo{\n"
"color: black;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QLabel#indicacion{\n"
"color: black;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QLabel#octubre{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QLabel#noviembre{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: transparent;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: transparent;\n"
"border-radius:10px;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"QToolButton#mes_1{\n"
"background:#3F414E;\n"
"border-radius:10px;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QToolButton#mes_2{\n"
"background:#3F414E;\n"
"border-radius:10px;\n"
"color: white;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QToolButton#reporte_1{\n"
"background:#ebdddd;\n"
"border-radius: 8px;\n"
"color: black;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QToolButton#reporte_2{\n"
"background:#ebdddd;\n"
"border-radius: 8px;\n"
"color: black;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QToolButton#reporte_3{\n"
"background:#ebdddd;\n"
"border-radius: 8px;\n"
"color: black;\n"
"font-size: 10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background: transparent;\n"
"color: black;\n"
"font-size: 9px;\n"
"}\n"
"\n"
"QToolButton#resumen{\n"
"background:#cfe6e0;\n"
"border-radius: 8px;\n"
"color: black;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"QFrame#hora{\n"
"image:url(:/images/images/hora sara.png);\n"
"}\n"
"\n"
"QPushButton#atras{\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Monitoreo)
        self.centralwidget.setObjectName("centralwidget")
        self.cont1 = QtWidgets.QFrame(self.centralwidget)
        self.cont1.setGeometry(QtCore.QRect(85, 230, 231, 91))
        self.cont1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont1.setObjectName("cont1")
        self.repor_1 = QtWidgets.QPushButton(self.cont1)
        self.repor_1.setGeometry(QtCore.QRect(40, 35, 75, 41))
        self.repor_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/cuesto.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repor_1.setIcon(icon)
        self.repor_1.setIconSize(QtCore.QSize(60, 60))
        self.repor_1.setObjectName("repor_1")
        self.pira_1 = QtWidgets.QPushButton(self.cont1)
        self.pira_1.setGeometry(QtCore.QRect(140, 30, 61, 51))
        self.pira_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/pira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pira_1.setIcon(icon1)
        self.pira_1.setIconSize(QtCore.QSize(35, 35))
        self.pira_1.setObjectName("pira_1")
        self.reporte_1 = QtWidgets.QToolButton(self.cont1)
        self.reporte_1.setGeometry(QtCore.QRect(5, 5, 61, 16))
        self.reporte_1.setObjectName("reporte_1")
        self.label = QtWidgets.QLabel(self.cont1)
        self.label.setGeometry(QtCore.QRect(55, 25, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.cont1)
        self.label_2.setGeometry(QtCore.QRect(155, 25, 47, 13))
        self.label_2.setObjectName("label_2")
        self.cont2 = QtWidgets.QFrame(self.centralwidget)
        self.cont2.setGeometry(QtCore.QRect(85, 380, 231, 91))
        self.cont2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont2.setObjectName("cont2")
        self.repor_2 = QtWidgets.QPushButton(self.cont2)
        self.repor_2.setGeometry(QtCore.QRect(40, 35, 75, 41))
        self.repor_2.setText("")
        self.repor_2.setIcon(icon)
        self.repor_2.setIconSize(QtCore.QSize(60, 60))
        self.repor_2.setObjectName("repor_2")
        self.pira_2 = QtWidgets.QPushButton(self.cont2)
        self.pira_2.setGeometry(QtCore.QRect(140, 30, 61, 51))
        self.pira_2.setText("")
        self.pira_2.setIcon(icon1)
        self.pira_2.setIconSize(QtCore.QSize(35, 35))
        self.pira_2.setObjectName("pira_2")
        self.reporte_2 = QtWidgets.QToolButton(self.cont2)
        self.reporte_2.setGeometry(QtCore.QRect(5, 5, 61, 16))
        self.reporte_2.setObjectName("reporte_2")
        self.label_5 = QtWidgets.QLabel(self.cont2)
        self.label_5.setGeometry(QtCore.QRect(55, 25, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.cont2)
        self.label_6.setGeometry(QtCore.QRect(155, 25, 47, 13))
        self.label_6.setObjectName("label_6")
        self.cont3 = QtWidgets.QFrame(self.centralwidget)
        self.cont3.setGeometry(QtCore.QRect(85, 490, 231, 91))
        self.cont3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont3.setObjectName("cont3")
        self.repor_3 = QtWidgets.QPushButton(self.cont3)
        self.repor_3.setGeometry(QtCore.QRect(40, 35, 75, 41))
        self.repor_3.setText("")
        self.repor_3.setIcon(icon)
        self.repor_3.setIconSize(QtCore.QSize(60, 60))
        self.repor_3.setObjectName("repor_3")
        self.pira_3 = QtWidgets.QPushButton(self.cont3)
        self.pira_3.setGeometry(QtCore.QRect(140, 30, 61, 51))
        self.pira_3.setText("")
        self.pira_3.setIcon(icon1)
        self.pira_3.setIconSize(QtCore.QSize(35, 35))
        self.pira_3.setObjectName("pira_3")
        self.reporte_3 = QtWidgets.QToolButton(self.cont3)
        self.reporte_3.setGeometry(QtCore.QRect(5, 5, 61, 16))
        self.reporte_3.setObjectName("reporte_3")
        self.label_3 = QtWidgets.QLabel(self.cont3)
        self.label_3.setGeometry(QtCore.QRect(55, 25, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.cont3)
        self.label_4.setGeometry(QtCore.QRect(155, 25, 47, 13))
        self.label_4.setObjectName("label_4")
        self.monitoreo = QtWidgets.QLabel(self.centralwidget)
        self.monitoreo.setGeometry(QtCore.QRect(115, 90, 181, 21))
        self.monitoreo.setObjectName("monitoreo")
        self.indicacion = QtWidgets.QLabel(self.centralwidget)
        self.indicacion.setGeometry(QtCore.QRect(75, 130, 271, 21))
        self.indicacion.setObjectName("indicacion")
        self.cont4 = QtWidgets.QFrame(self.centralwidget)
        self.cont4.setGeometry(QtCore.QRect(66, 680, 271, 91))
        self.cont4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cont4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cont4.setObjectName("cont4")
        self.resu_1 = QtWidgets.QPushButton(self.cont4)
        self.resu_1.setGeometry(QtCore.QRect(40, 15, 101, 61))
        self.resu_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/barras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resu_1.setIcon(icon2)
        self.resu_1.setIconSize(QtCore.QSize(100, 100))
        self.resu_1.setObjectName("resu_1")
        self.resu_2 = QtWidgets.QPushButton(self.cont4)
        self.resu_2.setGeometry(QtCore.QRect(160, 20, 81, 51))
        self.resu_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/torta.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resu_2.setIcon(icon3)
        self.resu_2.setIconSize(QtCore.QSize(80, 80))
        self.resu_2.setObjectName("resu_2")
        self.mes_1 = QtWidgets.QToolButton(self.centralwidget)
        self.mes_1.setGeometry(QtCore.QRect(85, 195, 71, 21))
        self.mes_1.setObjectName("mes_1")
        self.mes_2 = QtWidgets.QToolButton(self.centralwidget)
        self.mes_2.setGeometry(QtCore.QRect(85, 345, 71, 21))
        self.mes_2.setObjectName("mes_2")
        self.resumen = QtWidgets.QToolButton(self.centralwidget)
        self.resumen.setGeometry(QtCore.QRect(125, 650, 161, 20))
        self.resumen.setObjectName("resumen")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 590, 21, 17))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 610, 21, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.hora = QtWidgets.QFrame(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(10, 0, 351, 41))
        self.hora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hora.setObjectName("hora")
        self.atras = QtWidgets.QPushButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(0, 40, 71, 16))
        self.atras.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/atrás sara.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atras.setIcon(icon4)
        self.atras.setIconSize(QtCore.QSize(80, 80))
        self.atras.setObjectName("atras")
        Monitoreo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Monitoreo)
        QtCore.QMetaObject.connectSlotsByName(Monitoreo)

    def retranslateUi(self, Monitoreo):
        _translate = QtCore.QCoreApplication.translate
        Monitoreo.setWindowTitle(_translate("Monitoreo", "Monitoreo"))
        self.reporte_1.setText(_translate("Monitoreo", "Reporte1"))
        self.label.setText(_translate("Monitoreo", "Depresion"))
        self.label_2.setText(_translate("Monitoreo", "Ansiedad"))
        self.reporte_2.setText(_translate("Monitoreo", "Reporte2"))
        self.label_5.setText(_translate("Monitoreo", "Depresion"))
        self.label_6.setText(_translate("Monitoreo", "Ansiedad"))
        self.reporte_3.setText(_translate("Monitoreo", "Reporte3"))
        self.label_3.setText(_translate("Monitoreo", "Depresion"))
        self.label_4.setText(_translate("Monitoreo", "Ansiedad"))
        self.monitoreo.setText(_translate("Monitoreo", "Mi Monitoreo"))
        self.indicacion.setText(_translate("Monitoreo", "Aqui encontraras todos los cuestionarios que respondiste"))
        self.mes_1.setText(_translate("Monitoreo", "Octubre"))
        self.mes_2.setText(_translate("Monitoreo", "Noviembre"))
        self.resumen.setText(_translate("Monitoreo", "Resumen de cuestionarios"))


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


class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(380, 812)
        Inicio.setStyleSheet("*{\n"
"font-family century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image:url(:/imagenes/imagenes/29 (1).png);\n"
"}\n"
"QLabel{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#mascota{\n"
"background-image: url(:/imagenes/imagenes/fox 1.png);\n"
"border-radius: 35px;\n"
"}\n"
"QPushButton#salvavidas{\n"
"background: transparent;\n"
"background-image:url(:/imagenes/imagenes/WhatsApp Image 2020-10-14 at 2.00 1.png);\n"
"border-radius: 25px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.inicio = QtWidgets.QLabel(self.centralwidget)
        self.inicio.setGeometry(QtCore.QRect(50, 160, 41, 41))
        self.inicio.setObjectName("inicio")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 240, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 280, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 320, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 360, 61, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 400, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 440, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 101, 41))
        self.label.setObjectName("label")
        self.mascota = QtWidgets.QPushButton(self.centralwidget)
        self.mascota.setGeometry(QtCore.QRect(30, 60, 71, 71))
        self.mascota.setText("")
        self.mascota.setObjectName("mascota")
        self.salvavidas = QtWidgets.QPushButton(self.centralwidget)
        self.salvavidas.setGeometry(QtCore.QRect(40, 480, 50, 50))
        self.salvavidas.setText("")
        self.salvavidas.setObjectName("salvavidas")
        Inicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

        self.pushButton.clicked.connect(self.perfil)
        self.pushButton_3.clicked.connect(self.diario)
        self.pushButton_4.clicked.connect(self.monitor)
        self.pushButton_5.clicked.connect(self.desafio)
        self.pushButton_6.clicked.connect(self.info)
        self.pushButton_7.clicked.connect(self.confi)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Inicio"))
        self.inicio.setText(_translate("Inicio", "Inicio"))
        self.pushButton.setText(_translate("Inicio", "Perfil"))
        self.pushButton_2.setText(_translate("Inicio", "Chats"))
        self.pushButton_3.setText(_translate("Inicio", "Diario"))
        self.pushButton_4.setText(_translate("Inicio", "Monitoreo"))
        self.pushButton_5.setText(_translate("Inicio", "Desafios"))
        self.pushButton_6.setText(_translate("Inicio", "Más información"))
        self.pushButton_7.setText(_translate("Inicio", "Configuración"))
        self.label.setText(_translate("Inicio", "Alvaro Sevilla"))

    def perfil(self):
        self.Perfil = QtWidgets.QMainWindow()
        self.ui = Ui_Perfil()
        self.ui.setupUi(self.Perfil)
        self.Perfil.show()

    def diario(self):
        self.Diario_1 = QtWidgets.QMainWindow()
        self.ui = Ui_Diario_1()
        self.ui.setupUi(self.Diario_1)
        self.Diario_1.show()

    def monitor(self):
        self.Monitoreo = QtWidgets.QMainWindow()
        self.ui = Ui_Monitoreo()
        self.ui.setupUi(self.Monitoreo)
        self.Monitoreo.show()

    def desafio(self):
        self.desafios = QtWidgets.QMainWindow()
        self.ui = Ui_desafios()
        self.ui.setupUi(self.desafios)
        self.desafios.show()

    def info(self):
        self.Informacion = QtWidgets.QMainWindow()
        self.ui = Ui_Informacion()
        self.ui.setupUi(self.Informacion)
        self.Informacion.show()

    def confi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(380, 812)
        Register.setStyleSheet("*{\n"
                               "font-family: century gothic;\n"
                               "}\n"
                               "\n"
                               "QWidget{\n"
                               "background-image: url(:/images/images/background.png);\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo_2{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo_3{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QToolButton#icon{\n"
                               "background:#FDECA2;\n"
                               "border-radius:0px;\n"
                               "}\n"
                               "\n"
                               "QLabel{\n"
                               "font-weight:bold;\n"
                               "color:Black;\n"
                               "}\n"
                               "\n"
                               "QLabel#create{\n"
                               "font-size:18px;\n"
                               "}\n"
                               "\n"
                               "QLineEdit{\n"
                               "background:transparent;\n"
                               "border:none;\n"
                               "}\n"
                               "\n"
                               "QPushButton{\n"
                               "background:#51C55D;\n"
                               "color:white;\n"
                               "border-radius:16px;\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover{\n"
                               "background:#40A04A;\n"
                               "color:white;\n"
                               "border-radius:16px;\n"
                               "font-weight:bold;\n"
                               "}")
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.rectangulo = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo.setGeometry(QtCore.QRect(50, 340, 281, 41))
        self.rectangulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo.setObjectName("rectangulo")
        self.nombre = QtWidgets.QLineEdit(self.rectangulo)
        self.nombre.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.nombre.setMaxLength(20)
        self.nombre.setObjectName("nombre")
        self.rectangulo_2 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_2.setGeometry(QtCore.QRect(50, 400, 281, 41))
        self.rectangulo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_2.setObjectName("rectangulo_2")
        self.correo = QtWidgets.QLineEdit(self.rectangulo_2)
        self.correo.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.correo.setMaxLength(50)
        self.correo.setObjectName("correo")
        self.rectangulo_3 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_3.setGeometry(QtCore.QRect(50, 460, 281, 41))
        self.rectangulo_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_3.setObjectName("rectangulo_3")
        self.contrasena = QtWidgets.QLineEdit(self.rectangulo_3)
        self.contrasena.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.contrasena.setMaxLength(18)
        self.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasena.setObjectName("contrasena")
        self.icon = QtWidgets.QToolButton(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(140, 90, 111, 111))
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logotipo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(111, 111))
        self.icon.setAutoExclusive(False)
        self.icon.setObjectName("icon")
        self.create = QtWidgets.QLabel(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(100, 250, 181, 21))
        self.create.setObjectName("create")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 630, 279, 50))
        self.pushButton.setObjectName("pushButton")
        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        self.pushButton.clicked.connect(self.insert_data)
        self.pushButton.clicked.connect(self.principal)

    def insert_data(self):
        conexion1 = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="",
                                            database="usuarios")
        cursor1 = conexion1.cursor()
        sql = "insert into registro(nombre, correo, password) values (%s,%s,%s)"
        datos = (self.nombre.text(), self.correo.text(), self.contrasena.text())
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.nombre.setPlaceholderText(_translate("Register", "Nombre"))
        self.correo.setPlaceholderText(_translate("Register", "Correo"))
        self.contrasena.setPlaceholderText(_translate("Register", "Contraseña"))
        self.create.setText(_translate("Register", "Créate una cuenta"))
        self.pushButton.setText(_translate("Register", "Regístrate"))

    def principal(self):
        self.Inicio = QtWidgets.QMainWindow()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self.Inicio)
        self.Inicio.show()


class Ui_Chatbot(object):
    def setupUi(self, Chatbot):
        Chatbot.setObjectName("Chatbot")
        Chatbot.resize(380, 812)
        Chatbot.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/imagesini/imagesini/background.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#51C55D;\n"
"color:white;\n"
"border-radius:16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#40A04A;\n"
"color:white;\n"
"border-radius:16px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton#ingresa{\n"
"background:#FDECA2;\n"
"color:black;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Chatbot)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QToolButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(100, 170, 181, 191))
        self.logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagesini/imagesini/logotipo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QtCore.QSize(200, 220))
        self.logo.setObjectName("logo")
        self.descubre = QtWidgets.QPushButton(self.centralwidget)
        self.descubre.setGeometry(QtCore.QRect(50, 630, 279, 50))
        self.descubre.setObjectName("descubre")
        self.quest = QtWidgets.QLabel(self.centralwidget)
        self.quest.setGeometry(QtCore.QRect(80, 720, 161, 21))
        self.quest.setObjectName("quest")
        self.ingresa = QtWidgets.QPushButton(self.centralwidget)
        self.ingresa.setGeometry(QtCore.QRect(240, 720, 61, 21))
        self.ingresa.setObjectName("ingresa")
        Chatbot.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chatbot)
        QtCore.QMetaObject.connectSlotsByName(Chatbot)
        self.descubre.clicked.connect(self.registersc)



    def retranslateUi(self, Chatbot):
        _translate = QtCore.QCoreApplication.translate
        Chatbot.setWindowTitle(_translate("Chatbot", "Chatbot"))
        self.descubre.setText(_translate("Chatbot", "Descubre chatwith"))
        self.quest.setText(_translate("Chatbot", "¿Ya tienes una cuenta?"))
        self.ingresa.setText(_translate("Chatbot", "Ingresa"))


    def registersc(self):
        self.Register = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.Register)
        self.Register.show()


import sourceini

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Chatbot = QtWidgets.QMainWindow()
    ui = Ui_Chatbot()
    ui.setupUi(Chatbot)
    Chatbot.show()
    sys.exit(app.exec_())
