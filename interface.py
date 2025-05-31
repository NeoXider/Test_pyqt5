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
import text_ru as t
import style
import app_info


class TestWindow(QWidget):
    check: bool = True

    def __init__(self, size_win: Tuple, title: str, test: Test) -> None:
        super().__init__()
        self.create_interface(size_win, title)
        self.btn_OK.clicked.connect(self.click_OK)
        self.set_test(test)
        self.show()

    def create_interface(self, size_win: Tuple, title: str) -> None:
        self.setWindowTitle(title)
        self.resize(size_win[0], size_win[1])
        self.setStyleSheet(style.MAIN_STYLE)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.setLayout(self.main_layout)

        self.lb_Question = QLabel("")
        self.lb_Question.setObjectName("QuestionLabel")
        self.main_layout.addWidget(
            self.lb_Question, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.main_layout.addStretch(1)

        self.create_btns()

        self.groupBoxAns = QGroupBox(t.result_group)
        self.groupBoxAns.setObjectName("ResultGroupBox")
        self.main_layout.addWidget(self.groupBoxAns, alignment=Qt.AlignHCenter)

        self.lb_Result = QLabel()
        self.lb_Result.setObjectName("ResultLabel")
        self.lb_Correct = QLabel()
        self.lb_Correct.setObjectName("CorrectAnswerLabel")

        layout_res = QVBoxLayout()
        layout_res.addWidget(self.lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
        layout_res.addWidget(self.lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
        self.groupBoxAns.setLayout(layout_res)
        self.groupBoxAns.hide()

        self.main_layout.addStretch(1)
        self.main_layout.setSpacing(5)
        self.btn_OK = QPushButton("Ответить")
        self.btn_OK.setObjectName("AnswerButton")
        self.main_layout.addWidget(self.btn_OK, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(5)

        # Метка для номера вопроса и общего количества
        self.lb_QuestionCounter = QLabel("")
        self.lb_QuestionCounter.setObjectName("QuestionCounterLabel")
        self.main_layout.addWidget(
            self.lb_QuestionCounter, alignment=Qt.AlignmentFlag.AlignCenter
        )

        # Метка для версии и автора
        self.lb_AppInfo = QLabel(f"v{app_info.APP_VERSION} by {app_info.APP_AUTHOR}")
        self.lb_AppInfo.setObjectName("AppInfoLabel")
        self.main_layout.addWidget(
            self.lb_AppInfo,
            alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight,
        )

    def create_btns(self):
        self.groupBoxRadioBtn = QGroupBox(t.group_btns)
        self.groupBoxRadioBtn.setObjectName("AnswerGroupBox")
        self.main_layout.addWidget(
            self.groupBoxRadioBtn, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.radio_buttons = []
        self.radioGroup = QButtonGroup()
        self.grid_layout = QGridLayout()
        layout = QVBoxLayout()
        layout.addLayout(self.grid_layout)
        self.groupBoxRadioBtn.setLayout(layout)

    def set_test(self, test: Test):
        self.test = test
        self.restart()

    def restart(self) -> None:
        self.test.restart()
        self.set_question(self.test.get_question())
        self.update_question_counter_label()

    def update_question_counter_label(self):
        self.lb_QuestionCounter.setText(
            f"{t.question_word} {self.test.question_id + 1} {t.of_word} {self.test.total}"
        )

    def show_result(self) -> None:
        """показать панель ответов"""
        self.groupBoxAns.show()
        self.btn_OK.setText(t.btn_next)

    def show_question(self) -> None:
        """показать панель вопросов"""
        self.groupBoxAns.hide()
        self.btn_OK.setText(t.btn_answer)

        self.clear_btns()

    def clear_btns(self):
        for b in self.radio_buttons:
            b.setChecked(False)

    def set_question(self, q: Question):
        """функция записывает значения вопроса и ответов в соответствующие виджеты,
        при этом варианты ответов распределяются случайным образом"""
        self.set_buttons(q.get_answers())

        self.lb_Question.setText(q.question)
        self.lb_Correct.setText(q.right_answer)
        self.show_question()
        self.update_question_counter_label()

    def create_radio_buttons(self, answers: List):
        # Удаляем старые радиокнопки
        for btn in self.radio_buttons:
            self.radioGroup.removeButton(btn)
            self.grid_layout.removeWidget(btn)
            btn.deleteLater()
        self.radio_buttons = []
        # Создаём новые радиокнопки по количеству ответов
        for answer in answers:
            btn = QRadioButton(answer)
            self.radio_buttons.append(btn)
            self.radioGroup.addButton(btn)

    def set_buttons(self, answers: List):
        self.create_radio_buttons(answers)
        # Расставляем кнопки по сетке
        for i, btn in enumerate(self.radio_buttons):
            row = i // 2
            col = i % 2
            self.grid_layout.addWidget(
                btn, row, col, alignment=Qt.AlignmentFlag.AlignCenter
            )

    def show_correct(self, res):
        """показать результат - установим переданный текст в надпись "результат" и покажем нужную панель"""
        self.lb_Result.setText(res)
        # Устанавливаем цвет текста в зависимости от результата
        if res == t.right:
            self.lb_Result.setStyleSheet(f"color: {style.RIGHT_COLOR};")
        else:
            self.lb_Result.setStyleSheet(f"color: {style.WRONG_COLOR};")
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
