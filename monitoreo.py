from PyQt5 import QtCore, QtGui, QtWidgets


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
import source5


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitoreo = QtWidgets.QMainWindow()
    ui = Ui_Monitoreo()
    ui.setupUi(Monitoreo)
    Monitoreo.show()
    sys.exit(app.exec_())
