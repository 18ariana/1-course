import time, random

def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return print([values[n*i:n*i+n] for i in range(n)])


def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    pos = (0, 0)
    row, col = pos
    return values[row]

def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    return [values[i][col] for i in range(len(values))]


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos """
    row, col = pos
    square = []
    stroka = row // 3*3
    stolbets = col // 3*3
    for i in range(stroka, stroka + 3):
        for j in range(stolbets, stolbets + 3):
            square.append(values[i],[j])
    return square


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if values[i][j] == ".":
                return (i,j)
    return (-1,-1)

def find_possible_values(grid, pos):
    """ Вернуть все возможные значения для указанной позиции """
    checker = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    c = set(get_col(grid, pos))
    b = get_block(grid, pos)
    r = set(get_row(grid, pos))
    checker -= r
    checker -= c
    for i in range(3):
        checker -= set(get_block[i])
    return checker

def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    """
    empty_space = find_empty_positions(grid)
    if empty_space == (-1,-1):
        return grid
    space = find_possible_values(grid, pos)
    col, row = space
    for i in range (len(space)):
        grid[col][row] = i
        solution = solve[grid]
        grid[col][row]='.'
        if solution != None:
            return grid
    return None



def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False """

    for i in range(9):
        right = {1, 2, 3, 4, 5, 6, 7, 8, 9. '.'}
        if right - set(get_row(solution, (i, 0))) != {'.'}:
            return False
        right = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        if right - set(get_col(solution, (0, i))) != {'.'}:
            return False
    for i in ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6)):
        right = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        for n in get_block(solution, i):
            right -= set(n)
        if right != {'.'}:
            return False
    return True


def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    chek = N - 81
    grid = [["." for i in range(9)] for i in range(9)]
    grid = solve(grid)
    jungle = [(i,j) for i in range(9) for j in range(9)]
    for m in range (chek) :
        delete = random.choice(jungle)
        jungle.remove(delete)
        grid [delete[0]][delete[1]] = "."
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        start = time.time()
        solve(grid)
        end = time.time()
        print(fname + ": " + str(end - start))
