import datetime
from bs4 import BeautifulSoup
import requests
from plyer import notification
from dotenv import load_dotenv
import os

load_dotenv()


class API:
    url = "https://random-words5.p.rapidapi.com/getRandom"
    headers = {
        "X-RapidAPI-Key": os.getenv("KEY"),
        "X-RapidAPI-Host": os.getenv("HOST"),
    }

    def get_word(self):
        return requests.request("GET", self.url, headers=self.headers).text

    def word(self):
        word = self.get_word()
        d = requests.get(f'https://www.dictionary.com/browse/{word}')
        soup = BeautifulSoup(d.text, 'html.parser')
        ps = [p.text for p in soup.find_all(
            'span', {'class': 'one-click-content css-nnyc96 e1q3nk1v1'})]
        return f'{word} : {ps[:1]}'


if __name__ == "__main__":
    notification.notify(
        title="Word of the day",
        message=API().word(),
        app_icon=None,
        timeout=10,
    )

    while True:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        match time:
            case "10:00:00":

                notification.notify(
                    title="Word of the day",
                    message=API().word(),
                    app_icon=None,
                    timeout=10,
                )
            case "13:00:00":

                notification.notify(
                    title="Word of the day",
                    message=API().word(),
                    app_icon=None,
                    timeout=10,
                )
            case "16:00:00":

                notification.notify(
                    title="Word of the day",
                    message=API().word(),
                    app_icon=None,
                    timeout=10,
                )
            case "19:00:00":
                notification.notify(
                    title="Word of the day",
                    message=API().word(),
                    app_icon=None,
                    timeout=10,
                )
            case "21:00:00":
                notification.notify(
                    title="Word of the day",
                    message=API().word(),
                    app_icon=None,
                    timeout=10,
                )
