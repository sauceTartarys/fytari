from PyQt5.QtWidgets import *

app = QApplication([])


import json

try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)

except:
    notes = {}




window = QWidget()
window.resize(800, 460)



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


def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку","Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
    pole2.clear()
    pole1.clear()
    pole2.addItems(notes)
    with open("notes_data.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)
def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = pole2.selectedItems()[0].text()
    print(key)
    pole1.setText(notes[key]["текст"])
    pole3.clear()
    pole3.addItems(notes[key]["теги"])


pole2.itemClicked.connect(show_note)

def save_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes[key]["текст"] = pole1.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
                json.dump(notes, file, ensure_ascii=False)
    else:
                print("Замітка для збереження не вибрана!")


def del_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes.pop(key)
        pole2.clear()
        pole1.clear()
        pole3.clear()
        pole2.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")


titwar1.clicked.connect(add_note)


titwar3.clicked.connect(save_note)


window.setLayout(mainline)
window.show()
print(notes)
pole2.addItems(notes)


app.exec()

window.setLayout(mainline)
window.show()
app.exec()
