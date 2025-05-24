from interface import TestWindow
from test import Test

# сами вопросы теста
from test_question import questions_list


def main() -> None:
    test = Test(questions_list)
    app = TestWindow((800, 500), "Тест", test)
    app.exec()


if __name__ == "__main__":
    main()
