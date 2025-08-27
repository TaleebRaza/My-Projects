# Importing Modules
import pandas

from random import choice
from customtkinter import *
from tkinter import PhotoImage, messagebox

# ------------------------- Constants ------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
WIDTH = 850 ; HEIGHT = 600

# ------------------------- Panda Implementation ------------------------- #

def get_data():
    for filename in ["data/words_to_learn.csv", "data/french_words.csv"]:
        try:
            return pandas.read_csv(filename).to_dict(orient="records")
        except (FileNotFoundError, pandas.errors.EmptyDataError):
            continue

    messagebox.showinfo(title="No Data", message="Get a Data File to Play With First.")
    exit()

data = get_data()

# ------------------------- Global Variables ------------------------- #
current_card = {}
flip_timer = None
easter_egg = 0
# ------------------------- Helper Functions ------------------------- #

# ------------------------- Main Functions ------------------------- #
def next_word():
    global current_card, flip_timer
    if flip_timer is not None:
        app.after_cancel(flip_timer)

    try:
        current_card = choice(data)
    except IndexError:
        canvas.itemconfig(upper_canvas_text, text="Learned All The Words")
        canvas.itemconfig(lower_canvas_text, text="Close Me Now")
    else:
        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(upper_canvas_text, text="French", fill="black")
        canvas.itemconfig(lower_canvas_text, text=current_card["French"], fill="black")
        flip_timer = app.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(upper_canvas_text, text="English", fill="white")
    canvas.itemconfig(lower_canvas_text, text=current_card["English"], fill="white")

def is_known():
    global easter_egg
    try:
        data.remove(current_card)
    except ValueError:
        if easter_egg <= 10:
            canvas.itemconfig(upper_canvas_text, text="There Are No More Words")
            canvas.itemconfig(lower_canvas_text, text="Idiot")
            app.after(1500, next_word)
            easter_egg += 1
        else:
            canvas.itemconfig(upper_canvas_text, text="Can't You Read?")
            canvas.itemconfig(lower_canvas_text, text="Use Your Brain!\nClose Me Now")
            easter_egg = 0
    else:
        to_learn = pandas.DataFrame(data).to_csv("data/words_to_learn.csv")
        print(len(data))
        next_word()

def play_again():
    global data, current_card
    try:
        file = open("data/words_to_learn.csv", mode="r+")
        file.truncate(0)
    except FileNotFoundError:
        canvas.itemconfig(upper_canvas_text, text="Why?")
        canvas.itemconfig(lower_canvas_text, text="Learn First")
        app.after(1500, next_word)
    else:
        file.close()
        data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

# ------------------------- UI Setup ------------------------- #
app = CTk()
set_appearance_mode("dark")
app.minsize(width=WIDTH, height=HEIGHT)
app.title(string="Flashy")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")

# Creating canvas and canvas items
canvas = CTkCanvas(master=app, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 260, image=card_front)

upper_canvas_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
lower_canvas_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Placing canvas
canvas.grid(column=0, row=0, columnspan=2)

# Creating buttons
right_button = CTkButton(master=app, image=right_button_image, text='', bg_color=BACKGROUND_COLOR, fg_color=BACKGROUND_COLOR, hover=False, command=is_known)
wrong_button = CTkButton(master=app, image=wrong_button_image, text='', bg_color=BACKGROUND_COLOR, fg_color=BACKGROUND_COLOR, hover=False, command=next_word)
play_again_button = CTkButton(master=app, width=300, text='Play Again', bg_color=BACKGROUND_COLOR, fg_color=BACKGROUND_COLOR, text_color="black", corner_radius=20, border_color="black", border_width=2, hover_color="#8338ec", command=play_again)

# Placing the buttons
right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)
play_again_button.grid(column=0, row=2, columnspan=2)

next_word()
# Main loop
app.mainloop()
