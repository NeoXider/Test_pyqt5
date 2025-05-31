# Цвета (Киберпанк)
BG_COLOR = "#1a1a1a"  # Цвет фона приложения
QUESTION_COLOR = "#cccccc"  # Цвет текста вопроса и основного текста меток
ANSWER_COLOR = "#999999"  # Цвет текста ответов по умолчанию (неактивные радиокнопки)
RIGHT_COLOR = "#39ff14"  # Цвет текста для индикации правильного результата
WRONG_COLOR = "#ff00ff"  # Цвет текста для индикации неправильного результата
BUTTON_COLOR = "#00ffff"  # Цвет фона основной кнопки
BUTTON_TEXT_COLOR = "#1a1a1a"  # Цвет текста на основной кнопке и выбранных радиокнопках
RADIO_BG_COLOR = "#2a2a2a"  # Цвет фона радиокнопок
RADIO_BORDER_COLOR = "#555555"  # Цвет границы радиокнопок
RADIO_CHECKED_COLOR = "#8a2be2"  # Цвет фона выбранной радиокнопки и индикатора
RADIO_TEXT_COLOR = "#999999"  # Цвет текста радиокнопок по умолчанию
GROUPBOX_BORDER_COLOR = "#3498db"  # Цвет границы группы радиокнопок
GROUPBOX_TITLE_COLOR = "#2980b9"  # Цвет заголовка группы радиокнопок

# Новые цвета для блока результатов
RESULT_BOX_BORDER_COLOR = "#ff8c00"  # Оранжевая граница
RESULT_BOX_TITLE_COLOR = "#ff8c00"  # Оранжевый заголовок
CORRECT_ANSWER_TEXT_COLOR = "#ff8c00"  # Неоново-оранжевый для правильного ответа

# Шрифты
FONT_FAMILY = "Segoe UI, Arial, sans-serif"  # Семейство шрифтов
QUESTION_FONT_SIZE = 18  # Размер шрифта вопроса
ANSWER_FONT_SIZE = 15  # Размер шрифта ответов и текста в блоках
BUTTON_FONT_SIZE = 16  # Размер шрифта кнопок

# Стили для виджетов
MAIN_STYLE = f"""
    QWidget {{
        background: {BG_COLOR}; /* Цвет фона главного окна */
        color: {QUESTION_COLOR}; /* Цвет текста по умолчанию для виджетов в окне (если не переопределен) */
    }}
    QLabel {{
        color: {QUESTION_COLOR}; /* Цвет текста по умолчанию для всех меток */
    }}
    QLabel#QuestionLabel {{
        color: {QUESTION_COLOR}; /* Цвет текста для метки вопроса */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: 22px; /* Увеличен размер шрифта */
        font-weight: bold; /* Жирный шрифт */
    }}
    QLabel#CorrectAnswerLabel {{
        color: {CORRECT_ANSWER_TEXT_COLOR}; /* Цвет текста правильного ответа */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: {ANSWER_FONT_SIZE}px; /* Размер шрифта */
    }}
    QLabel#ResultLabel {{
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: {ANSWER_FONT_SIZE}px; /* Размер шрифта */
        font-weight: bold; /* Жирный шрифт */
        /* Цвет текста для ResultLabel устанавливается в коде (interface.py) */
    }}
    QRadioButton {{
        color: {RADIO_TEXT_COLOR}; /* Цвет текста радиокнопки */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: {ANSWER_FONT_SIZE}px; /* Размер шрифта */
        padding: 8px 16px; /* Внутренние отступы */
        margin-bottom: 10px; /* Внешний нижний отступ */
        background-color: {RADIO_BG_COLOR}; /* Цвет фона радиокнопки */
        border: 1px solid {RADIO_BORDER_COLOR}; /* Граница */
        border-radius: 5px; /* Скругление углов */
    }}
    QRadioButton:checked {{
        background-color: {RADIO_CHECKED_COLOR}; /* Цвет фона выбранной радиокнопки */
        color: {BUTTON_TEXT_COLOR}; /* Цвет текста выбранной радиокнопки */
    }}
    QRadioButton::indicator {{
        width: 15px; /* Ширина индикатора */
        height: 15px; /* Высота индикатора */
        border-radius: 7px; /* Скругление индикатора (делает его круглым) */
    }}
    QRadioButton::indicator:checked {{
        background-color: {RADIO_CHECKED_COLOR}; /* Цвет фона выбранного индикатора */
        border: 1px solid {RADIO_CHECKED_COLOR}; /* Граница выбранного индикатора */
    }}
    QPushButton {{
        background: {BUTTON_COLOR}; /* Цвет фона кнопки */
        color: {BUTTON_TEXT_COLOR}; /* Цвет текста кнопки */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: {BUTTON_FONT_SIZE}px; /* Размер шрифта */
        border-radius: 8px; /* Скругление углов */
        padding: 12px 28px; /* Внутренние отступы */
        margin-top: 16px; /* Внешний верхний отступ */
        margin-bottom: 8px; /* Внешний нижний отступ */
    }}
    QPushButton:hover {{
        background: #00bfff; /* Цвет фона кнопки при наведении */
    }}
    QGroupBox {{
        border: 1px solid #c8d6e5; /* Граница группы по умолчанию */
        border-radius: 8px; /* Скругление углов группы */
        margin-top: 18px; /* Внешний верхний отступ */
        margin-bottom: 18px; /* Внешний нижний отступ */
        padding: 18px 12px; /* Внутренние отступы */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: 15px; /* Размер шрифта заголовка */
    }}
    QGroupBox#AnswerGroupBox {{
        border: 2px solid {GROUPBOX_BORDER_COLOR}; /* Цвет и толщина границы группы ответов */
        font-weight: bold; /* Жирный шрифт заголовка */
    }}
    QGroupBox#AnswerGroupBox::title {{
        color: {GROUPBOX_TITLE_COLOR}; /* Цвет заголовка группы ответов */
        subcontrol-origin: margin; /* Местоположение заголовка относительно края */
        subcontrol-position: top center; /* Выравнивание заголовка сверху по центру */
        padding: 0 3px; /* Внутренние отступы заголовка */
    }}
    QPushButton#AnswerButton {{
        padding: 6px 18px;
        font-size: 18px; /* Увеличен размер шрифта */
        min-width: 200px;
        min-height: 28px;
        border-radius: 20px;
    }}
    QGroupBox#ResultGroupBox {{
        border: 2px solid {RESULT_BOX_BORDER_COLOR}; /* Цвет и толщина границы блока результатов */
        font-weight: bold; /* Жирный шрифт заголовка */
    }}
    QGroupBox#ResultGroupBox::title {{
        color: {RESULT_BOX_TITLE_COLOR}; /* Цвет заголовка блока результатов */
        subcontrol-origin: margin; /* Местоположение заголовка относительно края */
        subcontrol-position: top center; /* Выравнивание заголовка сверху по центру */
        padding: 0 3px; /* Внутренние отступы заголовка */
    }}
    QLabel#QuestionCounterLabel {{
        color: {ANSWER_COLOR}; /* Цвет текста счетчика вопросов */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: 12px; /* Размер шрифта */
        margin-top: 8px; /* Отступ сверху от кнопки */
    }}
    QLabel#AppInfoLabel {{
        color: {ANSWER_COLOR}; /* Цвет текста метки версии и автора */
        font-family: {FONT_FAMILY}; /* Семейство шрифтов */
        font-size: 10px; /* Размер шрифта */
        margin-right: 5px; /* Отступ справа */
        margin-bottom: 5px; /* Отступ снизу */
    }}
"""
