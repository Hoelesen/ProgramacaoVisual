import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


# Main Window
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTableWidget'
        self.left = 0
        self.top = 0
        self.width = 1100
        self.height = 400
        self.setStyleSheet('background-color: #f8f9fa;')

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()        

        titulo = QLabel("Seja bem vindo", self)
        titulo.move(10, 10)
        titulo.resize(180, 30)
        titulo.setStyleSheet('QLabel {font-size: 25px}')

        subtitulo = QLabel(
            "Este é o portal de serviço, um portal onde você pode acessar os recursos disponíveis", self)
        subtitulo.move(10, 40)
        subtitulo.resize(170, 30)
        subtitulo.setStyleSheet('QLabel {font-size: 15px}')

        botao1 = QPushButton('Novo serviço', self)
        botao1.move(20, 90)
        botao1.resize(170, 130)
        botao1.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        botao2 = QPushButton('Serviços em andamento', self)
        botao2.move(210, 90)
        botao2.resize(230, 130)
        botao2.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        botao3 = QPushButton('Entradas e saídas diárias', self)
        botao3.move(20, 230)
        botao3.resize(170, 130)
        botao3.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        botao4 = QPushButton('Agendamentos a receber', self)
        botao4.move(210, 230)
        botao4.resize(170, 130)
        botao4.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        botao5 = QPushButton('Relatórios', self)
        botao5.move(20, 370)
        botao5.resize(170, 130)
        botao5.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        botao6 = QPushButton('Cadastros', self)
        botao6.move(210, 370)
        botao6.resize(170, 130)
        botao6.setStyleSheet('QPushButton {background-color: white; color: #0d6efd; font-size:20px; margin: 12px; border: 1px solid gray; border-radius: 5px; padding: 35px 5px 35px 5px;}')

        self.layout = QVBoxLayout()
        content_layout = QGridLayout()
        buttons_layout = QVBoxLayout()
        title_layout = QVBoxLayout()

        title_layout.addWidget(titulo)
        title_layout.addWidget(subtitulo)
        button_section1_layout = QHBoxLayout()
        botao1.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section1_layout.addWidget(botao1)
        botao2.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section1_layout.addWidget(botao2)

        button_section2_layout = QHBoxLayout()
        botao3.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section2_layout.addWidget(botao3)
        botao4.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section2_layout.addWidget(botao4)

        button_section3_layout = QHBoxLayout()
        botao5.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section3_layout.addWidget(botao5)
        botao6.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        button_section3_layout.addWidget(botao6)

        buttons_layout.addLayout(button_section1_layout)
        buttons_layout.addLayout(button_section2_layout)
        buttons_layout.addLayout(button_section3_layout)

        content_layout.addLayout(buttons_layout, 0, 0, 1, 1)
        content_layout.addWidget(self.tableWidget, 0, 1, 1, 1)
        content_layout.setColumnStretch(1, 3)

        self.layout.addLayout(title_layout)
        self.layout.addLayout(content_layout)

        self.setLayout(self.layout)
        # Show window
        self.show()

    # Create table
    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.move(300, 20)
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        # Row count
        self.tableWidget.setRowCount(8)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        # Column count
        self.tableWidget.setColumnCount(7)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Id"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Nome"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Veículo"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Hr. busca"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Hr. entrega"))
        self.tableWidget.setItem(0, 5, QTableWidgetItem("Busca"))
        self.tableWidget.setItem(0, 6, QTableWidgetItem("Entrega"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("José Almeida dos Santos"))
        self.tableWidget.setItem(1, 2, QTableWidgetItem("Gol G5"))
        self.tableWidget.setItem(1, 3, QTableWidgetItem("08:05"))
        self.tableWidget.setItem(1, 4, QTableWidgetItem("10:25"))
        chkBoxItem1 = QTableWidgetItem()
        chkBoxItem1.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkBoxItem1.setCheckState(QtCore.Qt.Unchecked)  
        self.tableWidget.setItem(1, 5, chkBoxItem1)
        chkBoxItem2 = QTableWidgetItem()
        chkBoxItem2.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkBoxItem2.setCheckState(QtCore.Qt.Unchecked)  
        self.tableWidget.setItem(1, 6, chkBoxItem2)

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
