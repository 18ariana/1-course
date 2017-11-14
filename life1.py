import pygame
from pygame.locals import *



class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

# pygame.draw.rect(self.screen, pygame.Color('green'), (0,0, 5,5))


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()

    # Отрисовка списка клеток
    # Выполнение одного шага игры (обновление состояния ячеек)
    # PUT YOUR CODE HERE


    pygame.display.flip()
    clock.tick(self.speed)
pygame.quit()


def cell_list(self, randomize=True):
    """ Создание списка клеток.
    :param randomize: Если True, то создается список клеток, где
    каждая клетка равновероятно может быть живой (1) или мертвой (0).
    :return: Список клеток, представленный в виде матрицы
    """

    if randomize :
         self.clist = [[random.randrange(0,2) for i in range(self.cell_width)]
                       for g in range(self.cell_height)]
    return self.clist


def draw_cell_list(self, clist):
    """ Отображение списка клеток
    :param rects: Список клеток для отрисовки, представленный в виде матрицы
    """
    pygame.draw.rect(self.screen,pygame.Color, (x,y,a,b))
    for i in range(self.cell_width):
        for g in range(self.cell_height):
            x = i * self.cell_width - 1
            y = g * self.cell_height -1
            a = cell_size
            b = cell_size
    if self.clist([i][g]) == 1 :
        pygame.Color('Green')
    else pygame.Color('White')



def get_neighbours(self, cell):
    """ Вернуть список соседей для указанной ячейки
    :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
    :return: Одномерный список ячеек, смежных к ячейке cell
    """
    neighbours = [for i in range (len( self.clist)):
        for g in range(len(self.clist[i])):
            n1 = [i + 1, g],
            n2 = [i - 1, g],
            n3 = [i,g + 1],
            n4 = [i,g - 1],
            n5 = [i - 1, g + 1],
            n6 = [i + 1, g + 1],
            n7 = [i-1, g - 1],
            n8 = [i +1, g + 1]]

    return neighbours


def update_cell_list(self, cell_list):
    """ Выполнить один шаг игры.
    Обновление всех ячеек происходит одновременно. Функция возвращает
    новое игровое поле.
    :param cell_list: Игровое поле, представленное в виде матрицы
    :return: Обновленное игровое поле
    """
    new_clist = self.clist
    for i in range(self.cell_height):
        for g in range(self.cell_height):
            if self.clist[i][g] == 1:
                if sum(self.get_numbers(self.clist, i, g)) not in (2,3):
                    new_clist[i][g] = 0
                else:
                    new_clist[i][g] = 1
            else:
                if sum(self.get_numbers(self.clist, i, g)) == 3:
                    new_clist[i][g] = 1
                else:
                    new_clist[i][g] = 0
    self.clist = new_clist
    return self.clist