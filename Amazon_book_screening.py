import csv
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Book:
    def __init__(self, ):
        self.name = ''
        # 2 locations - under product description or click read more
        self.description = ''
        self.star_rating = 0
        self.five_stars = 0
        self.four_stars = 0
        self.three_stars = 0
        self.two_stars = 0
        self.one_stars = 0
        self.review = ''
        # regular price on front page
        self.price = 0
        self.kindle_price = 0
        self.paperback_price = 0
        # print length
        self.page_num = ''
        # reading age - maybe listed under product info or title
        self.reading_age = ''
        self.publication_date = ''
        self.dimensions = ''
        self.language = ''
        # ISBN - International Standard Book Number
        # ISBN 10 was the system that was used earlier whereas ISBN 13 is the new system.
        self.ISBN_10 = ''
        self.ISBN_13 = ''
        # best sellers rank under product details
        self.rank = ''
        # About the author - bottom of the page
        self.author = ''




