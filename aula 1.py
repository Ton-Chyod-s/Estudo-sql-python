import plotly.graph_objects as go
import plotly.offline as pyo
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication

import tratamento_db_v2 as tr
tratamento = tr.tratamento_db()

class Principal(QMainWindow):
    def __init__(self):
        super().__init()
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)
        
        layout = go.Layout(title="Exemplo de Gráfico Plotly em PyQt5")
        fig = go.Figure(data=tratamento.grafico_barra(), layout=layout)
        
        # Save the Plotly graph to an HTML file
        pyo.plot(fig, filename='plotly_graph.html', auto_open=False)
        
        # Set the URL for the QWebEngineView
        self.web_view.setUrl(QtCore.QUrl.fromLocalFile('plotly_graph.html'))

if __name__ == "__main__":
    app = QApplication([])
    principal = Principal()
    principal.show()
    app.exec()
