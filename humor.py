import itertools
import tkinter as tk


def slide_show():
        window = tk.Tk()
        window.title("Mems :)")
        window.geometry('1000x600')

        CYCLED_IMAGES = itertools.cycle([
                tk.PhotoImage(file="mem/1.png"),
                tk.PhotoImage(file="mem/2.png"),
                tk.PhotoImage(file="mem/3.png"),
                tk.PhotoImage(file="mem/4.png"),
                tk.PhotoImage(file="mem/5.png"),
                tk.PhotoImage(file="mem/6.png"),
                tk.PhotoImage(file="mem/7.png"),
                tk.PhotoImage(file="mem/8.png"),
                tk.PhotoImage(file="mem/9.png"),
                tk.PhotoImage(file="mem/10.png"),
        ])

        def get_next_image() -> tk.PhotoImage:
                return next(CYCLED_IMAGES)

        def _on_button_click():
                panel.config(image=get_next_image())

        panel = tk.Label(window, image=get_next_image())
        panel.pack()

        button = tk.Button(window, text="Наступний >>>")
        button.place(relx=0.5, rely=0.9)
        button.config(command=_on_button_click)

        window.mainloop()


def humor():
    while True:
        if input("Хочеш подивитися меми? Натисни 1\n"
                 "Щоб завершити, натисни Enter: ") == "1":
            slide_show()
        else:
            break



