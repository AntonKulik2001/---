def welcome(): #Приветственная строка
    print(" ------------------------ ")
    print(" Добро пожаловать в игру  ")
    print("      Крестики-Нолики     ")
    print(" ------------------------ ")
    print("Пишите ваш ход в виде: x y")
    print("     x - это строка       ")
    print("     y - это стролбик     ")
fielde = [[" "] * 3 for i in range(3)] # создаем поле для игры
def place():     # создаем визуальное игровое поле
    print()
    print("    | 0 | 1 | 2 |")
    print(" ---------------- ")
    for i, row in enumerate(fielde):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ---------------- ")
def move():    # принимаем ход игрока и проверяем корректность ввода
    while True:
        cords =input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапозона!")
            continue

        if fielde[x][y] != " ":
            print("Клетка занята!")
            continue

        return x,y
def check_win(): #Проверка победной комбинации
    win_cord =(((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),
               ((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),
               ((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(fielde[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True

    return False

welcome() #Начало игры
num = 0
while True:
    num += 1
    place()
    if num % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = move()

    if num % 2 == 1:
        fielde[x][y] = "X"
    else:
        fielde[x][y] = "0"
    if check_win():
        break

    if num == 9:
        print(" Ничья!")
        break