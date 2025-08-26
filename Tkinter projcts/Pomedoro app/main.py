from tkinter import PhotoImage
import winsound
from customtkinter import *
# ------------------------ Constants ------------------------
ONYX = "#3C3C3B"
BEIGE = "#EBEBD3"
NAPELS_YELLOW = "#F5D547"
RAZZMATZZ_RED = "#DB3069"
COBALT_BLUE = "#1446A0"
TRANSPARENT = "transparent"

FONT_NAME = "Courier"
WORK_TIME = 25
SHORT_BREAK_TIME = 5
LONG_BREAK_TIME = 20
WIDTH = HEIGHT = 500

# Global Variables
reps = 1
timer = '' # Not using None because CTk.after_cancel() expects a string

# ------------------------ Helper Functions ------------------------
def playsound(path):
    winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)

def bring_to_front():
    app.update_idletasks()  # Ensure state is up to date
    app.deiconify()  # Restore if minimized
    app.state('normal')  # Make sure it’s not minimized or hidden
    app.lift()  # Raise above all other windows
    app.attributes('-topmost', True)  # Temporarily set as topmost
    # app.after(500, lambda: app.attributes('-topmost', False))  # Revert topmost
    app.after(500, app.attributes, '-topmost', False)
    app.focus_force()  # Grab keyboard focus


# ------------------------ Timer Reset ------------------------

def reset_rep():
    global reps, timer
    reps = 1
    app.after_cancel(timer)
    timer_text.configure(text="Timer", text_color=BEIGE)
    checkmark.configure(text='')
    canvas.itemconfig(image_timer, text="00:00")

# ------------------------ Timer Mechanism ------------------------

def start_timer():
    global reps
    work_seconds = WORK_TIME * 60
    short_break_seconds = SHORT_BREAK_TIME * 60
    long_break_seconds = LONG_BREAK_TIME * 60

    bring_to_front()

    if reps % 2 != 0:
        playsound("start timer.wav")
        count_down(work_seconds)
        timer_text.configure(text="Working", text_color=RAZZMATZZ_RED)
    elif reps % 2 == 0 and reps != 8:
        playsound("start break.wav")
        count_down(short_break_seconds)
        timer_text.configure(text="Break", text_color=COBALT_BLUE)
    elif reps == 8:
        playsound("start break.wav")
        count_down(long_break_seconds)
        timer_text.configure(text="Break", text_color=COBALT_BLUE)

    reps += 1


# ------------------------ Countdown Mechanism ------------------------

def count_down(count = 0):
    global reps
    mins = count // 60
    seconds = count % 60

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(image_timer, text=f"{mins}:{seconds}")
    if count > 0:
        global timer
        timer = app.after(10, count_down, count-1)
    else:
        if reps <= 8:
            start_timer()
            if reps % 2 != 0:
                checkmark.configure(text="✔" * (reps//2))
        else:
            app.after(2000, reset_rep)
# ------------------------ UI Setup ------------------------

set_appearance_mode("dark")
# set_default_color_theme("blue")

app = CTk()
app.title("Pomodoro")
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)
app.config(bg=ONYX, padx=40)


# Creating Canvas
canvas = CTkCanvas(master=app, width=256, height=256, bg=ONYX, highlightthickness=0)
# Getting tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(128, 128, image=tomato_img)
# Creating text on image
image_timer = canvas.create_text(128, 150, text="00:00", fill=NAPELS_YELLOW, font=(FONT_NAME, 24, 'bold'))
# Placing canvas on screen
canvas.grid(column=1, row=1)


# Creating main label
timer_text = CTkLabel(master=app, text="Timer", font=(FONT_NAME, 50, "bold"), text_color=BEIGE, bg_color=ONYX, pady=30)
# Placing the timer label
timer_text.grid(column=1, row=0)

# Creating the start and reset button
start_button = CTkButton(master=app, text="Start", text_color="Black", hover_color=NAPELS_YELLOW, fg_color=TRANSPARENT , corner_radius=10, width=20, bg_color=ONYX, border_color=RAZZMATZZ_RED, border_width=2, font=(FONT_NAME, 20, "bold"), command=start_timer)
reset_button = CTkButton(master=app, text="Reset", text_color="Black", hover_color=NAPELS_YELLOW, fg_color= TRANSPARENT, corner_radius=10, width=10, bg_color=ONYX, border_color=RAZZMATZZ_RED, border_width=2, font=(FONT_NAME, 20, "bold"), command=reset_rep)
# Placing the buttons
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

# Creating the checkmark
checkmark = CTkLabel(master=app, text="", bg_color=ONYX, text_color=RAZZMATZZ_RED)
checkmark.grid(column=1, row=3)









app.mainloop()
