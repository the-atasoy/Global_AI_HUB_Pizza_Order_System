from PyQt5 import uic
with open("odeme_UI.py", "w", encoding="utf-8") as fout:
    uic.compileUi("odeme_UI.ui", fout)
    