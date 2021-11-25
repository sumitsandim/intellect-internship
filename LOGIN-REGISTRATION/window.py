from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x438")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 438,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    400.0, 219.0,
    image=background_img)

canvas.create_text(
    389.0, 61.5,
    text = "WELCOME",
    fill = "#000000",
    font = ("Roboto-BoldItalic", int(64.0)))

canvas.create_text(
    574.0, 159.0,
    text = "Start With",
    fill = "#000000",
    font = ("Roboto-BoldItalic", int(36.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 417, y = 249,
    width = 119,
    height = 128)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 616, y = 244,
    width = 115,
    height = 133)

window.resizable(False, False)
window.mainloop()
