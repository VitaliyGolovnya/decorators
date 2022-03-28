from datetime import datetime


def with_log(path):
    def _with_log(old_function):
        def new_function(*args, **kwargs):
            x = old_function(*args, **kwargs)
            with open(path + r'\log.txt', 'w', encoding='utf-8') as file:
                file.write(f'{datetime.now()} >> {old_function.__name__} >> {args, kwargs} >> {x}')
            return x

        return new_function

    return _with_log


path = r'C:\Users\vital\Desktop\Python projects\AdPy No.5'


@with_log(path)
def summator(x, y):
    return x + y


three = summator(1, 2)
five = summator(2, 3)

result = summator(three, five)

print('result: ', result)
print('result type: ', type(result))
