import turtle as t

def stok():
    for r in range(40, 0, -10):
        for i in range(6):
            t.color(255, 165, r * 6)
            t.fillcolor(162, r * 6, 255)
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)

def stageOne():
    t.rt(90)
    for r in range(40, 0, -10):
        for i in range(6):
            t.color(255, 165, r * 6)
            t.fillcolor(162, r * 6, 255)
            t.begin_fill()
            for j in range(4):
                t.forward(r * 2)
                t.left(90)
            t.end_fill()
            t.rt(60)

def stageTwo():
    for r in range(40, 0, -10):
        for i in range(6):
            t.color(255, 165, r * 6)
            t.fillcolor(162, r * 6, 255)
            t.begin_fill()
            for j in range(3):
                t.forward(r * 2)
                t.left(120)
            t.end_fill()
            t.rt(60)

def main():
    print("1 Дано")
    print("2 Задание 1")
    print("3 Задание 2")
    print("0 Выход")
    zad = input("Выберете задание: ")

    t.reset()
    t.hideturtle()
    t.colormode(255)
    t.pensize(5)

    if zad == "0":
        return True
    elif zad == "1":
        stok()
    elif zad == "2":
        stageOne()
    elif zad == "3":
        stageTwo()
    else:
        print("Вы ввели не правильное значение попробуйти еще раз")

    main()

main()