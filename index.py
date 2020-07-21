from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType
import mysql.connector as connector

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
        self.btn_add_category.clicked.connect(self.Add_Category)
        self.btn_add_author.clicked.connect(self.Add_Author)
        self.btn_add_publisher.clicked.connect(self.Add_Publisher)

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
        self.db = connector.connect(host='localhost', user='root', password='Abcd@1234', db='library')

        self.cur = self.db.cursor()
        book_title = self.ltxt_add_book_title.text()
        book_code = self.ltxt_add_book_code.text()
        book_category = self.cb_book_category.CurrentText()
        book_author = self.cb_book_author.CurrentText()
        book_publisher = self.cb_book_publisher.CurrentText()
        book_price = self.ltxt_add_book_price.text()

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

    # -----------Settings tab-------------------
    def Add_Category(self):
        self.db = connector.connect(host='localhost', user='root', passwd='Abcd@1234', database='library')
        self.cur = self.db.cursor()
        category_name = self.ltxt_category_name.text()
        self.cur.execute('''
            INSERT INTO categories (category_name) VALUES (%s)
        ''', (category_name,))

        self.db.commit()
        self.statusBar().showMessage('new category added')


    def Add_Author(self):
        self.db = connector.connect(host='localhost', user='root', passwd='Abcd@1234', database='library')
        self.cur = self.db.cursor()
        author_name = self.ltxt_author_name.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES (%s)
        ''', (author_name,))

        self.db.commit()
        self.statusBar().showMessage('new author added')

    def Add_Publisher(self):
        self.db = connector.connect(host='localhost', user='root', passwd='Abcd@1234', database='library')
        self.cur = self.db.cursor()
        publisher_name = self.ltxt_publisher_name.text()
        self.cur.execute('''
            INSERT INTO publishers (publisher_name) VALUES (%s)
        ''', (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('new publisher added')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
