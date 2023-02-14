from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


app = QApplication([])


'''json notes'''
notes = {
    "Welcome" : {
        "text" : "Lorem Ipsum",
        "tags" : ["latin", "test"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)




'''Interface'''
notes_win = QWidget()
notes_win.setWindowTitle('Simple notes')
notes_win.resize(900, 600)


list_notes = QListWidget()
list_notes_label = QLabel('Notes list')


button_note_create = QPushButton('Create note') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Write your tag...')
field_text = QTextEdit()
button_tag_add = QPushButton('Add to note')
button_tag_del = QPushButton('Delete tag from note')
button_tag_search = QPushButton('Search note')
list_tags = QListWidget()
list_tags_label = QLabel('Tags list')


#Layouts
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)


'''Functions'''
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])


'''Launch'''
list_notes.itemClicked.connect(show_note)


'''Start'''
notes_win.show()


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exec_()
