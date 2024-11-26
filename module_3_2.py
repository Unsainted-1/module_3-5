def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if '@' not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}. Возможно, вы забыли @')
    elif '.com' in recipient or '.ru' in recipient or '.net' in recipient:
        if '.com' in sender or '.ru' in sender or '.net' in sender:
            if recipient == sender:
                print('Нельзя отправить письмо самому себе!')
            elif sender != 'university.help@gmail.com':
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
         print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Хочу сказать, что я устал выполнять это задание', 'urban.teachermail.ru', sender='urban.teacher@mail.ru')
send_email('Хотел написать типо (.com or .ru) not in (recipent or sender) и постоянно залупа выходила]', 'wrinwrin@yandex.ru', sender='university.help@gmail.com')