from typing import Tuple
from typing_extensions import LiteralString
from question import Question
import random


class Test:
    def __init__(self, questions: Tuple) -> None:
        """Класса Test.
        Args:
            questions (Tuple): Кортеж вопросов.
        """

        self.questions = questions
        self.restart()

    def restart(self) -> None:
        """Перемешивает вопросы и сбрасывает счетчик."""
        self.question_id = 0
        random.shuffle(self.questions)
        self.total = len(self.questions)
        self.right_answer = 0

    def get_question(self) -> Question:
        """Возвращает текущий вопрос."""
        return self.questions[self.question_id]

    def next(self) -> bool:
        """Переходит к следующему вопросу.

        Returns:
            bool: True, если есть следующий вопрос, False в противном случае.
        """
        self.question_id += 1

        return self.question_id < self.total

    def right(self) -> None:
        """Увеличивает счетчик правильных ответов."""
        self.right_answer += 1

    def check(self, answer: str) -> bool:
        """Проверяет ответ на текущий вопрос."""
        return self.get_question().check(answer)

    def get_percent(self) -> float:
        """Возвращает процент правильных ответов.
        Returns:
            float: Процент правильных ответов.
        """
        return round(self.right_answer / self.total, 2)

    def get_result_right(self) -> LiteralString:
        return f"Правильных ответов: {self.right_answer}"

    def get_result_total(self) -> LiteralString:
        return f"Всего вопросов: {self.total}"

    def get_result_percent(self) -> LiteralString:
        return f"Процент правильных ответов: {self.get_percent()}"
