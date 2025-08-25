from tkinter import PhotoImage

from customtkinter import *
# ------------------------ Constants ------------------------
PINK = "#e2979c"
RED    = "#e76f51"
GREEN  = "#2a9d8f"
YELLOW = "#e9c46a"
FONT_NAME = "Courier"
WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
WIDTH = HEIGHT = 600

# ------------------------ Timer Reset ------------------------

# ------------------------ Timer Mechanism ------------------------

# ------------------------ Countdown Mechanism ------------------------

# ------------------------ UI Setup ------------------------

set_appearance_mode("dark")
set_default_color_theme("blue")

app = CTk()
app.title("Pomodoro")
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)
app.config(bg=YELLOW)


# Creating Canvas
canvas = CTkCanvas(master=app, width=512, height=512, bg=YELLOW, highlightthickness=0)
# Getting tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(256, 256, image=tomato_img)
# Creating text on image
canvas.create_text(260, 310, text="00:00", fill="white", font=(FONT_NAME, 34, 'bold'))
# Placing canvas on screen
canvas.grid(column=1, row=1)


# Creating main label
timer_text = CTkLabel(master=app, text="Timer", font=(FONT_NAME, 50, "normal"), te)


app.mainloop()

