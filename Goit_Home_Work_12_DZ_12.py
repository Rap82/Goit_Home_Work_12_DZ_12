# ============================= Модуль 12 (останій в Python Core) =======================================

# +++++++++++++++++++++++++++++++++  Серіалізація об'єктів Python ++++++++++++++++++++++

#                             1.Серіалізація об'єктів Python
#                             2.Серіалізація об'єктів Python за допомогою pickle
#                             3.Серіалізація об'єктів Python за допомогою json
#                             4.Робота з таблицями CSV у Python
#                             5.Управління порядком серіалізації
#                             6.Створення копій об'єктів Python



# ================================ Звдання 1 / Task 1 ======================================

# ================================  1.Серіалізація об'єктів Python  ==========================

# Для серіалізації/десеріалізації об'єктів Python, коли важлива швидкість, коректність і невеликий розмір пам'яті, 
# що використовується, найкраще підійде пакет pickle.

# У пакета pickle є дві пари парних методів:

# Перша пара методів - це dumps, який упаковує в byte-рядок об'єкт, і loads - він розпаковує з byte-рядки в об'єкт.

# Ці методи потрібні, коли ми хочемо контролювати, що робити з byte поданням, наприклад, 
# відправити його по мережі або прийняти з мережі.

# import pickle

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# byte_string = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_string)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False
# У цьому прикладі упакований у byte_string словник some_data розпакован в unpacked та unpacked суворо дорівнює some_data, 
# але це все ж таки не той самий об'єкт.

# Друга пара методів: dump та load - вони упаковують у відкритий для byte-запису 
# файл і розпаковують з відкритого для byte-читання файлу.

# import pickle

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }

# file_name = 'data.bin'

# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)

# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)

# print(unpacked == some_data)  # True
# print(unpacked is some_data)  # False
# Результат аналогічний попередньому прикладу. Головна відмінність у тому, 
# що під час виконання цього коду в робочій папці з'явився файл data.bin

# ++++++++++++++++++++++++++++++++++++++Умова / Condition ++++++++++++++++++++++++++++++++++++++++

# Є список, кожен елемент якого є словником з контактами користувача наступного виду:

#     {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }
# Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

# Розробіть дві функції для серіалізації та десеріалізації списку контактів 
# за допомогою пакета pickle та зберігання отриманих даних у бінарному файлі.

# Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. 
# Вона зберігає вказаний список у файл, використовуючи метод dump пакету pickle.

# Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, 
# використовуючи метод load пакету pickle.

# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++

# Примітка : Серіалізація і обернена до неї процедура Десіралізація схожа на роботу кодера - декодекр.
#            Спочатку - серіалізуємо дані , потім їх десерелізуємо за потреби. (По замовчуванню переводить в 
#             байт-рядки тому якщо треба працювати з серіалізованими даними то потрібно застосуовуати методи байт-рядків)(*для себе)


import pickle # Імпортуємо пакет *pickle- Пакет Для серіалізації/десеріалізації об'єктів Python, 
              # коли важлива швидкість, коректність і невеликий розмір пам'яті. 
              # Просто перетворює всі дані в байт рядки і повертає за потреби з байт рядків дані назад . 
              # також має методи запису і читання з файлу цих байт рядків.


def write_contacts_to_file(filename, contacts):
    ''' Функція приймає два аргумента , *filename - імя файлу в який будемо записувати наші контакти у вигляді байт-ряків
    і contacts - самі дані які треба записати .
    Відкриває наш файл для запису байт-рядків і за допомогою  метод *pickle.dump(contacts, fh) 
    записуємо туди свої контакти у вигляді байт рядків'''
    
    with open(filename, "wb") as fh: # Відкрити файл з іменем *filename(шлях до файлу тип Path) 
                                     # для запису з параметром "wb" -байт-рядків, Задопомогою менеджера контексту *with ... as
        pickle.dump(contacts, fh)    # Перетворюємо наші контакти в байт-рядки і передаємо їх файл-хендлеру *fh 
                                     # за допомгою методу *pickle.dump(contacts, fh).
                                     # По завершеню файл автоматично закриється і дані вньому збережуться.Читай менеджер контексту.
    

def read_contacts_from_file(filename):
    ''' Функція приймає один аргумента , *filename - імя файлу з якого будемо зчитувати наші контакти у вигляді байт-ряків
    і повертати ї початковий вигляд.(той що був до сереалізації)
    Відкриває наш файл для читання байт-рядків і за допомогою  метод *pickle.load(fh) 
    Зчитуємо байт-дані і нормальний їх вигляд присвоюємо змінній contacts 
    Повертаємо контакти з функції в їх початковому вигляді'''

    with open(filename, "rb") as fh: # Відкрити файл з іменем *filename(шлях до файлу тип Path) 
                                     # для читаннябайт-рядків з параметром "rb" - , Задопомогою менеджера контексту *with ... as
        contacts = pickle.load(fh)   # Зчитуємо данні з файлового хендлера *fh і десерілізуємо їх за допомогою метода *pickle.load(fh)
                                     # Присвоюємо десіралізовані дані зміній *contacts.
    return contacts         # Повертаємо дані з функції



# ++++++++++++++++++++ Код / Code ++++++++++++++++++++++++++++++++++++