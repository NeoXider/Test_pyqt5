from interface import TestWindow
from test import Test
from test_question import questions_list
from PyQt5.QtWidgets import QApplication


def main() -> None:
    test = Test(questions_list)
    app = QApplication([])
    win = TestWindow((700, 700), "Тест", test)
    app.exec_()


if __name__ == "__main__":
    main()
