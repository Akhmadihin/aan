import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"
os.environ["QT_QUICK_BACKEND"] = "software"

app = QApplication(sys.argv)

# Главное окно
window = QWidget()
window.setWindowTitle("WebView с взаимодействием")
window.showFullScreen()

# WebView
webview = QWebEngineView()
webview.load(QUrl("https://sites.google.com/view/kubiki/главная-страница"))

# Проверка загрузки
def on_load_finished(ok):
    if ok:
        print("Страница загружена")
        webview.page().runJavaScript("document.title", lambda title: print(f"Title: {title}"))
    else:
        print("Ошибка загрузки")

webview.loadFinished.connect(on_load_finished)

# Layout
layout = QVBoxLayout()
layout.addWidget(webview)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
