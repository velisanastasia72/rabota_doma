import random
import string


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def create_phone_book(count=5):
    phone_book = {}

    for _ in range(count):
        user_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])


        name = generate_random_string(8)


        tel = ''.join([str(random.randint(0, 9)) for _ in range(10)])


        phone_book[user_id] = {
            "name": name,
            "tel": tel
        }

    return phone_book



if __name__ == '__main__':

    data = create_phone_book()


    import json


    print(json.dumps(data, indent=4))