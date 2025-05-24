from random import shuffle


class Question:
    """содержит вопрос, правильный ответ и неправильные"""

    def __init__(self, question, right_answer, *args) -> None:
        """Конструктор класса Question.

        Args:
            question (str): Текст вопроса.
            right_answer (str): Правильный ответ.
            args: неправильные ответы
        """
        self.question = question
        self.right_answer = right_answer
        self.wrong_answers = list(args)

    def check(self, answer: str) -> bool:
        """Проверяет, является ли ответ правильным.

        Args:
            answer (str): Ответ пользователя.

        Returns:
            bool: True, если ответ правильный, False в противном случае.
        """
        return answer == self.right_answer

    def get_answers(self) -> list:
        """_summary_
        Возвращает список всех ответов, включая правильный. (Перемешивая)

        Returns:
            _type_: List<str>
        """

        answers = self.wrong_answers + [self.right_answer]
        shuffle(answers)
        return answers
