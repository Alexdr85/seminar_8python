'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной'''

def write_contacts(filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + input(f'Введите имя фамилию и отчество и номер телефона: '))
    return file

def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, surname, patronymic, phone = line.strip().split(',')
            contact = {
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'phone': phone
            }
            contacts.append(contact)
    return contacts

# def indiv_contacts(filename):
#     contacts = []
#     a = input('Введите характеристику для поиска: ')
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name': name,
#                 'surname': surname,
#                 'patronymic': patronymic,
#                 'phone': phone
#             }
#             contacts.append(contact)

filename = r'Clases de Python\seminario_8\book.txt'
a = int(input('1 - для ввода, 2 - для вывода \n'))
if a == 1:
    add_contact = write_contacts(filename)
elif a == 2:
    contact = read_contacts(filename)
    print(f'{contact}')
else:
    print('Нет такой функции!')

11:47
Ivan,Ivanov,Ivanovich,8777455236
Dmitriy,Dmitriv,Sergeevich,8745541236
Petrov,Petrov,Petrovich,8745236146


file_path = 'tel_sprav.txt'
vvod = int (input('Введите команду: \n1 - Вывод всех данных \n2 - Добавление контакта \n3 - Поиск контакта\n:'))
if vvod ==1:
    with open(file_path, 'r', encoding='UTF-8') as f:
        print(f.read())

elif vvod ==3:
    with open(file_path, 'r', encoding='UTF-8') as f:
        poisk = input('Введите имя или фамилию контакта: ')
        for line in f:
            if poisk in line: print(line) 
        data_tel = f.read()
    poisk = input('Введите имя или фамилию контакта: ')
    data_1 = data_tel.split(',')
    print(data_1)