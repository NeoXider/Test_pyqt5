from ast import Tuple
from typing import List
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QButtonGroup,
    QRadioButton,
    QPushButton,
    QLabel,
    QGridLayout,
    QMessageBox,
)

from question import Question
from test import Test
import text_en as t


class TestWindow(QApplication):
    check: bool = True

    def __init__(self, size_win: Tuple, title: str, test: Test) -> None:
        super().__init__([])
        self.create_interface(size_win, title)
        self.btn_OK.clicked.connect(self.click_OK)

        self.set_test(test)

    def create_interface(self, size_win: Tuple, title: str) -> None:
        self.main_win = QWidget()
        self.main_win.setWindowTitle(title)
        self.main_win.resize(size_win[0], size_win[1])
        self.main_win.show()

        self.main_layout = QVBoxLayout()
        self.main_win.setLayout(self.main_layout)

        self.main_layout.addStretch(1)
        self.lb_Question = QLabel("")
        self.main_layout.addWidget(
            self.lb_Question, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.main_layout.addStretch(1)

        self.create_btns()

        self.groupBoxAns = QGroupBox(t.result_group)
        self.main_layout.addWidget(self.groupBoxAns)
        self.lb_Result = QLabel()
        self.lb_Correct = QLabel()

        layout_res = QVBoxLayout()
        layout_res.addWidget(self.lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
        layout_res.addWidget(self.lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
        self.groupBoxAns.setLayout(layout_res)
        self.groupBoxAns.hide()

        self.main_layout.addStretch(1)
        self.main_layout.setSpacing(5)
        self.btn_OK = QPushButton("Ответить")
        self.main_layout.addWidget(self.btn_OK, stretch=2)
        self.main_layout.setSpacing(5)

    def create_btns(self):
        self.groupBoxRadioBtn = QGroupBox(t.group_btns)
        self.main_layout.addWidget(
            self.groupBoxRadioBtn, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.radio_buttons = [QRadioButton(str(i + 1)) for i in range(4)]
        self.radioGroup = QButtonGroup()
        for btn in self.radio_buttons:
            self.radioGroup.addButton(btn)

        self.grid_layout = QGridLayout()
        id = -1
        for r in range(2):
            for c in range(2):
                id += 1
                self.grid_layout.addWidget(
                    self.radio_buttons[id], r, c, alignment=Qt.AlignmentFlag.AlignCenter
                )
                if id + 1 >= len(self.radio_buttons):
                    break

        layout = QVBoxLayout()
        layout.addLayout(self.grid_layout)
        self.groupBoxRadioBtn.setLayout(layout)

    def set_test(self, test: Test):
        self.test = test
        self.restart()

    def restart(self) -> None:
        self.test.restart()
        self.set_question(self.test.get_question())

    def show_result(self) -> None:
        """показать панель ответов"""
        self.groupBoxRadioBtn.hide()
        self.groupBoxAns.show()
        self.btn_OK.setText(t.btn_next)

    def show_question(self) -> None:
        """показать панель вопросов"""
        self.groupBoxRadioBtn.show()
        self.groupBoxAns.hide()
        self.btn_OK.setText(t.btn_answer)

        self.clear_btns()

    def clear_btns(self):
        self.radioGroup.setExclusive(False)
        for b in self.radio_buttons:
            b.setChecked(False)
        self.radioGroup.setExclusive(True)

    def set_question(self, q: Question):
        """функция записывает значения вопроса и ответов в соответствующие виджеты,
        при этом варианты ответов распределяются случайным образом"""
        self.set_buttons(q.get_answers())

        self.lb_Question.setText(q.question)
        self.lb_Correct.setText(q.right_answer)
        self.show_question()

    def set_buttons(self, answers: List):
        for b in self.radio_buttons:
            b.setText(answers.pop())

    def show_correct(self, res):
        """показать результат - установим переданный текст в надпись "результат" и покажем нужную панель"""
        self.lb_Result.setText(res)
        self.show_result()

    def check_answer(self) -> bool:
        """если выбран какой-то вариант ответа, то надо проверить и показать панель ответов"""
        btn = self.radioGroup.checkedButton()
        if btn is None:
            return False

        if self.test.check(btn.text()):
            self.show_correct(t.right)
            self.test.right()
            print(t.right)
        else:
            self.show_correct(t.fail)
            print(t.fail)

        print(self.test.get_result_total())
        return True

    def next_question(self):
        """задает случайный вопрос из списка"""
        self.test.next()
        self.set_question(self.test.get_question())

    def click_OK(self):
        """определяет, надо ли показывать другой вопрос либо проверить ответ на этот"""
        if self.check:
            if self.check_answer():
                self.check = not self.check
        else:
            if self.test.question_id + 1 >= self.test.total:
                stats = (
                    f"{self.test.get_result_right()}\n"
                    f"{self.test.get_result_total()}\n"
                    f"{self.test.get_result_percent()}"
                )
                msg = QMessageBox()
                msg.setWindowTitle(t.result_group)
                msg.setText(f"{t.end}\n\n" + stats)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                self.restart()
            else:
                self.next_question()
            self.check = not self.check
