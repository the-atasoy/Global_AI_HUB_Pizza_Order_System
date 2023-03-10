if __name__ == '__main__':
    from connections.Anaekran import *
    uyg = QApplication(sys.argv)
    pencere = MainPage()
    pencere.show()
    sys.exit(uyg.exec_()) 