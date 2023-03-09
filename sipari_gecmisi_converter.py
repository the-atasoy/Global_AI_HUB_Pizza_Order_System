from PyQt5 import uic
with open("UI_Files/siparis_gecmisi_UI.py", "w", encoding="utf-8") as fout:
    uic.compileUi("siparis_gecmisi_UI.ui", fout)
    