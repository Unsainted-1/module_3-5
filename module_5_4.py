class House:
    houses_history = []
    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor <= 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def  __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def  __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def  __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def  __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def  __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Горский', 18)
print(House.houses_history)
h2 = House('Танхаус', 3)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)