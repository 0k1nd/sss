tasks = {
'task_1': 1,
'task_2':'London',
'task_4':320,
'task_52':1010,
'task_7':99,
'task_9': None,
'task_89': None,
'task_90':'G1/0/11'
}

def to_do_list():
    print('Выберите действие:')
    act = int(input(' 1. Добавить задачу \n 2. Просмотреть список задач \n 3. Удалить задачу \n 4. Выйти из программы \n  номер действия = '))
    if act == 1:
        key = input('введите название задачи: ')
        value = input('описание задачи: ')
        tasks[key] = value
    elif act == 2:
        for index, (keys, values) in enumerate(tasks.items()):
            print(f" {index + 1}  {values}")
    elif act == 3:
        for keys in tasks.items():
            print(keys)
        x = input('введите название задачи, которую хотите удалить =')
        del tasks[x]
    elif act == 4:
        return print('вы вышли из программы')
    else:
        print('ТАКОЙ КОМАНДЫ НЕ СУЩЕСТВУЕТ')
    to_do_list()

to_do_list()