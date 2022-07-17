from secrets import choice
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

window_titles = [
    'My First Test App',
    'My App',
    'What THe FuCk APP',
    'Something went wrong',
    'There are some bugs',
    'I fixed this!!!',
    'This is my App',
    'My Fixed App',
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.setFixedSize(QSize(300, 200))

        self.button_is_checked = False
        
        self.button = QPushButton("Press Me")
#        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_was_clicked)
        self.windowTitleChanged.connect(self.window_title_was_changed)
#        button.clicked.connect(self.button_was_toggled)
#        self.button.released.connect(self.button_was_released)
#        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("New Window Title: " + new_window_title)
        self.setWindowTitle(new_window_title)

    def window_title_was_changed(self, window_title):
        print("I changed title on - " + window_title)
        if window_title == "What THe FuCk APP":
            self.button.setDisabled(True)

    
#    def button_was_toggled(self, checked):
#        self.button_is_checked = checked
#    def button_was_released(self):
#        self.button_is_checked = self.button.isChecked()
#        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()