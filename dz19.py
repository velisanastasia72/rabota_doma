# import re
#
#
# def password_check():
#
#
#     passwords = ['my-p@ssw0rd']
#
#     pattern = r'^[a-zA-Z0-9@_-]{6,18}$'
#
#
#     valid_passwords = [p for p in passwords if re.match(pattern, p)]
#
#     print(valid_passwords)
#
#
# password_check()
#
#
# def data_look():
#
#     text = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
#
#     pattern = r'\d{2}/\d{2}/\d{4}'
#
#     dates = re.findall(pattern, text)
#
#     print(dates)
#
# data_look()

