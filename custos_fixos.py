# Form implementation generated from reading ui file 'v4.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_estoque(object):
    def setupUi(self, MainWindow_estoque):
        MainWindow_estoque.setObjectName("MainWindow_estoque")
        MainWindow_estoque.resize(580, 360)
        MainWindow_estoque.setMinimumSize(QtCore.QSize(570, 355))
        MainWindow_estoque.setMaximumSize(QtCore.QSize(580, 360))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_estoque)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-1, 50, 581, 311))
        self.frame_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(6, -1, 6, 6)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_35 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_35.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_35.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_35)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_form_salvar = QtWidgets.QPushButton(parent=self.frame_35)
        self.pushButton_form_salvar.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_form_salvar.setFont(font)
        self.pushButton_form_salvar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_form_salvar.setObjectName("pushButton_form_salvar")
        self.horizontalLayout_8.addWidget(self.pushButton_form_salvar)
        self.verticalLayout_3.addWidget(self.frame_35)
        self.frame_19 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_19.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_form_produto = QtWidgets.QLineEdit(parent=self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_produto.setFont(font)
        self.lineEdit_form_produto.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_produto.setObjectName("lineEdit_form_produto")
        self.gridLayout_6.addWidget(self.lineEdit_form_produto, 1, 1, 1, 1)
        self.lineEdit_form_ecomerce = QtWidgets.QLineEdit(parent=self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_ecomerce.setFont(font)
        self.lineEdit_form_ecomerce.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_ecomerce.setObjectName("lineEdit_form_ecomerce")
        self.gridLayout_6.addWidget(self.lineEdit_form_ecomerce, 1, 2, 1, 1)
        self.lineEdit_form_nome = QtWidgets.QLineEdit(parent=self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_nome.setFont(font)
        self.lineEdit_form_nome.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_nome.setObjectName("lineEdit_form_nome")
        self.gridLayout_6.addWidget(self.lineEdit_form_nome, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_19)
        self.frame_33 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_33.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_33.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_33.setObjectName("frame_33")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_33)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_form_valor = QtWidgets.QLineEdit(parent=self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_valor.setFont(font)
        self.lineEdit_form_valor.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_valor.setObjectName("lineEdit_form_valor")
        self.gridLayout_7.addWidget(self.lineEdit_form_valor, 1, 1, 1, 1)
        self.lineEdit_form_data = QtWidgets.QLineEdit(parent=self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_data.setFont(font)
        self.lineEdit_form_data.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_data.setObjectName("lineEdit_form_data")
        self.gridLayout_7.addWidget(self.lineEdit_form_data, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 1, 3, 1, 1)
        self.lineEdit_form_quantidade = QtWidgets.QLineEdit(parent=self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_quantidade.setFont(font)
        self.lineEdit_form_quantidade.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_quantidade.setObjectName("lineEdit_form_quantidade")
        self.gridLayout_7.addWidget(self.lineEdit_form_quantidade, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_33)
        self.frame_32 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_32.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_32.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_32)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_form_atualizar = QtWidgets.QPushButton(parent=self.frame_32)
        self.pushButton_form_atualizar.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_form_atualizar.setFont(font)
        self.pushButton_form_atualizar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_form_atualizar.setObjectName("pushButton_form_atualizar")
        self.gridLayout_9.addWidget(self.pushButton_form_atualizar, 1, 1, 1, 1)
        self.pushButton_form_inserir = QtWidgets.QPushButton(parent=self.frame_32)
        self.pushButton_form_inserir.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_form_inserir.setFont(font)
        self.pushButton_form_inserir.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_form_inserir.setObjectName("pushButton_form_inserir")
        self.gridLayout_9.addWidget(self.pushButton_form_inserir, 1, 0, 1, 1)
        self.lineEdit_form_procurar_nome = QtWidgets.QLineEdit(parent=self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_form_procurar_nome.setFont(font)
        self.lineEdit_form_procurar_nome.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45,45,45);\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
"    background-color: rgb(30,30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_form_procurar_nome.setObjectName("lineEdit_form_procurar_nome")
        self.gridLayout_9.addWidget(self.lineEdit_form_procurar_nome, 1, 4, 1, 1)
        self.pushButton_form_deletar = QtWidgets.QPushButton(parent=self.frame_32)
        self.pushButton_form_deletar.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pushButton_form_deletar.setFont(font)
        self.pushButton_form_deletar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_form_deletar.setObjectName("pushButton_form_deletar")
        self.gridLayout_9.addWidget(self.pushButton_form_deletar, 1, 2, 1, 1)
        self.pushButton_form_procurar = QtWidgets.QPushButton(parent=self.frame_32)
        self.pushButton_form_procurar.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_form_procurar.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.pushButton_form_procurar.setFont(font)
        self.pushButton_form_procurar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(161, 0, 0);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_form_procurar.setObjectName("pushButton_form_procurar")
        self.gridLayout_9.addWidget(self.pushButton_form_procurar, 1, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_32)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 581, 57))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(100, 6, 100, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_popup_custos = QtWidgets.QFrame(parent=self.frame)
        self.frame_popup_custos.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.frame_popup_custos.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_popup_custos.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_popup_custos.setObjectName("frame_popup_custos")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_popup_custos)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_popup_custos_fixos = QtWidgets.QLabel(parent=self.frame_popup_custos)
        self.label_popup_custos_fixos.setObjectName("label_popup_custos_fixos")
        self.horizontalLayout.addWidget(self.label_popup_custos_fixos)
        self.pushButton_popup_custos_fixos = QtWidgets.QPushButton(parent=self.frame_popup_custos)
        self.pushButton_popup_custos_fixos.setMaximumSize(QtCore.QSize(15, 16777215))
        self.pushButton_popup_custos_fixos.setStyleSheet("background-color: rgb(208, 208, 0);")
        self.pushButton_popup_custos_fixos.setObjectName("pushButton_popup_custos_fixos")
        self.horizontalLayout.addWidget(self.pushButton_popup_custos_fixos)
        self.horizontalLayout_2.addWidget(self.frame_popup_custos)
        MainWindow_estoque.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_estoque)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_estoque)

    def retranslateUi(self, MainWindow_estoque):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_estoque.setWindowTitle(_translate("MainWindow_estoque", "Custos Fixos"))
        self.label_6.setText(_translate("MainWindow_estoque", "Custos Fixos"))
        self.pushButton_form_salvar.setText(_translate("MainWindow_estoque", "Salvar excel"))
        self.label_7.setText(_translate("MainWindow_estoque", "Formecedor"))
        self.lineEdit_form_produto.setPlaceholderText(_translate("MainWindow_estoque", "TI"))
        self.lineEdit_form_ecomerce.setPlaceholderText(_translate("MainWindow_estoque", "Site"))
        self.lineEdit_form_nome.setPlaceholderText(_translate("MainWindow_estoque", "Pro labore"))
        self.label_10.setText(_translate("MainWindow_estoque", "Item"))
        self.lineEdit_form_valor.setPlaceholderText(_translate("MainWindow_estoque", "Marketing"))
        self.lineEdit_form_data.setPlaceholderText(_translate("MainWindow_estoque", "Nuvem de arquivos"))
        self.lineEdit_form_quantidade.setPlaceholderText(_translate("MainWindow_estoque", "DNS"))
        self.pushButton_form_atualizar.setText(_translate("MainWindow_estoque", "Atualizar"))
        self.pushButton_form_inserir.setText(_translate("MainWindow_estoque", "Inserir"))
        self.lineEdit_form_procurar_nome.setPlaceholderText(_translate("MainWindow_estoque", "ID"))
        self.pushButton_form_deletar.setText(_translate("MainWindow_estoque", "Deletar"))
        self.pushButton_form_procurar.setText(_translate("MainWindow_estoque", "Procurar"))
        self.label_popup_custos_fixos.setText(_translate("MainWindow_estoque", "TextLabel"))
        self.pushButton_popup_custos_fixos.setText(_translate("MainWindow_estoque", "x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_estoque = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_estoque()
    ui.setupUi(MainWindow_estoque)
    MainWindow_estoque.show()
    sys.exit(app.exec())
