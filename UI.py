def get_dict ():

    dict = [] 
    id = input ('Введите порядковый номер: ')
    dict.append(id)
    surname = input('Введите фамилию: ')
    dict.append(surname)
    name = input('Введите имя: ')
    dict.append(name)
    birth_day = input('Введите дату рождения в формате ДДММГГ: ')
    dict.append(birth_day)
    work_pl = input('Введите название организации: ')
    dict.append(work_pl)
    # ph_numb1 = ''
    # valid =False
    # while not valid:
    #     try:
    #         ph_numb1 = input('Введите номер телефона : ')
    #         if len(ph_numb1) != 11:
    #             print('В номере телефона должно быть 11 цифр.')
    #         else:
    #             ph_numb1 = int(ph_numb1)
    #             valid = True
    #     except:
    #         print('Номер телефона должен состоять только из цифр.')
    # dict.append(ph_numb1)
    # ph_numb2 = ''
    # ph_numb2 =input('Введите второй номер телефона, если нет введите пробел: ')
    # if ph_numb2 =='':
    #     ph_numb2=''
    #     dict.append(ph_numb2)
    # else:
    #     valid =False
    #     while not valid:
    #         try:
    #             ph_numb1 = input('Введите номер телефона : ')
    #             if len(ph_numb1) != 11:
    #                 print('В номере телефона должно быть 11 цифр.')
    #             else:
    #                 ph_numb1 = int(ph_numb1)
    #                 valid = True
    #         except:
    #             print('Номер телефона должен состоять только из цифр.')
    return 
