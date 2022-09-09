class Stack:
    #инициализация класса с созданием пустого стека
    def __init__(self):
        self.items = []
    #метод проверки пустого стека, возвращает true(если пуст) или false
    def isEmpty(self):
        return self.items == []
    #метод добавления
    def push(self,item):
        self.items.append(item)
    #метод удаления последнего значения из стека
    def pop(self):
        return self.items.pop()
    #метод, возвращающий последнее значение в стеке, стек при этом не меняется
    def peek(self):
        return self.items[len(self.items)-1]
    #метод возвращает длину стека по количеству элементов
    def size(self):
        return len(self.items)

