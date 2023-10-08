from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

window.resize(600,600)
app.setStyleSheet("""
    QWidget {
        background-color: yellow;
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

text = QTextEdit()

bludfish = QLabel("список тегів")
nener = QLabel("пошук тегів")
textjer = QLineEdit()

titwar0 = QPushButton("основа")
titwar1 = QPushButton("оукв")
titwar2 = QPushButton("яйко")
titwar3 = QPushButton("пупумпум")
titwar4 = QPushButton("пуши яйко")
titwar5 = QPushButton("пампампам")

arktika = QListWidget()
jegfa = QListWidget()

mainLine = QHBoxLayout()
mainLine.addWidget(text)
line1 = QVBoxLayout()
lines2 = QVBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

mainLine.addLayout(line1)

line1.addLayout(line2)
line1.addLayout(line3)

v1 = QVBoxLayout()
v1.addWidget(text)


v2 = QVBoxLayout(textjer)
v2 = QVBoxLayout()
v2.addWidget(bludfish)
v2.addWidget(arktika)

v2.addWidget(titwar4)
v2.addWidget(titwar2,)

v2.addWidget(titwar3),

v2.addWidget(nener)
mainLine.addLayout(v2)

v2.addWidget(jegfa)
v2.addWidget(titwar1)
v2.addWidget(titwar0)
v2.addWidget(titwar5)









window.setLayout(mainLine)
window.show()
app.exec()