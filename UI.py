from tkinter import *
from tkinter import font as tkfont
import ttkbootstrap as tb
from UI_methods import UIMethods
from datetime import date

# Window Init
window = tb.Window(themename="cyborg")
window.title("Top 100 Time Machine")
window.iconbitmap("./Images/app_icon.ico")
UIMethods.center_window(400, 750, window, push_y=-30)

# Fonts
h1 = tkfont.Font(family="Futura", size=41)
h2 = tkfont.Font(family="Futura", size=30)
h3 = tkfont.Font(family="Futura", size=18)
h4 = tkfont.Font(family="Futura", size=13)
button_font_medium = tkfont.Font(family="Futura", size=13)

# Search Section
search_frame = tb.Frame(window,)
search_frame.pack(pady=30, padx=30)

search_label = tb.Label(search_frame,
                        text="Search Top 100",
                        font=h1)
search_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

date_entry = tb.DateEntry(search_frame, bootstyle="success", firstweekday=0,
                          startdate=date(1998, 12, 3),
                          dateformat="%Y-%m-%d", width=25)
date_entry.grid(row=1, column=0, padx=(0, 8), sticky=N+E+W+S)

my_style = tb.Style()
my_style.configure('info.Outline.TButton', font=button_font_medium)
button = tb.Button(search_frame, bootstyle="info", text="search",
                   command=lambda: UIMethods.update_all_labels(year_label, day_month_label, date_entry, window,
                                                               results_frame, h4, h3),
                    style="info.Outline.TButton")
button.grid(row=1, column=1)

# Week of Section
week_of_frame = tb.Frame(window, width=290)
week_of_frame.pack(padx=30)

the_week_of_label = tb.Label(week_of_frame, text="The week of...", font=h4, justify="left",
                             anchor="w")
the_week_of_label.grid(row=0, column=0)

year_label = tb.Label(week_of_frame, text="", font=h1)
year_label.grid(row=1, column=0)

day_month_label = tb.Label(week_of_frame, text="", font=h4)
day_month_label.grid(row=2, column=0)

results_frame = Frame(window)
results_frame.pack(fill=BOTH, expand=1, pady=(35, 0))

# Getting and displaying songs
UIMethods.update_all_labels(year_label, day_month_label, date_entry, window, results_frame, h4, h3)

# Create and run window loop
window.mainloop()

