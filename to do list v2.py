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

def start():
    while True:
        x = str(input(' add_task \n view_tasks \n delete_task \n exit \n  название действия = '))
        if x == exit:
            break
        def add_task():
            key = input('введите название задачи: ')
            value = input('описание задачи: ')
            tasks[key] = value
        def view_tasks():
            for index, (keys, values) in enumerate(tasks.items()):
                print(f" {index + 1}  {values}")
        def delete_task():
            for keys in tasks.items():
                print(keys)
                x = input('введите название задачи, которую хотите удалить =')
                del tasks[x] 
        match x:
                case "add_task":
                    add_task()
                case "view_tasks":
                    view_tasks() 
                case "delete_task":
                    delete_task()
start()