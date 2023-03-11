import sys

if __name__ == '__main__':
    from GUI_Pages.MainPage import *
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec_())