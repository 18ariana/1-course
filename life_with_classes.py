import pygame
from pygame.locals import *
import random
from copy import deepcopy


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
            pygame.draw.line
            (self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line
            (self.screen, pygame.Color('black'), (0, y), (self.width, y))

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
            self.draw_cell_list()
            self.clist.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
        
    def cell_list(self, randomize=True):
        self.clist = CellList(self.cell_width, self.cell_height, randomize)
        self.grid = self.clist.grid

    def draw_cell_list(self):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if self.grid[j][i].is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, a, b))



class Cell():
    def __init__(self, row, col, state=0):
        self.alive = state
        self.row = row
        self.col = col

    def is_alive(self):
        return self.alive


class CellList:
    def __init__(self, nrows, ncols, randomize=True):
            self.ncols = ncols
            self.nrows = nrows
            if (randomize):
                self.grid = [[Cell(i, j, random.randint(0, 1))for i in range(nrows)] for g in range(ncols)]
            else:
                self.grid = [[Cell(i, g, 0)for i in range(nrows)] for g in range(ncols)]

    def get_neighbours(self, n1, n2, n3, n4, n5, n6, n7, n8, cell):
        neighbours = [ n1, n2, n3, n4, n5, n6, n7, n8 ]
        for i in range(len(self.grid))):
            for g in range(len(self.grid)):
                n1 = [i + 1, g],
                n2 = [i - 1, g],
                n3 = [i, g + 1],
                n4 = [i, g - 1],
                n5 = [i - 1, g + 1],
                n6 = [i + 1, g + 1],
                n7 = [i - 1, g - 1],
                n8 = [i + 1, g + 1]
                neighbours.append(self.grid[i][g])

            return neighbours

    def update(self, count):
        new_grid = deepcopy(self.grid)
        for cell in self:
            neighbours = self.get_neighbours(cell)
           cnt = sum(c.is_alive() for c in neighbours)
            if cell.is_alive():
                if cnt < 2 or cnt > 3:
                        new_grid[cell.row][cell.col].alive = 0
            else:
                if cnt == 3:
                    new_grid[cell.row][cell.col].alive = 1
        self.grid = new_grid
        return self

    def __iter__(self):
       self.i_cnt, self.g_cnt = 0, 0
        return self

    def __next__(self):
            if (self.i_cnt == self.nrows):
                raise StopIteration
                cell = self.grid[self.i_countnt][self.g_count]
            self.g_cnt += 1
            if self.g_cnt == self.ncols:
                self.i_cnt += 1
                self.g_cnt = 0

            return cell

    def __str__(self):
        str = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                if (self.grid[i][g].alive):
                    str += '1 '
                else:
                    str += '0 '
            str += '\n'
        return str

    @classmethod
    def from_file(cls, filename):
        grid = []
        with open(filename) as f:
            for i, line in enumerate(f):
                grid.append([Cell(i, g, int(c))
                             for j, c in enumerate(line) if c in '01'])
        clist = cls(len(grid), len(grid[0]), False)
        clist.grid = grid
        return clist
   
if __name__ == '__main__':
game = GameOfLife(640, 480, 10)
game.run()

