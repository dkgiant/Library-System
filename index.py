from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hidding_Themes()
        self.tab_main.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.btn_showthemes.clicked.connect(self.Show_themes)
        self.btn_hidethemes.clicked.connect(self.Hidding_Themes)
        self.btn_daytoday.clicked.connect(self.Open_Day_To_Day_Tab)
        self.btn_books.clicked.connect(self.Open_Books_Tab)
        self.btn_users.clicked.connect(self.Open_Users_Tab)
        self.btn_settings.clicked.connect(self.Open_Settings_Tab)

    def Show_themes(self):
        self.gb_themes.show()

    def Hidding_Themes(self):
        self.gb_themes.hide()

    # -----------Tab Handler-----------------
    def Open_Day_To_Day_Tab(self):
        self.tab_main.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tab_main.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tab_main.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tab_main.setCurrentIndex(3)

    # -----------Books tab-------------------
    def Add_New_Book(self):
        pass

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass

    # -----------Users tab-------------------
    def Add_New_User(self):
        pass

    def Edit_User(self):
        pass

    def Login(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
