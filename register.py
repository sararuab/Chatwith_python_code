#Pantalla de registro de usuario

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QMessageBox, QLabel, QPushButton, QLineEdit, QSpinBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import mysql.connector as mc
import mysql.connector


class Ui_Register(object):
    def setupUi(self,Register):
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
        self.rectangulo.setGeometry(QtCore.QRect(50, 250, 281, 41))
        self.rectangulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo.setObjectName("rectangulo")
        self.nombre = QtWidgets.QLineEdit(self.rectangulo)
        self.nombre.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.nombre.setMaxLength(20)
        self.nombre.setObjectName("nombre")
        self.rectangulo_2 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_2.setGeometry(QtCore.QRect(50, 310, 281, 41))
        self.rectangulo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_2.setObjectName("rectangulo_2")
        self.correo = QtWidgets.QLineEdit(self.rectangulo_2)
        self.correo.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.correo.setMaxLength(50)
        self.correo.setObjectName("correo")
        self.rectangulo_3 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_3.setGeometry(QtCore.QRect(50, 370, 281, 41))
        self.rectangulo_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_3.setObjectName("rectangulo_3")
        self.contrasena = QtWidgets.QLineEdit(self.rectangulo_3)
        self.contrasena.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.contrasena.setMaxLength(18)
        self.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasena.setObjectName("contrasena")
        self.icon = QtWidgets.QToolButton(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(140, 30, 111, 111))
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logotipo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(111, 111))
        self.icon.setAutoExclusive(False)
        self.icon.setObjectName("icon")
        self.create = QtWidgets.QLabel(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(100, 170, 181, 21))
        self.create.setObjectName("create")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 520, 279, 50))
        self.pushButton.setObjectName("pushButton")
        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        self.pushButton.clicked.connect(self.insert_data)

    def insert_data(self):
        conexion1=mysql.connector.connect(host="localhost", 
                                            user="root", 
                                            passwd="", 
                                            database="usuarios")
        cursor1=conexion1.cursor()
        sql="insert into registro(nombre, correo, password) values (%s,%s,%s)"
        datos=(self.nombre.text(),self.correo.text(),self.contrasena.text())
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
import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
