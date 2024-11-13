from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
notifText = ""
music = False  # Переменная для отслеживания проигрывания музыки

def set():
    global t, notifText
    rem_time = sd.askstring("Время напоминания", "Введите время напоминания в формате ЧЧ:ММ (в 24-часовом формате):")
    if rem_time:
        try:
            hour = int(rem_time.split(":")[0])
            minute = int(rem_time.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0)
            t = dt.timestamp()
            notifText = sd.askstring("Текст напоминания", "Введите текст напоминания:")
            label.config(text=f"Напоминание на {hour:02}:{minute:02} с текстом: {notifText}")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            mb.showinfo("Напоминание", notifText)
            t = None
    window.after(10000, check)

def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play(10)

def stop_music():
    global music, notifText
    if music:
        pygame.mixer.music.stop()
        music = False
        notifText = ""
    label.config(text="Установить новое напоминание")

if __name__ == "__main__":
    window = Tk()
    window.title("Напоминание")

    label = Label(text="Установите напоминание", font=("Arial", 14))
    label.pack(pady=10)

    set_btn = Button(text="Установить напоминание", command=set)
    set_btn.pack(pady=10)

    stop_btn = Button(text="Остановить музыку", command=stop_music)
    stop_btn.pack(pady=5)

    check()

    window.mainloop()