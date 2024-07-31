from tkinter import *
from tkinter import font as tkfont
import ttkbootstrap as tb
from datetime import date
import time
from top_100_scraper import Top100Scraper

class UIMethods:

    @staticmethod
    def center_window(w, h, win, push_y=0, push_x=0):
        x_coordinate = int((win.winfo_screenwidth() / 2) - (w / 2)) + push_x
        y_coordinate = int((win.winfo_screenheight() / 2) - (h / 2)) + push_y
        win.geometry(f"{w}x{h}+{x_coordinate}+{y_coordinate}")

    @staticmethod
    def get_date(date_entry):
        date_str = date_entry.entry.get()
        year_month_day = date_str.split("-")
        # year, month, day
        d = date(int(year_month_day[0]), int(year_month_day[1]), int(year_month_day[2]))
        return d

    @staticmethod
    def update_small_date_label(label, date_widget):
        d = UIMethods.get_date(date_widget)
        date_str = d.strftime('%A, %b %d')
        label.config(text=date_str)

    @staticmethod
    def update_big_date_label(label, date_obj):
        d = UIMethods.get_date(date_obj)
        date_str = d.strftime('%Y')
        label.config(text=date_str)

    @staticmethod
    def update_songs_labels(songs_dict, results_frame, h4, h3):

        # clear frame
        for child in results_frame.winfo_children():
            child.destroy()



        # making a scrollable frame
        canvas = tb.Canvas(results_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = tb.Scrollbar(results_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            '<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        results_second_frame = Frame(canvas, width=1000, height=1800)

        row = 0
        rank = 0
        for title in songs_dict:
            rank += 1
            new_label = tb.Label(results_second_frame, text=f"#{rank}  {title}", font=h3, wraplength=310)
            row += 1
            new_label.grid(row=row, column=0, sticky=W, padx=(30, 0))
            new_label_1 = tb.Label(results_second_frame, bootstyle="danger", text=songs_dict[title], font=h4, wraplength=310)
            row += 1
            new_label_1.grid(row=row, column=0, sticky=W, pady=(0, 15), padx=(30, 0))
        canvas.create_window((0, 0), window=results_second_frame, anchor="nw")

    @staticmethod
    def update_all_labels(year_label, day_month_label, date_entry, window, results_frame, h4, h3):
        UIMethods.update_small_date_label(day_month_label, date_entry)
        UIMethods.update_big_date_label(year_label, date_entry)

        scraper = Top100Scraper()
        songs_dict = scraper.scrape_top_100(UIMethods.get_date(date_entry))

        UIMethods.update_songs_labels(songs_dict, results_frame, h4, h3)
