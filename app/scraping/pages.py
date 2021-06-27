from collections import deque
from datetime import datetime

import pytz
from bs4 import BeautifulSoup
from simple_settings import settings

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
        title = self.article.select_one(OnAirScheduleLocators.title).get_text(
            strip=True
        )
        title, _ = title.split("（")
        return title

    def get_schedules(self):
        schedules = self.article.select(OnAirScheduleLocators.schedule)
        result = []
        for schedule in schedules:
            on_air = schedule.select_one(OnAirScheduleLocators.on_air).get_text(
                strip=True
            )
            start, end = self.on_air_str_to_datetime(on_air)
            episode = schedule.select_one(OnAirScheduleLocators.episode).get_text(
                strip=True
            )
            result.append({"start": start, "end": end, "episode": episode})

        return result

    def on_air_str_to_datetime(self, on_air):
        """parse した日時を aware な datetime にする

        TODO: 良い方法が思い付かず、かなり強引な処理なのでリファクタしたい

        Args:
          on_air: str
                  %m月%d日（%a）%p%I:%M～%I:%M, e.g. 6月22日（火）午後3：45～4：45
                  %a は locale.LC_TIME を "ja_JP.UTF-8" にしないと parse 出来ない
                  %p は locale を変更しても parse 出来なかった

        Returns:
          on_air は '開始時刻～終了時刻' になってるので start, end と分けて返す

          start: datetime(aware)
          end: datetime(aware)
        """
        # 再放送は午後なのでひとまず固定
        pm = {
            "en": "PM",
            "ja": "午後",
        }
        connector = "～"
        fmt = "%m月%d日%p%I：%M"
        jst = pytz.timezone(settings.TIME_ZONE)

        index = on_air.find(pm["ja"])
        date = on_air[:index]  # %m月%d日（%a）
        date = date[:-3]  # %m月%d日

        start, end = on_air[index:].split(connector)  # start: 午後%I：%M, end: %I：%M
        _, start = start.split(pm["ja"])  # start: %I：%M

        start = pm["en"].join([date, start])  # %m月%d日PM%I：%M
        end = pm["en"].join([date, end])

        now = datetime.now(jst)

        # year は on_air から取得出来ないので現在日時に replace する
        start = datetime.strptime(start, fmt).replace(year=now.year)  # native
        end = datetime.strptime(end, fmt).replace(year=now.year)  # native

        # replace で tzinfo を jst に変更すると 19 分ズレるので localize を使う
        start = jst.localize(start)  # aware, jst
        end = jst.localize(end)  # aware, jst

        return start, end
