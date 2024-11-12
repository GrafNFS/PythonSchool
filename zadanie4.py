def zadanieOne():
    i = 3
    while i <= 43:
        print(i)
        i += 10

def zadanieTwo():
    passWord = ""
    print("Пароль должен быть не меньше 8 символов")
    while len(passWord) <= 8:
        passWord = input("Введите пароль: ")
        if len(passWord) >= 8:
            print("Вы саблюли условие о длине пароля")

def zadanieThree():
    strAvto = ""
    print("Вы должны ввести: \"LADA 2010г 205000км 450000руб\"")
    while strAvto.find("LADA 2010г 205000км 450000руб"):
        strAvto = input("Введите параметры автомобиля по шаблону \nKIA 2010г 5000км 1450000руб: ")
        strAvtoArray = strAvto.split()
        print(f"Продается автомобиль\nМарка: {strAvtoArray[0]}\nГод выпуска: {strAvtoArray[1]}\nПробег: {strAvtoArray[2]}\nЦена: {strAvtoArray[3]}")

def main():
    print("1 Задание 1")
    print("2 Задание 2")
    print("3 Задание 3")
    print("0 Выход")
    zad = input("Выберете задание: ")

    if zad == "0":
        return True
    elif zad == "1":
        zadanieOne()
    elif zad == "2":
        zadanieTwo()
    elif zad == "3":
        zadanieThree()
    else:
        print("Вы ввели не правильное значение попробуйти еще раз")

    main()

main()