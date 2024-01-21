from tkinter import Tk, Canvas
okno = Tk()
okno.title("Kartka Świątecznaa")

can = Canvas(okno, bg="#85BBAE", height=600, width=800)

Pien = can.create_rectangle(370, 400, 430, 500, fill="saddlebrown", outline="saddlebrown", width=5)

choinka1 = can.create_polygon(300, 400, 500, 400, 400, 200, fill="forest green", outline="forest green", width=5)
choinka2 = can.create_polygon(320, 300, 480, 300, 400, 150, fill="forest green", outline="forest green", width=5)

bombka1 = can.create_oval(350, 270, 370, 290, fill="red")
bombka2 = can.create_oval(400, 320, 420, 340, fill="gold")
bombka3 = can.create_oval(450, 270, 470, 290, fill="red")
bombka4 = can.create_oval(380, 350, 400, 370, fill="blue")
bombka5 = can.create_oval(430, 350, 450, 370, fill="silver")

gwiazdka = can.create_polygon(400, 150, 390, 180, 395, 160, 390, 150, 400, 155, 410, 150, 405, 160, 410, 180, fill="yellow", outline="yellow", width=10)

snieg = can.create_rectangle(0, 500, 800, 600, fill="white", outline="white")

tekst = can.create_text(400, 100, text="Wesołych Świąt", font="Arial 24 bold", fill="red")

chmurka1 = can.create_oval(650, 50, 750, 120, fill="white", outline="white")
chmurka2 = can.create_oval(700, 80, 800, 150, fill="white", outline="white")

can.pack()

okno.mainloop()