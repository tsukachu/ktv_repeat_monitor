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
        return self.article.select_one(OnAirScheduleLocators.title).get_text(strip=True)

    def get_schedules(self):
        schedules = self.article.select(OnAirScheduleLocators.schedule)
        result = []
        for schedule in schedules:
            on_air = schedule.select_one(OnAirScheduleLocators.on_air).get_text(
                strip=True
            )
            episode = schedule.select_one(OnAirScheduleLocators.episode).get_text(
                strip=True
            )
            result.append({"on_air": on_air, "episode": episode})

        return result
