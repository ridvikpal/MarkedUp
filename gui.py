'''
This file contains all the functions for creating the gui
using the PyQt5 library
'''

''' IMPORT MODULES '''
import sys, os
import plotly.offline
import plotly.express as px
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

''' FUNCTION DEFINITIONS '''
# show the plotly figure in a seperate window using QT web engine
def show_in_window(fig, name: str):
    fig.update_layout(title_text=name, title_x=0.5, title_font_size=20)

    plotly.offline.plot(fig, filename='figure.html', auto_open=False)

    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "figure.html"))
    web.load(QUrl.fromLocalFile(file_path))
    web.show()
    sys.exit(app.exec_())