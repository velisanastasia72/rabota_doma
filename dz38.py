import csv


FILENAME = "network_devices.csv"


def create_csv():

    data = [
        ["hostname", "vendor", "model", "location"],
        ["sw1", "Cisco", "3750", "London"],
        ["sw2", "Cisco", "3850", "Liverpool"],
        ["sw3", "Cisco", "3650", "Liverpool"],
        ["sw4", "Cisco", "3650", "London"]
    ]


    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(data)

    print(f"Файл '{FILENAME}' успешно создан.")


def read_and_print_csv():
    print("\n--- Чтение данных из файла ---")

    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')


        for row in reader:
            print(row)



if __name__ == '__main__':

    create_csv()


    read_and_print_csv()