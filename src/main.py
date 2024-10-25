import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PyQt5.QtGui import QPalette, QColor

app = QApplication(['', '--no-sandbox'])

# Set a dark style (Fusion)
app.setStyle("Fusion")

# Create a dark color palette
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(dark_palette)

window = QMainWindow()
window.setWindowTitle("Flyff Universe")  
window.resize(800, 600)
profile = QWebEngineProfile("MySession") 
page = QWebEnginePage(profile)
session = QWebEngineView()
session.setPage(page)
window.setCentralWidget(session)

try:
    session.setUrl(QUrl('https://universe.flyff.com/play'))
except Exception as e:
    print(f"An error occurred: {str(e)}")

window.show()
sys.exit(app.exec_())
