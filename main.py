import turtle as t
from random import randint

def theeCercle(rad): #Рисуем 3 круга
    for i in range(3):
        t.begin_fill()
        t.color(randint(0, 255), randint(0, 255), randint(0, 255))
        t.circle(rad)
        t.end_fill()

        t.penup()
        t.fd(rad * 2)
        t.pendown()

def triangleRomb():#Рисуем прямоуголник, ромб и трапецию
    t.begin_fill()
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(4):#рисуем прямоуголник
        if i%2 > 0:
            t.forward(50)
        else:
            t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    t.fd(150)
    t.left(45)
    t.pendown()
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.begin_fill()
    for i in range(4): #рисуем ромб
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.penup()
    t.fd(150)
    t.right(45)
    t.pendown()
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))

    t.begin_fill()#рисуем трапецию
    t.forward(150)
    t.left(115)
    t.fd(70)
    t.left(65)
    t.fd(80)
    t.end_fill()

def christmasTree():#Рисуем елку
    for j in range(3):
        t.begin_fill()
        for i in range(3):
            t.color(0, 128, 0)
            t.forward(100)
            t.left(120)
        t.end_fill()
        t.penup()
        t.right(90)
        t.fd(50)
        t.left(90)
        t.pendown()

def square():#Рисуем 3 квадрата
    for j in range(3):
        t.begin_fill()
        for i in range(4):
            t.color(0, 128, 0)
            t.forward(30)
            t.left(90)
        t.end_fill()
        t.penup()
        t.fd(60)
        t.pendown()

def cat():#Рисуем кота
    t.penup()
    t.pensize(2)
    t.color(255, 0, 0)
    t.setpos(-70, -70)
    t.pendown()
    t.left(45)
    t.forward(50)
    t.circle(5, 270)
    t.forward(50)
    t.left(45)
    t.circle(10, 90)
    t.fd(65)
    t.circle(20, 90)

    t.penup()
    t.color(0, 128, 0)
    t.setpos(-65, -70)
    t.pendown()
    t.right(135)
    t.forward(47)
    t.circle(9, 270)
    t.forward(47)

    t.penup()
    t.color(255, 0, 0)
    t.setpos(-60, -70)
    t.pendown()
    t.left(90)
    t.forward(44)
    t.circle(13, 270)
    t.forward(44)

    t.penup()
    t.color(255, 99, 71)
    t.setpos(-55, -70)
    t.pendown()
    t.left(90)
    t.forward(41)
    t.circle(17, 270)
    t.forward(41)

    t.penup()
    t.color(250, 128, 114)
    t.setpos(-50, -70)
    t.pendown()
    t.left(90)
    t.forward(38)
    t.circle(21, 270)
    t.forward(38)

    t.penup()
    t.color(255, 0, 0)
    t.setpos(-45, -70)
    t.pendown()
    t.left(90)
    t.forward(40)
    t.left(15)
    t.circle(30, 30)
    t.forward(14)
    t.circle(30, 40)
    t.fd(10)
    t.left(100)
    t.circle(30, 40)
    t.right(120)
    t.circle(10, 45)
    t.right(100)
    t.circle(30, 40)
    t.left(100)
    t.fd(10)
    t.circle(41, 40)
    t.forward(10)
    t.circle(30, 30)
    t.left(10)
    t.forward(35)
    t.penup()
    t.setpos(100, 100)

def main():
    print("1 Нарисовать 3 круга разных цветов")
    print("2 Нарисовать 3 фигуры \"прямоугольник, ромб и трапецию\"")
    print("3 Нарисовать елку")
    print("4 Нарисовать три квадрата")
    print("5 Нарисовать кота")
    print("0 Выход")
    zad = input("Выберете задание: ")

    t.reset()
    t.hideturtle()
    t.colormode(255)

    if zad == "0":
        return True
    elif zad == "1":
        theeCercle(60)
    elif zad == "2":
        triangleRomb()
    elif zad == "3":
        christmasTree()
    elif zad == "4":
        square()
    elif zad == "5":
        cat()
    else:
        print("Вы ввели не правильное значение попробуйти еще раз")

    main()

main()