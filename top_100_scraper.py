import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import font as tkfont
import ttkbootstrap as tb
from datetime import date


class Top100Scraper:
    def __init__(self):
        self.date = "1998-12-03"
        self.url = f"https://www.billboard.com/charts/hot-100/{self.date}/"

    def set_date(self, date_obj):
        day = str(date_obj.day)
        month = str(date_obj.month)
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
        self.date = f"{date_obj.year}-{month}-{day}"
        self.url = f"https://www.billboard.com/charts/hot-100/{self.date}/"

    def scrape_top_100(self, date_obj):
        self.set_date(date_obj)

        response = requests.get(self.url)
        html = response.text

# #post-1479786 > div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > div:nth-child(3) > ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.lrv-u-padding-l-050.lrv-u-padding-l-1\@mobile-max > span
# #post-1479786 > div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.lrv-u-padding-l-050.lrv-u-padding-l-1\@mobile-max > span

        soup = BeautifulSoup(html, "html.parser")
        soup_song_titles = soup.select(selector="div ul li ul li h3")
        soup_song_authors = soup.select(".c-label.a-no-trucate")
        songs = {
        }

        for x in range(len(soup_song_titles)):
            soup_song_title = soup_song_titles[x]
            song_title = soup_song_title.get_text().replace("\n", "").strip()

            try:
                soup_song_author = soup_song_authors[x]
                song_author = soup_song_author.get_text().replace("\n", "").strip()
            except:
                song_author = "-"

            songs[song_title] = song_author

            print(song_title + "   " + song_author)

        return songs

