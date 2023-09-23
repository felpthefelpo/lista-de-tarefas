import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget
from PyQt5.QtGui import QPalette, QColor

class ListaDeTarefas(QWidget):
    def __init__(self):
        super().__init__()

        self.tarefas_a_fazer = []
        self.tarefas_finalizadas = []

        self.setWindowTitle("Lista de Tarefas")
        self.setGeometry(100, 100, 400, 300)

        # Defina o estilo com a cor de fundo preta (#363636) e texto branco (#FFFFFF)
        self.setStyleSheet("background-color: #363636; color: #FFFFFF;")

        # Defina a paleta para cores personalizadas
        palette = QPalette()
        palette.setColor(QPalette.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

        self.layout_principal = QVBoxLayout()

        self.lista_a_fazer = QListWidget()
        self.lista_finalizado = QListWidget()
        
        self.layout_principal.addWidget(self.lista_a_fazer)
        self.layout_principal.addWidget(self.lista_finalizado)

        self.layout_botoes = QHBoxLayout()

        self.entrada_tarefa = QLineEdit()
        self.layout_botoes.addWidget(self.entrada_tarefa)

        self.botao_adicionar = QPushButton("Adicionar")
        self.botao_adicionar.clicked.connect(self.adicionar_tarefa)
        self.layout_botoes.addWidget(self.botao_adicionar)

        self.botao_finalizar = QPushButton("Finalizar")
        self.botao_finalizar.clicked.connect(self.finalizar_tarefa)
        self.layout_botoes.addWidget(self.botao_finalizar)

        self.layout_principal.addLayout(self.layout_botoes)

        self.setLayout(self.layout_principal)

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.text()
        if tarefa:
            self.lista_a_fazer.addItem(tarefa)
            self.entrada_tarefa.clear()

    def finalizar_tarefa(self):
        tarefa_selecionada = self.lista_a_fazer.currentItem()
        if tarefa_selecionada:
            tarefa_texto = tarefa_selecionada.text()
            self.lista_a_fazer.takeItem(self.lista_a_fazer.row(tarefa_selecionada))
            self.lista_finalizado.addItem(tarefa_texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ListaDeTarefas()
    janela.show()
    sys.exit(app.exec_())
