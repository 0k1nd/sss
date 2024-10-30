tasks = {}

def main():
    while True:
        x = int(input(' 1.add_task \n 2.view_tasks \n 3.delete_task \n 4.exit \n  номер действия = '))
        if x == 4:
            break
 
        match x:
                case 1:
                    add_task()
                case 2:
                    view_tasks() 
                case 3:
                    delete_task()


def add_task():
    key = input('введите название задачи: ')
    value = 'описание пустое'
    tasks[key] = value


def view_tasks():
    for index, (keys, values) in enumerate(tasks.items()):
        print(f" {index + 1}  {keys}")


def delete_task():
    for keys in tasks.items():
        print(keys)
        x = input('введите название задачи, которую хотите удалить =')
        del tasks[x]
main()