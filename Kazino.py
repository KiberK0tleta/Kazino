import pyautogui
import sys
import random
from colorama import *
import time

# from sqlalchemy import create_engine, func, Column, Integer, String, Text
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

start_time = time.time()

# Создаем подключение к базе данных
engine = create_engine("sqlite:///Kazino_Royale_DATA.db")

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# connection = sqlite3.connect("Kazino_Royale_DATA.db")
# cursor = connection.cursor()


# class Players:
#     def __init__(self, id, name, kingdom, balance, stavka, azart):
#         self.id = id
#         self.name = name
#         self.kingdom = kingdom
#         self.balance = balance
#         self.stavka = stavka  # комбинация
#         self.azart = azart


# player_1 = Players(1, "Артур", "Камелот", 10000, "", 70)
# player_2 = Players(2, "Гвиневра", "Камелот", 2000, "", 80)
# player_3 = Players(3, "Ланселот", "Камелот", 1500, "", 60)
# player_4 = Players(4, "Эльфрида", "Редания", 800, "", 70)
# player_5 = Players(5, "Тристан", "Камелот", 700, "", 60)
# player_6 = Players(6, "Изольда", "Цинтра", 500, "", 70)
# player_7 = Players(7, "Мерлин", "Нильфгаард", 1200, "", 50)
# player_8 = Players(8, "Галавант", "Редания", 1300, "", 70)
# player_9 = Players(9, "Розамунда", "Камелот", 1700, "", 60)
# player_10 = Players(10, "Эдвард", "Цинтра", 2100, "", 70)
# player_11 = Players(11, "Моргана", "Нильфгаард", 1100, "", 70)
# player_12 = Players(12, "Леонид", "Редания", 1500, "", 50)
# player_13 = Players(13, "Алина", "Камелот", 1800, "", 70)
# player_14 = Players(14, "Гаррет", "Цинтра", 2000, "", 90)
# player_15 = Players(15, "Элеонор", "Нильфгаард", 900, "", 70)
# player_16 = Players(16, "Исольда", "Редания", 1300, "", 80)
# player_17 = Players(17, "Борис", "Камелот", 1400, "", 70)
# player_18 = Players(18, "Ирина", "Цинтра", 2500, "", 60)
# player_19 = Players(19, "Константин", "Нильфгаард", 3000, "", 70)
# player_20 = Players(20, "Януарий", "Редания", 950, "", 70)
# player_21 = Players(21, "Валентин", "Камелот", 400, "", 70)
# player_22 = Players(22, "Ангелина", "Цинтра", 700, "", 70)
# player_23 = Players(23, "Донат", "Венгерберг", 550, "", 90)
# player_24 = Players(24, "Ангус", "Редания", 1600, "", 70)
# player_25 = Players(25, "Эльф", "Камелот", 2200, "", 70)
# player_26 = Players(26, "Октавия", "Йотунхейм", 10900, "", 50)
# player_27 = Players(27, "Даниэль", "Венгерберг", 1100, "", 50)
# player_28 = Players(28, "Лукия", "Редания", 1300, "", 40)
# player_29 = Players(29, "Севастьян", "Камелот", 1900, "", 70)
# player_30 = Players(30, "Анна", "Венгерберг", 2500, "", 70)


# players_list = [
#     player_1,
#     player_2,
#     player_3,
#     player_4,
#     player_5,
#     player_6,
#     player_7,
#     player_8,
#     player_9,
#     player_10,
#     player_11,
#     player_12,
#     player_13,
#     player_14,
#     player_15,
#     player_16,
#     player_17,
#     player_18,
#     player_19,
#     player_20,
#     player_21,
#     player_22,
#     player_23,
#     player_24,
#     player_25,
#     player_26,
#     player_27,
#     player_28,
#     player_29,
#     player_30,
# ]




# Работа с БД
Base = declarative_base()


# # Определяем класс модели для таблиц
class Igroki(Base):
    __tablename__ = "Игроки"

    id = Column("ID", Integer, primary_key=True)
    name = Column("Имя", Text)
    kingdom = Column("Королевство", Text)
    balance = Column("Баланс", Integer)
    azart = Column("Азарт", Integer)
    comment = Column("Комментарий", Text)


class Stavki_Rulet(Base):
    __tablename__ = "Ставки_на_рулетку"

    id = Column("ID", Integer, primary_key=True)
    table_number = Column("Номер_стола", Integer)
    name = Column("Игрок", Text)
    kingdom = Column("Королевство", Text)
    stavka = Column("Ставка", Integer)
    combination = Column("Комбинация", Text)
    sector = Column("Шарик_закатился_на_сектор", Text)
    stavka_win = Column("Ставка_Игрока_Зашла", Text)
    balance = Column("Текущий_Баланс_Рулетки", Integer)

class Rulet(Base):
    __tablename__ = "Рулетка"

    id = Column("ID", Integer, primary_key=True)
    table_number = Column("Номер_стола", Integer)
    start_balance = Column("Стартовый_Баланс", Integer)
    now_balance = Column("Текущий_Баланс", Integer)
    comment = Column("Комментарий", Text)
    results_of_day = Column("Итоги_дня", Integer)

class Avtomat(Base):
    __tablename__ = "Игровые_Автоматы"

    id = Column("ID", Integer, primary_key=True)
    avtomat_number = Column("Номер_автомата", Integer)
    start_balance = Column("Стартовый_Баланс", Integer)
    # start_balance = Column("Стартовый_Баланс", Integer, default=0)
    now_balance = Column("Текущий_Баланс", Integer)
    comment = Column("Комментарий", Text)
    results_of_day = Column("Итоги_дня", Integer)


class BANK(Base):
    __tablename__ = "Банк"

    id = Column("ID", Integer, primary_key=True)
    day = Column("День", Integer)
    avtomat_profit = Column("Доход_с_автоматов", Integer)
    ruletka_profit = Column("Доход_с_рулеток", Integer)
    results_of_day = Column("Итоги_дня", Integer)
    storage = Column("Хранилище", Integer)


class Debtors(Base):
    __tablename__ = "Должники"

    id = Column("ID", Integer, primary_key=True)
    day = Column("День", Integer)
    id_player = Column("ID_Игрока", Integer)
    name = Column("Имя", Text)
    kingdom = Column("Королевство", Text)
    duty = Column("Долг", Integer)
    comment = Column("Комментарий", Text)


class Winners(Base):
    __tablename__ = "Победители"

    id = Column("ID", Integer, primary_key=True)
    day = Column("День", Integer)
    id_player = Column("ID_Игрока", Integer)
    name = Column("Имя", Text)
    kingdom = Column("Королевство", Text)
    jackpot = Column("Джекпот", Integer)
    comment = Column("Комментарий", Text)


# Создаем таблицу
# Base.metadata.create_all(engine)


# table_name = "Игроки"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Рулетка"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Игровые_Автоматы"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Банк"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Должники"
# Base.metadata.tables[table_name].drop(engine)
# table_name = "Победители"
# Base.metadata.tables[table_name].drop(engine)





# Заполняем таблицу данными
# players_data = [
#     Igroki(id=1, name="Артур", kingdom="Камелот", balance=10000, combination="", azart=70, comment=""),
#     Igroki(id=2, name="Гвиневра", kingdom="Камелот", balance=2000, combination="", azart=80, comment=""),
#     Igroki(id=3, name="Ланселот", kingdom="Камелот", balance=1500, combination="", azart=60, comment=""),
#     Igroki(id=4, name="Эльфрида", kingdom="Редания", balance=800, combination="", azart=70, comment=""),
#     Igroki(id=5, name="Тристан", kingdom="Камелот", balance=700, combination="", azart=60, comment=""),
#     Igroki(id=6, name="Изольда", kingdom="Цинтра", balance=500, combination="", azart=70, comment=""),
#     Igroki(id=7, name="Мерлин", kingdom="Нильфгаард", balance=1200, combination="", azart=50, comment=""),
#     Igroki(id=8, name="Галавант", kingdom="Редания", balance=1300, combination="", azart=70, comment=""),
#     Igroki(id=9, name="Розамунда", kingdom="Камелот", balance=1700, combination="", azart=60, comment=""),
#     Igroki(id=10, name="Эдвард", kingdom="Цинтра", balance=2100, combination="", azart=70, comment=""),
#     Igroki(id=11, name="Моргана", kingdom="Нильфгаард", balance=1100, combination="", azart=70, comment=""),
#     Igroki(id=12, name="Леонид", kingdom="Редания", balance=1500, combination="", azart=50, comment=""),
#     Igroki(id=13, name="Алина", kingdom="Камелот", balance=1800, combination="", azart=70, comment=""),
#     Igroki(id=14, name="Гаррет", kingdom="Цинтра", balance=2000, combination="", azart=90, comment=""),
#     Igroki(id=15, name="Элеонор", kingdom="Нильфгаард", balance=900, combination="", azart=70, comment=""),
#     Igroki(id=16, name="Исольда", kingdom="Редания", balance=1300, combination="", azart=80, comment=""),
#     Igroki(id=17, name="Борис", kingdom="Камелот", balance=1400, combination="", azart=70, comment=""),
#     Igroki(id=18, name="Ирина", kingdom="Цинтра", balance=2500, combination="", azart=60, comment=""),
#     Igroki(id=19, name="Константин", kingdom="Нильфгаард", balance=3000, combination="", azart=70, comment=""),
#     Igroki(id=20, name="Януарий", kingdom="Редания", balance=950, combination="", azart=70, comment=""),
#     Igroki(id=21, name="Валентин", kingdom="Камелот", balance=400, combination="", azart=70, comment=""),
#     Igroki(id=22, name="Ангелина", kingdom="Цинтра", balance=700, combination="", azart=70, comment=""),
#     Igroki(id=23, name="Донат", kingdom="Венгерберг", balance=550, combination="", azart=90, comment=""),
#     Igroki(id=24, name="Ангус", kingdom="Редания", balance=1600, combination="", azart=70, comment=""),
#     Igroki(id=25, name="Эльф", kingdom="Камелот", balance=2200, combination="", azart=70, comment=""),
#     Igroki(id=26, name="Октавия", kingdom="Йотунхейм", balance=10900, combination="", azart=50, comment=""),
#     Igroki(id=27, name="Даниэль", kingdom="Венгерберг", balance=1100, combination="", azart=50, comment=""),
#     Igroki(id=28, name="Лукия", kingdom="Редания", balance=1300, combination="", azart=40, comment=""),
#     Igroki(id=29, name="Севастьян", kingdom="Камелот", balance=1900, combination="", azart=70, comment=""),
#     Igroki(id=30, name="Анна", kingdom="Венгерберг", balance=2500, combination="", azart=70, comment=""),
# ]
# session.add_all(players_data)

# ------------------------------------------------
# Удалить все записи
# session.query(Winners).delete()
# session.query(Igroki).delete()
# session.query(BANK).delete()
# session.query(Debtors).delete()

# Добавили записи Победителям
# try:
#     winner_update = Winners(id=0, day=0, id_player=-2, name="Test 1", kingdom="Neverland", jackpot=0, comment = "тестовый")
#     session.add(winner_update)
#     winner_update = Winners(id=-1, day=0, id_player=-1, name="Test 2", kingdom="Neverland", jackpot=0, comment = "тестовый")
#     session.add(winner_update)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# Добавили записи Должникам
# try:
#     debtor_update = Debtors(id=0, day=0, id_player=0, name="Test 1", kingdom="Neverland", duty = 1000, comment = "Не вернет")
#     session.add(debtor_update)
#     debtor_update = Debtors(id=1, day=0, id_player=1, name="Test 2", kingdom="Neverland", duty = 1000, comment = "Не вернет")
#     session.add(debtor_update)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# try:
#     for i in range(2, 11):
#         avtomat_update = Avtomat(id=i, avtomat_number=i, start_balance=0, now_balance = 0, comment = "", results_of_day = 0)
#         session.add(avtomat_update)

#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")


# try:
#     for i in range(1, 11):
#         rulet_update = Rulet(id=i, table_number=i, start_balance=10000, now_balance = 0, comment = "", results_of_day = 0)
#         session.add(rulet_update)

#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# Добавили записи Банку
# try:
#     bank_update_start = BANK(
#         id=0,
#         day=0,
#         avtomat_profit=0,
#         ruletka_profit=0,
#         results_of_day=0,
#         storage=10000,
#     )
#     session.add(bank_update_start)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# Список для игроков
# players_list = []
# names = ["Артур", "Ланселот", "Гвиневра", "Мерлин", "Изольда", "Тристан", "Персиваль", "Морган", "Галахад", "Гавейн", "Элоуэн", "Элиан", "Игрейна", "Герайнт", "Гавейн", "Моргана", "Гахерис", "Нимуэ", "Агравейн", "Моргауза", "Тристан", "Игрена", "Бедивер", "Элейна", "Леонтес", "Вивьен", "Элен", "Утер", "Этельстан", "Изолт", "Игрейна", "Лоэнгрин", "Раньель", "Галахальт", "Диндран", "Борс", "Моргауз", "Гвендолин", "Мордред", "Гвейн", "Саграмор", "Карадок", "Селидант", "Динас", "Гахариет", "Гавен", "Липпи", "Абелард", "Бекет", "Колман", "Изабо", "Элоиза", "Игрейн", "Женевьева", "Говен", "Изолт", "Рианнон", "Диндрана", "Серидвен", "Элен", "Раньель", "Вивиан", "Бланшфлер", "Эсклармонда", "Айбрик", "Мэлори", "Изольда", "Изоуд", "Борс", "Бедвир", "Кай", "Кулхч", "Эктор", "Горлойс", "Гвальчмей", "Гвин", "Иорверт", "Уриен", "Ивен", "Персиваль", "Пеллеас", "Паламед", "Леодегран", "Ллачеу", "Карадок", "Галахад", "Кей", "Увайн", "Ронабви", "Бреунор", "Мирддин", "Рис", "Бледдри", "Кол", "Эдейрн", "Элиан", "Эмир", "Морфран", "Падарн", "Тегир"
#         "Янита", "Йоханна", "Таисия", "Жаклин", "Диана", "Федосья", "Фаина", "Цвета", "Зоя", "Анастасия", "Галина", "Жаклин", "Елизавета", "Шарлота", "Злата", "Лидия", "Чеслава", "Цилла", "Федосья", "Гелла", "Диана", "Фаина", "Лидия", "Цилла", "Алёна", "Зоя", "Янита", "Зоя", "Беатриса", "Шушана", "Оксана", "София", "Прасковья", "Изольда", "Розалина", "Беатриса", "Яна", "Устинья", "Йосифа", "Цвета", "Евгения", "Жаклин", "София", "Злата", "Христина", "Янита", "Янита", "Антонина", "Майя", "Таисия", "Ульяна", "Ольга", "Ульяна", "Яна", "Беатриса", "Ольга", "Яна", "Юна", "София", "Злата", "Ульяна", "Эльвира", "Марина", "Оксана", "Диана", "Регина", "Цилла", "Шушана", "Алла", "Злата", "Янита", "Гертруда", "Зинаида", "Злата", "Чечилия", "Зинаида", "Алёна", "Шушана", "Надежда", "Злата", "Йана", "Злата", "Эллада", "Лидия", "Варвара", "Таисия", "Федосья", "Элина", "Регина", "Майя", "Эльвира", "Йоланта", "Регина", "Зоя", "Цара", "Надежда", "Оксана", "Злата", "Евгения", "Борислава", "Гюзель", "Наталья", "Ждан", "Семён", "Платон", "Олег", "Прохор", 
#         "Роман", "Устин", "Никодим", "Руслан", "Ярослав", "Родион", "Роман", "Илья", "Эдуард", "Степан", "Фёдор", "Юрий", "Фёдор", "Роберт", "Марат", "Ярослав", "Шерлок", "Пётр", "Сава", "Иосиф", "Никодим", "Йоган", "Марат", "Иосиф", "Бронислав", "Тит", "Борис", "Жерар", "Устин", "Ираклий", "Йоханес", "Борис", "Ждан", "Юлий", "Бронислав", "Устин", "Закир", "Всеволод", "Роберт", "Родион", "Цефас", "Трофим", "Роман", "Богдан", "Евсей", "Тимур", "Альберт", "Трофим", "Фёдор", "Эрик", "Шарль", "Огюст", "Ждан", "Донат", "Семён", "Цефас", "Роман", "Ярослав", "Борис", "Гордей", "Эрик", "Емельян", "Йосып", "Гордей", "Емельян", "Герасим", "Кузьма", "Закир", "Кузьма", "Борис", "Леопольд", "Орест", "Ефим", "Шерлок", "Ждан", "Бронислав", "Заур", "Ярослав", "Феликс", "Игнатий", "Савва", "Семён", "Тимофей", "Роберт", "Марат", "Прохор", "Кузьма", "Огюст", "Жигер", "Устин", "Шамиль", "Вячеслав", "Сава", "Цицерон", "Жерар", "Шамиль", "Ян", "Эрик", "Богдан", "Феликс", "Сергей", "Йоханес", "Чеслав", "Харитон", "Родион", "Тит", "Тимофей", "Цицерон", "Шерлок", 
#         "Устин", "Жерар", "Жигер", "Орест", "Закир", "Харитон", "Фёдор", "Ефим", "Йоханес", "Тит", "Огюст", "Лев", "Мирослав", "Радислав", "Борис", "Никодим", "Чеслав", "Фёдор", "Тимур", "Йосып", "Жерар", "Платон", "Лукьян", "Шарль", "Семён", "Илларион", "Лев", "Богдан", "Харитон", "Назар", "Лев", "Харитон", "Леон", "Тимофей", "Шерлок", "Тарас", "Пётр", "Ярослав", "Эдуард", "Цефас", "Йоханес", "Устин", "Фёдор", "Болеслав", "Прохор", "Вадим", "Стефан", "Харитон", "Эрик", "Вадим", "Прохор", "Огюст", "Еремей", "Тит", "Закир", "Шерлок", "Тимофей", "Вадим", "Евдоким", "Ярослав", "Бронислав", "Илья", "Марат", "Марат", "Вадим", "Устин", "Юлий", "Игнат", "Шерлок", "Борис", "Ярослав", "Устин", "Бронислав", "Тимур", "Феликс", "Цефас", "Валерий", "Глеб", "Мирослав", "Жерар", "Жерар", "Кузьма", "Фёдор", "Марат", "Людовик", "Руслан", "Филипп", "Лукьян", "Йоханес", "Фёдор", "Прохор", "Ярослав", "Харитон", "Михаил", "Лев", "Андрей", "Осип", "Ярослав", "Шерлок", "Эдуард", "Юрий", "Шарль", "Тит", "Ярослав", "Ираклий", "Чарльз", "Устин", "Ян", "Харитон", "Йомер", 
#         "Артём", "Огюст", "Тит", "Матвей", "Семён", "Мирослав", "Эрик", "Йоханес", "Геннадий", "Оскар", "Добрыня", "Устин", "Феликс", "Эрик", "Станислав", "Данила", "Зенон", "Йоган", "Еремей", "Трофим", "Руслан", "Йоган", "Данила", "Лукиллиан", "Фёдор", "Геннадий", "Фёдор", "Камиль", "Чеслав", "Устин", "Станислав", "Добрыня", "Фёдор", "Борис", "Йоханес", "Цицерон", "Людовик", "Цефас", "Герман", "Валериан", "Гарри", "Жигер", "Сергей", "Максим", "Конрад", "Йозеф", "Святослав", "Никодим", "Добрыня", "Оскар" ]
# kingdoms = ["Камелот", "Редания", "Цинтра", "Венгерберг", "Нильфгаард"]

# try:
#     # Создаём 100 игроков
#     for i in range(1, 401):

#     # while not Exception:

#         generate_name = random.choice(names)
#         names.remove(generate_name)
#         generate_balance = random.randint(1, 100) * (random.randint(1, 10) * 100) * 10
#         generate_kingdom = random.choice(kingdoms)

#         player = Igroki(id = i, name=generate_name, kingdom=generate_kingdom, balance=generate_balance, azart=70, comment="")
#         players_list.append(player)
#         # print(generate_name)

#     session.add_all(players_list)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")



# ------------------------------------------------


# Берем из Хранилища стартовый баланс для каждого автомата и рулетки
Avtomat_1_BANK = 0
Avtomat_now_balance = 0
Avtomat_1 = (
    session.query(Avtomat).filter_by(avtomat_number=1).first()
)  # в этой переменной тперь значение из БД
try:
    Avtomat_now_balance = Avtomat_1.start_balance  # = 10 000
    # Сразу же вычитаем из Хранилища эту сумму
    max_value = session.query(func.max(BANK.storage)).scalar()
    start_mony = session.query(BANK).filter_by(storage=max_value).first()
    start_mony.storage -= Avtomat_1.start_balance

except Exception as e:
    print(f"Произошла ошибка: {e}")
# session.commit()




# Берем из Хранилища стартовый баланс для рулетки
Ruletka_1_BANK = 0
Ruletka_now_balance = 0
Ruletka_1 = (
    session.query(Rulet).filter_by(table_number=1).first()
)
try:
    Ruletka_now_balance = Ruletka_1.start_balance  # = 10 000
    # Сразу же вычитаем из Хранилища эту сумму
    max_value = session.query(func.max(BANK.storage)).scalar()
    start_mony = session.query(BANK).filter_by(storage=max_value).first()
    start_mony.storage -= Ruletka_1.start_balance

except Exception as e:
    print(f"Произошла ошибка: {e}")





# Ищем последний день
n_day = 0
try:
    max_day_subquery = session.query(func.max(BANK.day)).as_scalar()
    bank_buffer = session.query(BANK).filter(BANK.day == max_day_subquery).first()
    n_day = bank_buffer.day + 1
    print(f"\n\nБанк день: {n_day}, хранилище: {bank_buffer.storage}\n\n")
except Exception as e:
    print(f"Произошла ошибка(bank_buffer): {e}")


n_winner_id = 0
try:
    max_value = session.query(func.max(Winners.id)).scalar()
    winners_buffer = session.query(Winners).filter_by(id=max_value).first()
    # winners_buffer = session.query(Winners).filter(Winners.id == func.max(Winners.id)).first()
    n_winner_id = winners_buffer.id + 1
    print(f"\n\nПобедители(поиск id): ID: {n_winner_id}\n\n")
except Exception as e:
    print(f"Победители(поиск id): Произошла ошибка: {e}")







# ----------------------------------------------------------------------------------------------------------
class Stol_Ruletka:
    def __init__(self, id, count_players_now, bank):
        self.id = id
        self.count_players_now = count_players_now
        self.bank = bank


Table_1 = Stol_Ruletka(1, 0, 10000)
Table_2 = Stol_Ruletka(2, 0, 10000)
Table_3 = Stol_Ruletka(3, 0, 10000)


class Stavki_na_Ruletky:
    def __init__(self, n, color, amount, player_name, combo):
        self.n = n
        self.color = color
        self.amount = amount  # количество поставленных денег
        self.player_name = player_name  # имя игрока
        self.combo = combo  # комбинация ставок


n_0 = Stavki_na_Ruletky(0, "ZERO", 0, "", {})
n_1 = Stavki_na_Ruletky(1, "red", 0, "", {})
n_2 = Stavki_na_Ruletky(2, "red", 0, "", {})
n_3 = Stavki_na_Ruletky(3, "red", 0, "", {})
n_4 = Stavki_na_Ruletky(4, "black", 0, "", {})
n_5 = Stavki_na_Ruletky(5, "red", 0, "", {})
n_6 = Stavki_na_Ruletky(6, "black", 0, "", {})
n_7 = Stavki_na_Ruletky(7, "red", 0, "", {})
n_8 = Stavki_na_Ruletky(8, "black", 0, "", {})
n_9 = Stavki_na_Ruletky(9, "red", 0, "", {})
n_10 = Stavki_na_Ruletky(10, "black", 0, "", {})
n_11 = Stavki_na_Ruletky(11, "black", 0, "", {})
n_12 = Stavki_na_Ruletky(12, "red", 0, "", {})
n_13 = Stavki_na_Ruletky(13, "black", 0, "", {})
n_14 = Stavki_na_Ruletky(14, "red", 0, "", {})
n_15 = Stavki_na_Ruletky(15, "black", 0, "", {})
n_16 = Stavki_na_Ruletky(16, "red", 0, "", {})
n_17 = Stavki_na_Ruletky(17, "black", 0, "", {})
n_18 = Stavki_na_Ruletky(18, "red", 0, "", {})
n_19 = Stavki_na_Ruletky(19, "red", 0, "", {})
n_20 = Stavki_na_Ruletky(20, "black", 0, "", {})
n_21 = Stavki_na_Ruletky(21, "red", 0, "", {})
n_22 = Stavki_na_Ruletky(22, "black", 0, "", {})
n_23 = Stavki_na_Ruletky(23, "red", 0, "", {})
n_24 = Stavki_na_Ruletky(24, "black", 0, "", {})
n_25 = Stavki_na_Ruletky(25, "red", 0, "", {})
n_26 = Stavki_na_Ruletky(26, "black", 0, "", {})
n_27 = Stavki_na_Ruletky(27, "red", 0, "", {})
n_28 = Stavki_na_Ruletky(28, "black", 0, "", {})
n_29 = Stavki_na_Ruletky(29, "black", 0, "", {})
n_30 = Stavki_na_Ruletky(30, "red", 0, "", {})
n_31 = Stavki_na_Ruletky(31, "black", 0, "", {})
n_32 = Stavki_na_Ruletky(32, "red", 0, "", {})
n_33 = Stavki_na_Ruletky(33, "black", 0, "", {})
n_34 = Stavki_na_Ruletky(34, "red", 0, "", {})
n_35 = Stavki_na_Ruletky(35, "black", 0, "", {})
n_36 = Stavki_na_Ruletky(36, "red", 0, "", {})
new_stavka = Stavki_na_Ruletky(-1, "null", 0, "", {})


Stavka_list = [
    n_0,
    n_1,
    n_2,
    n_3,
    n_4,
    n_5,
    n_6,
    n_7,
    n_8,
    n_9,
    n_10,
    n_11,
    n_12,
    n_13,
    n_14,
    n_15,
    n_16,
    n_17,
    n_18,
    n_19,
    n_20,
    n_21,
    n_22,
    n_23,
    n_24,
    n_25,
    n_26,
    n_27,
    n_28,
    n_29,
    n_30,
    n_31,
    n_32,
    n_33,
    n_34,
    n_35,
    n_36,
]


# print(f"-----------------------------------------------------\n\n\n")


# def Serch_active_players():
#     Active_player = random.randint(1, 10)

#     # Ищите игрока с соответствующим id
#     active_player = None
#     for p in players_list:
#         if p.id == Active_player:
#             active_player = p
#             break
#     if active_player.balance <= 2:
#         Serch_active_players()

#     return active_player





# def load_players_from_db():
#     players = session.query(Igroki).filter(Igroki.balance > 100).all()
#     return players

# Igroki_list = load_players_from_db()

Igroki_FULL_list = session.query(Igroki).all()
Igroki_list = [player for player in Igroki_FULL_list if player.balance > 100]

def Serch_active_players():
    try:
        active_player = random.choice(Igroki_list)
        active_player.azart = 70
        return active_player
    except Exception as e:
        print(f"Произошла ошибка(поиск играков): {e}")
        return None



# def Serch_active_players():
#     try:
#         # Выбираем случайного игрока с балансом больше 2
#         active_player = (
#             session.query(Igroki)
#             .filter(Igroki.balance > 2)
#             .order_by(func.random())
#             .first()
#         )
#         if not active_player:
#             return None # Если не нашли игрока, возвращаем None
#         active_player.azart = 70
#         return active_player
#     except Exception as e:
#         print(f"Произошла ошибка(поиск играков): {e}")
#         return None

# TODO: Додумать количество ставки которое делает игрок
def count_Stavka():
    try:
        # new_stavka.amount = random.randint(1, player.balance - 1)
        if player.balance <= 0:
            Dolg()
        if player.azart >= 50:
            # Сделать большую ставку 30-50%
            min_stavka = int(player.balance * 0.3)
            max_stavka = int(player.balance * 0.8)
            new_stavka.amount = random.randint(min_stavka, max_stavka)
        elif player.azart < 50 and player.azart >= 40:
            # Сделать большую ставку 10-30%
            min_stavka = int(player.balance * 0.1)
            max_stavka = int(player.balance * 0.3)
            new_stavka.amount = random.randint(min_stavka, max_stavka)
        else:
            # Сделать меньшую ставку 3-10%
            min_stavka = int(player.balance * 0.03)
            max_stavka = int(player.balance * 0.1)
            new_stavka.amount = random.randint(min_stavka, max_stavka)
    except:
        print(
            Fore.RED
            + f"------------------------------------------------------------   У НАС ПОЯВИЛСЯ ДОЛЖНИК   ------------------------------------------------------------ "
            + Style.RESET_ALL
        )
        Dolg()
        count_Stavka()
        # new_stavka.amount = random.randint(1, player.balance - 1)



Variant_of_stavka = {
    1: {  # Шас 5%
        "name": "Straight Bet",
        "money": 0,
        "comment": "Вы ставите на одно конкретное число. Выигрыш выплачивается 35:1.",
        "win": 35,
    },
    2: {  # Шас 5%
        "name": "Zero Bet",
        "money": 0,
        "comment": "Вы ставите на ноль. Выигрыш выплачивается 35:1.",
        "win": 35,
    },
    4: {  # Шас 10%
        "name": "Street Bet",
        "money": 0,
        "comment": "Вы ставите на вертикальный ряд из трех чисел. Выигрыш выплачивается 11:1.",
        "win": 11,
    },
    5: {  # Шас 10%
        "name": "Line Bet",
        "money": 0,
        "comment": "Вы ставите на два вертикальных ряда, образуя шесть чисел. Выигрыш выплачивается 5:1.",
        "win": 5,
    },
    6: {  # Шас 20%
        "name": "Red/Black Bet",
        "money": 0,
        "comment": "Вы ставите на цвет ячейки. Выигрыш выплачивается 1:1.",
        "win": 1,
    },
    8: {  # Шас 20%
        "name": "1-18 or 19-36 Bet",
        "money": 0,
        "comment": "Вы ставите на диапазон чисел (1-18 или 19-36). Выигрыш выплачивается 1:1.",
        "win": 1,
    },
    9: {  # Шас 20%
        "name": "Column Bet",
        "money": 0,
        "comment": "Вы ставите на один из трех горизонтальных столбцов с числами. Выигрыш выплачивается 2:1.",
        "win": 2,
    },
    10: {  # Шас 10%
        "name": "Dozen Bet",
        "money": 0,
        "comment": "Вы ставите на одну из трех дюжин чисел (1-12, 13-24, 25-36). Выигрыш выплачивается 2:1.",
        "win": 2,
    },
    # ------------------------------
    7: {  # не буду использовать
        "name": "Even/Odd Bet",
        "money": 0,
        "comment": "Вы ставите на то, будет ли выпавшее число четным или нечетным. Выигрыш выплачивается 1:1.",
        "win": 1,
    },
    13: {  # не буду использовать
        "name": "Split Bet",
        "money": 0,
        "comment": "Вы ставите на линию между двумя соседними числами. Выигрыш выплачивается 17:1.",
        "win": 17,
    },
    3: {  # не буду использовать
        "name": "Corner Bet",
        "money": 0,
        "comment": "Вы ставите на угол, образованный четырьмя соседними числами. Выигрыш выплачивается 8:1.",
        "win": 8,
    },
}

# 3 по вертикали
street_bets = {
    1: [n_1, n_2, n_3],
    2: [n_4, n_5, n_6],
    3: [n_7, n_8, n_9],
    4: [n_10, n_11, n_12],
    5: [n_13, n_14, n_15],
    6: [n_16, n_17, n_18],
    7: [n_19, n_20, n_21],
    8: [n_22, n_23, n_24],
    9: [n_25, n_26, n_27],
    10: [n_28, n_29, n_30],
    11: [n_31, n_32, n_33],
    12: [n_34, n_35, n_36],
}

# Вы ставите на один из трех горизонтальных столбцов с числами
column_bets = {
    1: [n_1, n_4, n_7, n_10, n_13, n_16, n_19, n_22, n_25, n_28, n_31, n_34],
    2: [n_2, n_5, n_8, n_11, n_14, n_17, n_20, n_23, n_26, n_29, n_32, n_35],
    3: [n_3, n_6, n_9, n_12, n_15, n_18, n_21, n_24, n_27, n_30, n_33, n_36],
}

# Вы ставите на одну из трех дюжин чисел (1-12, 13-24, 25-36)
dozen_bets = {
    1: [n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12],
    2: [n_13, n_14, n_15, n_16, n_17, n_18, n_19, n_20, n_21, n_22, n_23, n_24],
    3: [n_25, n_26, n_27, n_28, n_29, n_30, n_31, n_32, n_33, n_34, n_35, n_36],
}


def Stavka_na_Ruletky():
    global new_stavka
    stavka_colour = "null"
    colour_win = "dfvbaes"
    player_win = false
    WIN = 0

    player_chose = random.randint(1, 100)
    # player_chose = 75

    if player_chose <= 5:
        Scenarios = Variant_of_stavka[1]
        new_stavka = random.choice(Stavka_list)  # тут он ставит на рандомное поле

    elif player_chose > 5 and player_chose <= 10:
        Scenarios = Variant_of_stavka[2]
        new_stavka = n_0  # тут он ставит на ZERO

    elif player_chose > 10 and player_chose <= 20:
        Scenarios = Variant_of_stavka[4]
        key = random.choice(list(street_bets.keys()))
        new_stavka.combo = street_bets[key]
        # Вы ставите на вертикальный ряд из трех чисел. Выигрыш выплачивается 11:1

    elif player_chose > 20 and player_chose <= 30:
        Scenarios = Variant_of_stavka[5]
        key = random.choice(list(street_bets.keys()))
        if key == 12:
            new_stavka.combo = street_bets[key] + street_bets[key - 1]
        else:
            new_stavka.combo = street_bets[key] + street_bets[key + 1]
        # Вы ставите на два вертикальных ряда, образуя шесть чисел. Выигрыш выплачивается 5:1

    elif player_chose > 30 and player_chose <= 50:
        Scenarios = Variant_of_stavka[6]
        stavka_colour = random.choice(["red", "black"])
        # Вы ставите на цвет ячейки. Выигрыш выплачивается 1:1

    elif player_chose > 50 and player_chose <= 70:
        Scenarios = Variant_of_stavka[8]
        new_stavka = random.choice(Stavka_list)
        # Вы ставите на диапазон чисел (1-18 или 19-36). Выигрыш выплачивается 1:1

    elif player_chose > 70 and player_chose <= 90:
        Scenarios = Variant_of_stavka[9]
        key = random.choice(list(column_bets.keys()))
        new_stavka.combo = column_bets[key]
        # Вы ставите на один из трех горизонтальных столбцов с числами. Выигрыш выплачивается 2:1

    elif player_chose > 90 and player_chose <= 100:
        Scenarios = Variant_of_stavka[10]
        key = random.choice(list(dozen_bets.keys()))
        new_stavka.combo = dozen_bets[key]
        # Вы ставите на одну из трех дюжин чисел (1-12, 13-24, 25-36). Выигрыш выплачивается 2:1

    else:
        print(f"Игрок ОТКАЗАЛСЯ ИГРАТЬ")

    # Крутится рулетка
    Ruletka_go = random.randint(0, 36)
    for n_instance in Stavka_list:
        if Ruletka_go == n_instance.n:
            colour_win = n_instance.color
            break

    #   ТЕСТИМ  ----------------------------------------------------
    # Scenarios = Variant_of_stavka[10]

    # print(f"Сценарий: {Scenarios['name'], Scenarios['comment']}")

    # тут считается величина ставки
    count_Stavka()
    # try:
    #     new_stavka.amount = random.randint(1, player.balance - 1)
    # except:
    #     print(
    #         Fore.RED
    #         + f"------------------------------------------------------------   ОПЯТЬ КАКАЯ ТО ХРЕНЬ С РАНДОМОМ БАЛАНСА   ------------------------------------------------------------ "
    #         + Style.RESET_ALL
    #     )
    #     Dolg()
    #     new_stavka.amount = random.randint(1, player.balance - 1)

    # print(
    #     f"{player.id}, {player.name}, Королевство: {player.kingdom}, Баланс: {player.balance}"
    # )
    # print(
    #     "Ставка: "
    #     + Fore.YELLOW
    #     + str(new_stavka.amount)
    #     + Style.RESET_ALL
    #     + " золотых на:"
    # )

    if Scenarios == Variant_of_stavka[1] or Scenarios == Variant_of_stavka[2]:
        # print(f"<{new_stavka.n} {new_stavka.color}>")
        if Ruletka_go == new_stavka.n:
            WIN = 1      
    # elif Scenarios == Variant_of_stavka[4]:
    #     print(
    #         f"<{new_stavka.combo[0].n} {new_stavka.combo[0].color}> ИЛИ <{new_stavka.combo[1].n} {new_stavka.combo[1].color}> ИЛИ <{new_stavka.combo[2].n} {new_stavka.combo[2].color}>"
    #     )
    # elif Scenarios == Variant_of_stavka[5]:
    #     print(
    #         f"Cтолбец <{new_stavka.combo[0].n} {new_stavka.combo[0].color}, {new_stavka.combo[1].n} {new_stavka.combo[1].color}, {new_stavka.combo[2].n} {new_stavka.combo[2].color}> И <{new_stavka.combo[3].n} {new_stavka.combo[3].color}, {new_stavka.combo[4].n} {new_stavka.combo[4].color}, {new_stavka.combo[5].n} {new_stavka.combo[5].color}> "
    #     )
    elif Scenarios == Variant_of_stavka[6]:
        # if stavka_colour == "red":
        #     print("КРАСНОЕ")

        # else:
        #     print("ЧЕРНОЕ")
        if stavka_colour == colour_win:
            WIN = 1
    elif Scenarios == Variant_of_stavka[8]:
        if new_stavka.n > 0 and new_stavka.n <= 18:
            # print("НА ЧИСЛА ОТ 1 ДО 18")
            if Ruletka_go > 0 and Ruletka_go <= 18:
                WIN = 1
        else:
            # print("НА ЧИСЛА ОТ 19 ДО 36")
            if Ruletka_go > 18:
                WIN = 1
    # elif Scenarios == Variant_of_stavka[9]:
    #     print(
    #         f"<{new_stavka.combo[0].n} {new_stavka.combo[0].color}> ИЛИ <{new_stavka.combo[1].n} {new_stavka.combo[1].color}> ИЛИ <{new_stavka.combo[2].n} {new_stavka.combo[2].color}> ИЛИ <{new_stavka.combo[3].n} {new_stavka.combo[3].color}> ИЛИ <{new_stavka.combo[4].n} {new_stavka.combo[4].color}> ИЛИ <{new_stavka.combo[5].n} {new_stavka.combo[5].color}> ИЛИ <{new_stavka.combo[6].n} {new_stavka.combo[6].color}> ИЛИ <{new_stavka.combo[7].n} {new_stavka.combo[7].color}> ИЛИ <{new_stavka.combo[8].n} {new_stavka.combo[8].color}> ИЛИ <{new_stavka.combo[9].n} {new_stavka.combo[9].color}> ИЛИ <{new_stavka.combo[10].n} {new_stavka.combo[10].color}> ИЛИ <{new_stavka.combo[11].n} {new_stavka.combo[11].color}>"
    #     )
    # elif Scenarios == Variant_of_stavka[10]:
    #     if new_stavka.combo[0].n >= 1 and new_stavka.combo[0].n <= 12:
    #         print("ДЮЖИНУ (1 - 12)")
    #     elif new_stavka.combo[0].n >= 13 and new_stavka.combo[0].n <= 24:
    #         print("ДЮЖИНУ (13 - 24)")
    #     else:
    #         print("ДЮЖИНУ (25 - 36)")
    # else:
    #     print(f"ERROR>")

    # print(
    #     Style.RESET_ALL
    #     + f"Шарик закатился на сектор: "
    #     + Fore.BLUE
    #     + f"{n_instance.n} {n_instance.color}"
    #     + Style.RESET_ALL
    # )

    # Пошла проверка на совпадение хотябы 1 из комбинации
    if Ruletka_go in [n.n for n in new_stavka.combo] or WIN == 1:
        # print(
        #     Fore.RED
        #     + f"ВАМ ПОВЕЗЛО!\n"
        #     + Fore.GREEN
        #     + f"Его баланс: {player.balance} + {new_stavka.amount*Scenarios['win']} = {player.balance + new_stavka.amount*Scenarios['win']}"
        # )
        player.balance += new_stavka.amount * Scenarios["win"]
        Table_1.bank -= new_stavka.amount * Scenarios["win"]
        # print(
        #     Style.RESET_ALL
        #     + f"\n-----------------------------------------------------\n"
        # )
        player.azart += 10
        player_win = True
    else:
        # print(f"Значение Рулетки не совпало с значениями в ряду")
        player.balance -= new_stavka.amount
        Table_1.bank += new_stavka.amount
        player.azart -= 10

    # print(f"Азаарт игрока: {player.azart}\n")
    if player_win == True:
        player.azart -= 30

    if player_win == False:
        if new_stavka.amount >=100 and new_stavka.amount <=200:
            player.azart += 1
        elif new_stavka.amount >200 and new_stavka.amount <=500:
            player.azart += 2
        elif new_stavka.amount >=500 and new_stavka.amount <=2000:
            player.azart += 5
        elif new_stavka.amount >2000 and new_stavka.amount <=10000:
            player.azart += 10
        elif new_stavka.amount >10000 and new_stavka.amount <=50000:
            player.azart += 20
        elif new_stavka.amount >50000:
            player.azart -= 20
        else:
            player.azart -= 3

    if player.azart > 30:
        Stavka_na_Ruletky()





winning_combinations = {
    1: {
        "combo": [9, 3, 9],
        "win": 5,
    },
    2: {
        "combo": [3, 2, 1],
        "win": 5,
    },
    3: {
        "combo": [10, 9, 8],
        "win": 2,
    },
    4: {
        "combo": [3, 2, 3],
        "win": 3,
    },
    5: {
        "combo": [4, 3, 4],
        "win": 3,
    },
}

jackpot_list = {
    1: "Выйгрыш х2",
    2: "Выйгрыш х10",
    3: "МЕГА Джекпот",
    10: "Игрок сорвал БАНК",
}


# Создаем барабаны с числами от 1 до 10
Baraban_1 = [i for i in range(1, 11)]
# Baraban_2 = [i for i in range(1, 11)]
# Baraban_3 = [i for i in range(1, 11)]

def Baraban_GO():
    result = []
    for _ in range(3):  # Вращаем три барабана
        result.append(random.choice(Baraban_1))

    # Выводим результат
    # print(f"Результат: {result[0]} | {result[1]} | {result[2]}")
    return result


exits = 0
win_combo = 0

def Stavka_on_Baraban():
    global exits
    global Avtomat_now_balance
    global Avtomat_1_BANK
    global win_combo

    count_win_info = 0
    win = False
    win_combo = 0
    # тут считается величина ставки
    new_stavka.amount = random.choice([5, 10, 50, 100])

    # print(
    #     f"{player.id}, {player.name}, Королевство: {player.kingdom}, Баланс: {player.balance}"
    # )
    # print("Ставка: " + Fore.YELLOW + f"{new_stavka.amount} золотых" + Style.RESET_ALL)

    result = Baraban_GO()

    if (result[0] + 1 == result[1]) and (result[1] + 1 == result[2]):
        win = True
        win_combo = 1
    elif all(x == 7 for x in result):
        win = True
        win_combo = 3
        print(
            Fore.RED
            + f"////////////////////////////  --- МЕГА ДЖЕКПОТ ---  ////////////////////////////"
            + Style.RESET_ALL
        )
    elif result[0] == result[1] == result[2] and Avtomat_now_balance >= 100000:
        win = True
        win_combo = 10
        Avtomat_1_BANK += 50000
        Avtomat_now_balance -= 50000
        # exits = 1

    elif result[0] == result[1] == result[2]:
        win = True
        win_combo = 2

    for combination in winning_combinations.values():
        if result == combination["combo"] or win == True:
            if win_combo == 1:
                combination["win"] = 2
            elif win_combo == 2:
                combination["win"] = 10
            elif win_combo == 3:
                combination["win"] = 100
            elif win_combo == 10:
                combination["win"] = 1
                print(Fore.BLUE + f"\t\t\tИгрок сорвал БАНК!" + Style.RESET_ALL)
                # time.sleep(3)
                player.balance += 30000
                Avtomat_now_balance -= 30000
                count_win_info = 30000

            player.balance += new_stavka.amount * combination["win"]
            Avtomat_now_balance -= new_stavka.amount * combination["win"]
            count_win_info += new_stavka.amount * combination["win"]

            # print(
            #     f"Выйгрыш х{combination['win']}: {new_stavka.amount} * {combination['win']} = {new_stavka.amount * combination['win']}"
            # )
            # print(
            #     Fore.RED
            #     + f"Вы выиграли! Новый баланс: {player.balance}"
            #     + Style.RESET_ALL
            # )
            win = True
            break

    if win == False:
        player.balance -= new_stavka.amount
        Avtomat_now_balance += new_stavka.amount
        # print(f"Вы проиграли. Новый баланс: {player.balance}")

        if new_stavka.amount == 5:
            player.azart -= 1
        elif new_stavka.amount == 10:
            player.azart -= 2
        elif new_stavka.amount == 50:
            player.azart -= 5
        elif new_stavka.amount == 100:
            player.azart -= 10

        # print(f"Азарт: {player.azart}")
    # print(f"Баланс АВТОМАТА: {Avtomat_now_balance}\n")
    global n_winner_id
    if win_combo == 3 or win_combo == 10:
        try:
            wnners_update = Winners(
                id=n_winner_id,
                day=n_day,
                id_player=player.id,
                name=player.name,
                kingdom=player.kingdom,
                jackpot=count_win_info,
                comment=jackpot_list[win_combo],
            )
            n_winner_id += 1
            session.add(wnners_update)
            session.commit()
        except Exception as e:
            print(f"Победители(заполнение): Произошла ошибка: {e}") 

    if player.azart > 30:
        Stavka_on_Baraban()


print(f"НАЧАЛО ИГРЫ:\n")


# print(
#     f"Баланс стола: " + Fore.YELLOW + str(Table_1.bank) + Style.RESET_ALL + " золотых"
# )


# print(f"ИТОГИ:\n")
# print(
#     f"Баланс стола: " + Fore.YELLOW + str(Table_1.bank) + Style.RESET_ALL + " золотых"
# )

# try:
#     wnners_update = Winners(
#             id=2,
#             day=2,
#             id_player=2,
#             name="sdfb",
#             kingdom="svbdbdbfgnrst",
#             jackpot=0,
#             comment="bsnfntnrsns",
#         )
#     session.add(wnners_update)
#     session.commit()
# except Exception as e:
#     print(f"Произошла ошибка: {e}")





# bank_max_day = session.query(func.max(BANK.day)).scalar()
# bank_buffer = session.query(BANK).filter_by(day=func.max(BANK.day)).first()

n = 0
# have_Dolg = false
list_of_debtors = {}
def Dolg():

    player.balance += 1000
    try:
        max_value = session.query(func.max(Debtors.id)).scalar()
        max_Deb_id = session.query(Debtors).filter_by(id=max_value).first()
    except Exception as e:
        print(f"Должник: Произошла ошибка: {e}")
    # max_Deb_id.id += 1

    # НОВЫЙ должник
    new_debtor = {
        "id_player": player.id,
        "name": player.name,
        "money": 1000,
        "kingdom": player.kingdom
    }

    # список должников + НОВЫЙ должник
    list_of_debtors[max_Deb_id.id + 1] = new_debtor
    try:
        debtor_update = Debtors(
            id=max_Deb_id.id + 1,
            day = 0,
            id_player = new_debtor["id_player"],
            name=new_debtor["name"],
            kingdom=new_debtor["kingdom"],
            duty=new_debtor["money"],
            comment="",
        )
        session.add(debtor_update)
        session.commit()
    except Exception as e:
        print(f"Должник: Произошла ошибка: {e}")
    



# ! ----- ЗАПУСК ПРОГРАММЫ ----- !
for i in range(1000):     
    player = Serch_active_players()  # это выбранный игрок который будет делать ставку

    # игрок выбирает во что сыграть
    random.choice([Stavka_on_Baraban, Stavka_na_Ruletky])()
    
    # Сохранение данных
    for igrok in Igroki_FULL_list:
        if igrok.id == player.id:
            igrok.balance = player.balance

    # player_to_update = session.query(Igroki).filter_by(id=player.id).first()
    # player_to_update.balance = player.balance
    # session.commit()


for igrok in Igroki_FULL_list:
    session.merge(igrok)  # Обновим данные игрока в базе данных
session.commit()

try:
    Avtomat_1.now_balance = Avtomat_now_balance  # просто чтобы инфа была в БД
    # session.commit()
except Exception as e:
    print(f"Произошла ошибка(баланс автомата): {e}")







# пример
# print(f"#ID: {player.id}")
# player_to_update = session.query(Igroki).filter_by(id=player.id).first()
# player_to_update.balance = 1
# print(f"Имя: {player_to_update.name}, Баланс: {player_to_update.balance} золотых")


# Заполняем таблицу Автомат
try:
    if Avtomat_1_BANK != 0 and Avtomat_now_balance != 0:
        Avtomat_1.results_of_day = Avtomat_1_BANK + Avtomat_now_balance
        Avtomat_now_balance = 0
        Avtomat_1_BANK = 0

    elif Avtomat_1_BANK == 0:
        Avtomat_1.results_of_day = Avtomat_now_balance
        Avtomat_now_balance = 0
    else:
        Avtomat_1.results_of_day = Avtomat_1_BANK
        Avtomat_1_BANK = 0

except Exception as e:
    print(f"Произошла ошибка(заполнение Автомата): {e}")


try:
    last_storage = bank_buffer.storage
except Exception as e:
    print(f"Произошла ошибка(Банк): {e}")

# Заполняем таблицу Банк
try:
    bank_update = BANK(
        id=n_day,
        day=n_day,
        avtomat_profit=Avtomat_1.results_of_day,
        ruletka_profit=0,
        results_of_day=Avtomat_1.results_of_day + 0,
        storage=last_storage + Avtomat_1.results_of_day + 0,
    )
    session.add(bank_update)
    # session.commit()
except Exception as e:
    print(f"Произошла ошибка(заполнение банка): {e}")


# Закрываем сессию
session.commit()
session.close()

end_time = time.time()
execution_time = end_time - start_time
print(f"Программа выполнилась за {round(execution_time, 2)} секунд")
# connection.commit()
# connection.close()
