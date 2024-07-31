import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self._color = self._check_color(color)
        all_sides = []
        for side in sides:
            all_sides.append(side)
        self._sides = all_sides
        self.filled = False

    def get_color(self):
        return self._color

    @staticmethod
    def _check_color(colors):
        if not isinstance(colors, tuple):
            return [0, 0, 0]
        for color in colors:
            if not isinstance(color, int):
                return [0, 0, 0]
        if isinstance(colors, int):
            list_from_tuple = [colors]
        else:
            list_from_tuple = list(colors)
        while len(list_from_tuple) <= 2:
            list_from_tuple.append(0)
        while len(list_from_tuple) > 3:
            list_from_tuple.pop(0)
        for i in range(len(list_from_tuple)):
            if isinstance(list_from_tuple[i], int) or isinstance(list_from_tuple[i], float):
                int_numb = abs(int(list_from_tuple[i]))
                list_from_tuple[i] = 255 if (int_numb > 255) else int_numb
            else:
                list_from_tuple[i] = 0
        return list_from_tuple

    @staticmethod
    def _is_valid_color(*colors):
        for color in colors:
            if (not isinstance(color, int)) or (color > 255):
                return False
        else:
            return True

    def set_color(self, *colors):
        if not self._is_valid_color(*colors):
            return
        list_colors = []
        for color in colors:
            list_colors.append(color)
        while len(list_colors) > 3:
            list_colors.pop(0)
        while len(list_colors) < 3:
            list_colors.append(0)
        self._color = list_colors

    def _is_valid_sides(self, sides):
        list_sides = sides
        if len(list_sides) != self.sides_count :
            return False
        for side in sides:
            if not isinstance(side, int):
                return False
        return True

    def get_sides(self):
        return self._sides

    def len_(self):
        perimeter = 0
        if not isinstance(self._sides, int):
            for side in self._sides:
                perimeter += side
        else:
            perimeter = self._sides
        return perimeter

    def set_sides(self, *sides):
        all_sides = []
        for side in sides:
            all_sides.append(side)
        if not self._is_valid_sides(all_sides):
            return
        self._sides = all_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if not self._is_valid_sides(self._sides):
            self._sides = [1]
        self._radius = self._sides[0] / 2 / math.pi

    @staticmethod
    def get_square(radius):
        return math.pi * radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color = (0, 0, 0), *sides):
        super().__init__(color, *sides)
        if not self._is_valid_sides(self._sides):
            self._sides = [1, 1, 1]
        self._height = self.all_heights_triangle(*sides)

    @staticmethod
    def all_heights_triangle(*sides):
        perimetr = 0
        for side in sides:
            perimetr += side
        h_p = perimetr / 2
        numerator = 2 * ((h_p * (h_p - sides[0]) * (h_p - sides[1]) * (h_p - sides[2])) ** 0.5)
        list_heights = []
        for side in sides:
            height = numerator / side
            list_heights.append(height)
        return list_heights

    def get_square(self):
        return self._sides[0] * self._height[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if not self._is_valid_sides(self._sides):
            side = 1
        else:
            side = self._sides[0]
        self._sides = [side] * self.sides_count

    def _is_valid_sides(self, sides):
        if len(sides) != 1 or (not isinstance(sides[0], int)):
            return False
        return True

    def _is_valid_sides2(self, *sides):
        if len(sides) != 1:  #
            return False
        for side in sides:
            if side is not int:
                return False
        return True

    def get_volume(self):
        return self._sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print((circle1.len_()))

print(cube1.get_volume())





