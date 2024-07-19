class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.nFloors:
            print('Такого этажа не существует!')
        else:
            if new_floor < 1:
                for f in range(1, new_floor-1, -1):
                    print('Спускаемся:', f)
            for f in range(1, new_floor+1):
                print('Поднимаемся:', f)

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.nFloors}.'

    def __eq__(self, other):
        return self.nFloors == other.nFloors

    def __lt__(self, other):
        return self.nFloors < other.nFloors

    def __le__(self, other):
        return self.nFloors <= other.nFloors

    def __gt__(self, other):
        return self.nFloors > other.nFloors

    def __ge__(self, other):
        return self.nFloors >= other.nFloors

    def __ne__(self, other):
        return self.nFloors != other.nFloors

    def __add__(self, value):
        self.nFloors += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


def main():
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    del h2
    del h3

    print(House.houses_history)


if __name__ == '__main__':
    main()