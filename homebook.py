import time

def show_menu():
    print('\n***Телефонная книжка***\n'
          '1. Отоброзить весь справочник\n'
          '2. Найти абонента\n'
          '3. Добавить абонента\n'
          '4. Изменить номер телефона\n'
          '5. Удалить абонента\n'
          '6. Сохранить справочник\n'
          #'7. Сохранить справочник\n'
          '7. Закончить работу\n')
    
    while True:
        try :
            choice = int(input('Выберите необходимое действие: ' ))
            if choice < 1 or choice > 7:
                #choice = int(input('Выберите необходимое действие: ', ))
                work_with_phonebook()
            break
        except:
            print('Ошибка ввода')    
    return choice


#0.читает фаил сохраненный
def read_txt(filename): #читает и присваивает ключи
    phone_book = []
    fields = ['Фамилия','Имя','Телефон']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.rstrip('\n').split(',')))
            phone_book.append(record)
    return phone_book

#2. найти абонента
def find_by_find(phone_book, find):
    flag = 0
    for dict in phone_book:
        for key, value in dict.items():
            if value == find:
                res = []
                res.append(dict)
                for dict in res:
                    print('Результаты поиска:\n''---------------------------')
                    print('\n'.join(f'{key}: {value}' for key, value in dict.items()) )
                    print("---------------------------")
                    flag = 1
    if flag != 1:
        print(f'Абонент {find} не найден')
    input('Для продолжения нажмите [Enter] . . .')
    return res


#3. Добавить абонента + сохранение записи в txt
def add_user(filename, phone_book, user_lastname, user_number, user_firstname=''):
    new_user = {'Фамилия':user_lastname,'Имя':user_firstname,'Телефон':user_number}
    phone_book.append(new_user)
    with open(filename,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')#срез последней ', '

#4. Изменить номер телефона абонента
def change_number(filename, phone_book, user_lastname, user_firstname, new_number):
    # Изменения, которые нужно внести
    changes = {'Фамилия':user_lastname,'Имя':user_firstname,'Телефон':new_number}
    # Находим словарь и вносим изменения
    for d in phone_book:
        if user_lastname in d.values() and user_firstname in d.values():
            d.update(changes)

        with open(filename, 'w', encoding='utf-8') as f:
    # Записываем картеж в файл
            for d in phone_book:
                f.write(','.join(d.values()) + '\n')        


#5. Удаление абонента                    
def del_user(filename,phone_book,last_name, firstname):
    new_phone_book = tuple(d for d in phone_book if not (last_name in d.values() and firstname  in d.values()))
    print(f'Абонент {last_name} {firstname} удален!')
    with open(filename, 'w', encoding='utf-8') as f:
    # Записываем картеж в файл
        for d in new_phone_book:
            f.write(','.join(d.values()) + '\n')
    
    return

def save_phone_book(new_filename, phone_book):
    save = new_filename + '.txt'
    with open(save, 'w', encoding='utf-8') as f:
    # Записываем картеж в файл
        for d in phone_book:
            f.write(','.join(d.values()) + '\n')


#Программа телефонный справочник! СТАРТ
def work_with_phonebook():
	
    choice = show_menu() #меню

    filename = 'phonebook.txt'

    phone_book = read_txt(filename)

    while (choice != 7):
        if choice == 1: #'1. Отоброзить весь справочник'
            #сортировка кортежа словарей
            sorted_phone_book = tuple(sorted(phone_book, key=lambda d: d['Фамилия']))
            
            for dict in sorted_phone_book:
                for key, value in dict.items():
                    print(f'{key}: {value}')
                print("---------------------------")  # Печатает новую строку после каждого словаря
            input('Для продолжения нажмите [Enter] . . .')        
        elif choice == 2: #'2. Найти абонента'
            find = input('Найти можно по Фамилии, Имени или Телефону:').upper()
            find_by_find(phone_book, find)
            

        elif choice == 3: #'3. Добавить абонента'
            print('\n***Добавить нового абонента в телефонную книгу***\n')
            user_lastname = input('Видите *Фамилию: ').upper()
            user_firstname = input('Видите Имя: ').upper()
            
            #res = print('\n'.join(f'{key}: {value}' for key, value in dict.items()) )
            user_number = input('Видите номер *Телефона: ')
            add_user(filename, phone_book, user_lastname, user_number, user_firstname)

            print(f'Абонент {user_lastname}, {user_firstname}, {user_number} добавлен!')
            time.sleep(3)          

        elif choice == 4: #'4. Изменить номер абонента\n'
            print('\n ***Изменить номер абонента***\n')
            user_lastname = input('Ввидите фамилию: ').upper()
            user_firstname = input('Ввидите имя: ').upper()
            new_number = input('Ввидите новый номер: ')

            if len(last_name) == 0:
                print('***Ошибка ввода вы ничего не ввели***')
                time.sleep(2) 
                choice
            print(f'Вы хотите изменить номер {user_lastname} {user_firstname} абонента ?', 
                  '\n 1. - Да', '\n 2. - Нет')
            while True:
                try:
                    yes_no = int(input('Выберите необходимое действие: ' ))
                    if yes_no > 0 or yes_no < 3:
                        if yes_no == 1:
                            change_number(filename, phone_book, user_lastname, user_firstname, new_number)
                            print('\n ***Номер измене!***\n')    
                            time.sleep(3)
                            work_with_phonebook()
                        elif yes_no == 2:
                            print('***Отмена***')
                            time.sleep(2)                        
                            work_with_phonebook()
                    else:
                        print('***Ошибка***')
                        work_with_phonebook()
                        time.sleep(3)
                    time.sleep(3)    
                    work_with_phonebook()                     
                    break
                except:
                    print('Ошибка ввода')

        elif choice == 5: #'5. Удалить абонента\n'
            print('\n ***Удаления Абонента***')
            last_name = input('Ввидите фамилию: ').upper()
            firstname = input('Имя для удаления: ').upper()
            if len(last_name) == 0:
                print('***Ошибка***')
                time.sleep(2) 
                choice
            print(f'Вы хотите удалить {last_name} {firstname} абонента ?', 
                  '\n 1. - Да', '\n 2. - Нет')
            while True:
                try:
                    yes_no = int(input('Выберите необходимое действие: ' ))
                    if yes_no > 0 or yes_no < 3:
                        if yes_no == 1:
                            del_user(filename,phone_book,last_name, firstname)
                            print('Номер абонента удален!')
                            time.sleep(3)
                            work_with_phonebook() 
                        elif yes_no == 2:
                            print('***Отмена***')
                            time.sleep(2)                        
                            work_with_phonebook()
                    else:
                        print('***Ошибка***')
                        work_with_phonebook()
                        time.sleep(3)
                    #print('***Ошибка***')
                    time.sleep(3)    
                    work_with_phonebook()                     
                    break
                except:
                    print('Ошибка ввода')
                

        elif choice == 6: #'6. Сохранить справочник\n'
             print('***Сохранить справочник***')
             new_filename = input('Ввидите новое имя файла: ')

             letters ='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ.,1234567890-=+)()*' 
             if all(letter in letters for letter in new_filename):
                save_phone_book(new_filename, phone_book)
                print('***Фаил сохранен***')
                time.sleep(3)
                work_with_phonebook()

             else:
                print('Ошибка ввода')
                print("Ввод содержит недопустимые символы.")
                choice
                time.sleep(3)            

        elif choice == 7: #'7. Закончить работу'
            print('Програма закрыта')
            time.sleep(3)
            break
                                

        choice = show_menu()

        
           
 

work_with_phonebook()