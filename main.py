from PyQt5.QtWidgets import *

app = QApplication([])



window = QWidget()
window.resize(800, 500)
mainline = QHBoxLayout()
app.setStyleSheet("""
    QWidget {
        background-color: purple;
    }

    QPushButton{
        background-color: brown;
    }
    GroupBox{
        background: rgb(177,24,24);

    }
    QRadioButton{
        background-color: red;
    }
    QLabel{
        background-color: #b11818;
        }
""")

titwar1 = QPushButton('створити замітку')
titwar2 = QPushButton('видалити замітку')
titwar3 = QPushButton('зберегти замітку')
titwar4 = QPushButton('додати до замітки')
titwar5 = QPushButton('відкріпити від замітки')
titwar6 = QPushButton('Шукати по тегу')
text1 = QLabel('список заміток')
text2 = QLabel('список тегів')
pole1 = QTextEdit()
pole2 = QListWidget()
pole3 = QListWidget()
pole4 = QLineEdit()

linepole = QVBoxLayout()
linemenu = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

mainline.addLayout(linepole)
mainline.addLayout(linemenu)
linepole.addWidget(pole1)
linemenu.addWidget(text1)
linemenu.addWidget(pole2)
line1.addWidget(titwar1)
line1.addWidget(titwar2)
linemenu.addLayout(line1)
linemenu.addWidget(titwar3)
linemenu.addWidget(text2)
linemenu.addWidget(pole3)
linemenu.addWidget(pole4)
line2.addWidget(titwar4)
line2.addWidget(titwar5)
linemenu.addLayout(line2)
linemenu.addWidget(titwar6)

window.setLayout(mainline)
window.show()
app.exec()
