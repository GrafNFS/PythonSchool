from tkinter import *
from tkinter import filedialog as fd
from tkinter import colorchooser, messagebox as mb
from PIL import Image, ImageTk, ImageGrab

def changePenWidth():
    try:
        pen_width=int(pen_width_entry.get())
        if pen_width > 0:
            globals().update(pen_size=pen_width)
            canvas.update()
        else:
            mb.showerror("Ошибка", "Толщина пера должна быть положительным числом.")
    except ValueError:
        mb.showerror("Ошибка", "Толщина пера должна быть целым числом")

def quitWindow():
    window.destroy()

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + pen_size, y + pen_size, fill=pen_color, outline=pen_color)

def chooseColor():
    # Выбор цвета с помощью диалогового окна
    color = colorchooser.askcolor()[1]
    if color:
        globals().update(pen_color=color)

def clearCanvas():
    # Очистка холста и изображения
    canvas.delete("all")

def loadImage():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files','*.png;*.jpg;*jpeg;*.bmp;*gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600,400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0,0,anchor=NW,image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")

def saveCanvas():
    file_path = fd.asksaveasfilename(defaultextension= '.png',filetypes=[('.PNG files', '*.png')])
    if file_path:
        x = window.winfo_rootx()+canvas.winfo_x()
        y = window.winfo_rooty()+canvas.winfo_y()
        x1 = x+canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(file_path)
        mb.showinfo("Сохранено", "Изображение успешно сохранено")

if __name__ == "__main__":
    window = Tk()
    window.title("Рисование на холсте")

    pen_color = "red"
    pen_size = 2
    canvas = Canvas(window, width=600, height=400)
    canvas.pack()
    canvas.bind("<B1-Motion>", draw)


    color_btn = Button(window, text="Выбрать цвет", command=chooseColor)
    color_btn.pack(side=LEFT)

    clear_btn = Button(window, text="Очистить холст", command=clearCanvas)
    clear_btn.pack(side=LEFT)

    menu_bar= Menu(window)
    window.config(menu=menu_bar)
    file_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label="Файл", menu=file_menu)
    file_menu.add_command(label='Загрузить изображение', command=loadImage)
    file_menu.add_command(label='Сохранить', command=saveCanvas)
    file_menu.add_separator()
    file_menu.add_command(label='Выход', command=quitWindow)


    pen_width_label=Label(window,text="Толщина линии:").pack(side=LEFT)

    pen_width_entry=Entry (window, width=10)
    pen_width_entry.pack(side=LEFT)
    pen_width_entry.insert(0, pen_size)

    change_pen_width_btn= Button (window, text='Установить толщину', command=changePenWidth).pack(pady=10)

    window.mainloop()