
from customtkinter import *

# ********************************* Constants ********************************* #
API_KEY_ALPHA = "R18OQQGKQJO7CQ8D"
API_KEY_NEWS = "238af1d7e8844fbe9c2a0769339e2d41"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

LIGHT_GREEN = "#97CC04"
GREEN = "#306B34"
ORANGE = "#F45D01"
PURPLE = "#49416D"
GREY = "#6F686D"
TRANSPARENT = "transparent"
CANVAS_TITLE_FONT = ("ubuntu condensed extra bold", 25, "bold")
NEWS_TITLE_FONT = ("ubuntu condensed extra bold", 40, "bold")
CONTENT_FONT = ("URW Bookman Demi", 10, "bold")

# ********************************* UI Setup ********************************* #
app = CTk()
app.minsize(width=1280, height=720)
app.maxsize(width=1280, height=720)
set_appearance_mode("dark")


# Creating Required Widgets

# Canvases
canvas_left = CTkCanvas(master=app, width=500, height=500, bg=PURPLE, highlightthickness=0, takefocus=False, cursor="circle")
title_left_canvas = canvas_left.create_text(250, 50, fill="white", text="Yesterday Closing Price", font=CANVAS_TITLE_FONT)
content_left_canvas = canvas_left.create_text(250, 250, fill="white", text="Content", font=CONTENT_FONT)

canvas_right = CTkCanvas(master=app, width=500, height=500, bg=PURPLE, highlightthickness=0, takefocus=False, cursor="circle")
title_right_canvas = canvas_right.create_text(250, 50, fill="white", text="Yesterday+ Closing Price", font=CANVAS_TITLE_FONT)
content_right_canvas = canvas_right.create_text(250, 250, fill="white", text="Content", font=CONTENT_FONT)

canvas_news = CTkCanvas(master=app, width=1000, height=300, bg=PURPLE, highlightthickness=0, takefocus=False, cursor="circle")
title_news_canvas = canvas_news.create_text(500, 50, fill="white", text="News", font=NEWS_TITLE_FONT)
content_news_canvas = canvas_news.create_text(500, 150, fill="white", text="This Is Where Content Will Go", font=CONTENT_FONT)

# Buttons
get_news_button = CTkButton(master=app, text="Get News", width=500, height=50, fg_color=TRANSPARENT, bg_color=GREEN, hover_color=ORANGE)

canvas_left.grid(row=0, column=0)
canvas_right.grid(row=0, column=2, columnspan=2)
canvas_news.grid(row=3, column=0, columnspan=4)

# Main loop
app.mainloop()


