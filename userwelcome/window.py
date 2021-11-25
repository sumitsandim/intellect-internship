from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("762x507")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 507,
    width = 762,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    381.0, 253.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 253, y = 190,
    width = 114,
    height = 149)

canvas.create_text(
    225.0, 84.0,
    text = "WELCOME",
    fill = "#d61f40",
    font = ("Roboto-Bold", int(48.0)))

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 49, y = 190,
    width = 146,
    height = 149)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 644, y = 45,
    width = 88,
    height = 21)

window.resizable(False, False)
window.mainloop()
