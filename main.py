# импорт библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

# класс для хранения вопросов
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# список вопросов
questions_list=[]
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Что символизируют звёзды на флаге США?', 'Штаты', 'Деньги', 'Свобода', 'Ядерное оружие'))
questions_list.append(Question('Внезапная алгебра: выберите правильную формулу дискриминанта', 'b^2-4ac', 'b^2+4ac', 'b^4-2ac', 'b^4+2ac'))
shuffle(questions_list)

# создание приложения, главного окна, и его настройка
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memo card')
main_win.resize(500, 300)
main_win.setStyleSheet('background-color: #5c5c5c;')

# счётчики
main_win.cur_question = 0
main_win.total = 0
main_win.score = 0

# создание виджетов
btn_ok = QPushButton('Ответить')
lb_Question = QLabel('Вопрос')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')
btn_ok.setStyleSheet('background-color: #3b3b3b;')

# создание групп
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
AnsGroupBox = QGroupBox('Результаты теста')
RadioGroupBox.setStyleSheet('background-color: #3b3b3b;')
AnsGroupBox.setStyleSheet('background-color: #3b3b3b;')

# функция, отображающая окно результата
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

# функция, отображающая окно вопроса
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

# список кнопок, для удобства последующей рандомизации
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# функция, отображающая вопросы, ответы, и рандомизирующая их положение
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

# функция, показывающая, правильно ли ответил пользователь
def show_correct(res):
    lb_Result.setText(res)
    show_result()

# функция, проверяющая правильность ответа
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неверно!')

# функция, отображающая следующий вопрос и статистику
def next_question():
    main_win.cur_question += 1
    main_win.total += 1
    print('Статистика:\nВсего вопросов -', main_win.total, '\nПравильных ответов - ', main_win.score, '\nРейтинг -', str(main_win.score/main_win.total*100)+'%')
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
        last=questions_list[len(questions_list)-1]
        shuffle(questions_list)
        while last == questions_list[0]:
            shuffle(questions_list)
    q = questions_list[main_win.cur_question]
    ask(q)

# функция, определяющая, какую функцию запускает кнопка
def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


# создание лэйаутов и расположение виджетов по ним
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=3)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

main_win.setLayout(layout_card)


# отображение вопросов и обработка ответов
ask(questions_list[0])
btn_ok.clicked.connect(click_OK)

# отображение окна
main_win.show()
app.exec_()