import time

class User:
    def __init__(self):
        self.data = []

    def add_user(self, nickname, password, age):
        self.data.append({'nickname': nickname, 'password': password, 'age': age})

class Video:
    def __init__(self, title, duration, adult_mode):
        self.title = title
        self.duration = duration
        self.adult_mode = bool

    def dura(self, title):
        for i in ur.videos:
            if title == i:
                return self.duration

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.video_o = []
        self.current_user = None

    def log_in(self, nickname, password):
        global b
        if nickname in self.users:
            if password == self.users[nickname]:
                print(f'Приветствую, {nickname}')
                self.current_user = self.users[nickname]
                b = 1
            else:
                print('Неверный пароль')
                b = 0
        else:
            print('Такого пользователя не существует')
            b = 0

    def register(self, nickname, password, age):
        user = User()
        user.add_user(nickname, password, age)
        self.users = {nickname: password}
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, video):
        self.videos.append(video.title)
        self.video_o.append(video)

    def get_video(self, search):
        global currentvid
        s = 0
        for i in self.videos:
            if search.lower() in i.lower():
                print(i)
                currentvid = i
                s += 1
        if s == 0:
            print('Ничего не найдено')

    def watch_video(self, title):
        for video in self.video_o:
            if video.title == title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Ты еще маленький для этого видео')
                    return
                for i in range(video.duration):
                    print(f'\rВидео проигрывается {i + 1} секунд...', end='')
                    time.sleep(1)
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200, False)
v2 = Video('Для чего девушкам парень программист?', 10, True)
ur.add(v1)
ur.add(v2)

while True:
    choice = int(input('Выберите действие:\n 1 — Вход \n 0 — регистрация \n'))
    if choice == 0:
        ur.register(input('Придумайте логин: '),input('Придумайте пароль: '),input('Сколько вам лет? '))
    if choice == 1:
        nickname = input('Введите логин: ')
        password = input('Введите пароль: ')
        ur.log_in(nickname, password)
        if b == 0:
            continue
    while True:
        a = input('Поиск видео: \nНаберите 9, чтобы выйти\n')
        if a == '9':
            ur.log_out()
            break
        ur.get_video(a)
        vid = int(input('Выбрать видео?\n 0 — поиск заново \n 1 — Да\n 9 — Выйти\n'))
        if vid == 0:
            continue
        if vid == 1:
            ur.watch_video(currentvid)
        if vid == 9:
            ur.log_out()
            break
