from datetime import datetime


def with_log(path):
    def _with_log(old_function):
        def new_function(*args, **kwargs):
            x = old_function(*args, **kwargs)
            with open(path + r'\log.txt', 'w', encoding='utf-8') as file:
                file.write(f'{datetime.now()} >> {old_function.__name__} >> {args, kwargs} >> {x}')
        return new_function
    return _with_log


@with_log(r'C:\Users\vital\Desktop\Python projects\AdPy No.5')
def read_cookbook (f="cookbook.txt", mode="rt"):
    cook_book = {}
    with open (f, mode, encoding="utf-8") as file:
        while True:
            dish = file.readline().strip()
            if not dish:
                break
            cook_book[dish] = []
            ingredients = dict()
            for i in range(int(file.readline())):
                lst = file.readline().strip().split(" | ")
                ingredients["ingredient_name"] = lst[0]
                ingredients["quantity"] = int(lst[1])
                ingredients["measure"] = lst[2]
                cook_book[dish] += [ingredients.copy()]
            file.readline()
    return cook_book


read_cookbook()



