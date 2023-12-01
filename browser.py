import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import *
from urllib.parse import urlparse
from PyQt5.QtGui import QPixmap

class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()
        loadUi("browser.ui", self)

        self.browser = QWebEngineView()
        self.verticalLayout_2.addWidget(self.browser)

        self.lineEdit.returnPressed.connect(self.navigate_to_url)

        self.back.clicked.connect(self.browser.back)

        self.forward.clicked.connect(self.browser.forward)

        self.refresh.clicked.connect(self.browser.reload)

        self.home.clicked.connect(self.show_home)
    def show_home(self):
        self.browser.setUrl(QUrl('http://example.com'))
    
    def navigate_to_url(self):
        url = self.lineEdit.text()
        parsed_url = urlparse(url)
        if parsed_url.scheme == '':
            url = 'https://www.' + url
        self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('Michael Browser')
window = BrowserWindow()
window.show()
sys.exit(app.exec_())