import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from urllib.parse import urlparse
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStyleSheet("background-color: white;")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_screen = QWidget()
        self.browser_screen = QWidget()

        self.create_home_screen()
        self.create_browser_screen()

        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.browser_screen)

        self.stacked_widget.setCurrentWidget(self.home_screen)

        self.showMaximized()

    def create_home_screen(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.home_screen.setLayout(layout)
        welcome_label = QLabel("Welcome to Michael Browser")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 50px;")
        layout.addWidget(welcome_label, alignment=Qt.AlignCenter)

        image_label = QLabel()
        pixmap = QPixmap('blog_6.jpg') 
        pixmap = pixmap.scaledToWidth(400) 
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)
                

        enter_button = QPushButton("Enter Browser")
        enter_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px;")
        enter_button.clicked.connect(self.show_browser)
        layout.addWidget(enter_button)
        

    def create_browser_screen(self):
        layout = QVBoxLayout()
        self.browser_screen.setLayout(layout)

        navbar = QToolBar()
        layout.addWidget(navbar)

        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.show_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.page().urlChanged.connect(self.update_url)

    def show_browser(self):
        self.stacked_widget.setCurrentWidget(self.browser_screen)
        self.browser.setUrl(QUrl('http://example.com'))

    def show_home(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

    def navigate_to_url(self):
        url = self.url_bar.text()
        parsed_url = urlparse(url)
        if parsed_url.scheme == '':
            url = 'https://www.' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Michael Browser')
window = MainWindow()
window.show()
sys.exit(app.exec_())
