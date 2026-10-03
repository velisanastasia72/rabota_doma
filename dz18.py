import re


def find_emails():
    text = "12345@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"

    pattern = r'[a-zA-Zа-яА-ЯёЁ0-9._-]+@[a-zA-Zа-яА-ЯёЁ0-9.-]+'

    emails = re.findall(pattern, text)

    print(emails)


if __name__ == "__main__":
    find_emails()