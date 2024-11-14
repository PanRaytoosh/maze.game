from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(400.500)

v_line = QVBoxLayout()

def click_btn():
    secret_text.setText('Ти простро чудо!')

btn = QPushButton('click me')
btn.clicked.connect(click_btn)

v_line.addWidget(btn, alignment=Qt.AlignCenter)

secret
app = QApplication(sys.argv)
line_edit = QLineEdit()
line_edit.textChanged.connect(handle_text_changed)
line_edit.show()

app.exec_()
