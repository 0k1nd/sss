tasks = []

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
        print('-------------')


def add_task():
    task_name = str(input('введите название задачи: '))
    tasks.append(task_name)


def view_tasks():
    for i, element in enumerate(tasks):
        print((i + 1), element)


def delete_task():
    for i, element in enumerate(tasks):
        print((i + 1), element)
    del_task = int(input('введите номер задачи, которую хотите удалить ='))
    tasks.pop(del_task - 1)


main()