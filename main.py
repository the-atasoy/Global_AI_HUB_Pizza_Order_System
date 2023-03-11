import sys

if __name__ == '__main__':
    from GUI_Pages.MainPage import *
    uyg = QApplication(sys.argv)
    pencere = MainPage()
    pencere.show()
    sys.exit(uyg.exec_()) 