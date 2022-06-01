my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(my_list))

for i in my_list:
    my_list = [i.lower() for i in my_list]
    #print(my_list)
    my_list = ' '.join(my_list)
    #print(my_list)
    my_list = my_list.split()
    #print(my_list)

    print(my_list)