from collections import deque

from bs4 import BeautifulSoup

from app.scraping.locators import OnAirScheduleLocators


class BasePage:
    def __init__(self, session):
        self.session = session

    def get(self):
        response = self.session.get(self.url)
        self.soup = BeautifulSoup(response.text, "lxml")


class OnAirSchedulePage(BasePage):
    url = "https://www.ktv.jp/repeat/"

    def parse(self):
        articles = self.soup.select(OnAirScheduleLocators.article)
        self.articles = deque(articles)

    @property
    def has_next(self):
        return len(self.articles) != 0

    def pop(self):
        self.article = self.articles.popleft()

    def get_title(self):
        return self.article.select_one(OnAirScheduleLocators.title).string
