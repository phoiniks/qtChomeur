#!/usr/bin/python3
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        labels = []
        inputText = []
        
        layout = QGridLayout()

        for label in ["Bezeichnung:", "Firma:", "Ansprechpartner:",
                      "Anrede:", "Straße:", "PLZ:", "Telefon:",
                      "Mobil:", "E-Mail:", "Website:", "Quelle:",
                      "Ergebnis:"]:
            labels.append(QLabel(label))

        for inp in ["Bezeichnung", "Firma", "Ansprechpartner",
                      "Anrede", "Straße", "PLZ", "Telefon",
                      "Mobil", "E-Mail", "Website", "Quelle",
                      "Ergebnis"]:
            inputText.append(QLineEdit(inp))

        idx = 0
        for cnt in range(0, len(labels)):
            print("idx: {}, cnt: {}".format(idx, cnt))
            layout.addWidget(labels[cnt], cnt, 0)
            layout.addWidget(inputText[cnt], cnt, 1)
            
        self.setLayout(layout)
        self.setWindowTitle("Chomeur")


if __name__=="__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
