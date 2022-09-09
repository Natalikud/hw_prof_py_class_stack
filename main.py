from stack import Stack

def balance(String):
    s = Stack()
    for index in String:
        # print(index)
        if index == '(' or index =='['  or index =='{':
            s.push(index)
            # print(s.items)
        else:
            s.pop()
            # print(s.items)
    print(f'Проверка сбалансированности скобок:{String}')
    if s.isEmpty() == True:
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    balance('(((([{}]))))')
    # balance('}{}')


