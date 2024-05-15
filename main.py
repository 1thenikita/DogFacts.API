import requests
from translate import Translator


def start():
    url = "http://dog-api.kinduff.com/api/facts"
    translator: Translator = Translator(from_lang='english', to_lang='russian')
    numb = input("Введите число (по желанию)")
    print("Получаем ответ от API...")
    link = (url + "?number=" + numb if numb != None else url)
    response: requests.Response = requests.get(url=link)
    if response.status_code == 200:
        resp: dict = response.json()
        facts: str = resp['facts']
        print(f"Факт: {translator.translate(';'.join(facts))}")
    else:
        if response.json().get('success') == "true":
            print("Ошибка в API!")
        else:
            print(f"Ошибка {response.status_code}.")


if __name__ == '__main__':
    start()