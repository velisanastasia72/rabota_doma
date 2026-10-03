# class AccountA:
#
#
#     usd_rate = 90.0
#     eur_rate = 98.0
#
#     def __init__(self, owner, account_number, interest_rate, balance=0.0):
#
#         self.set_owner(owner)
#         self.set_account_number(account_number)
#         self.set_interest_rate(interest_rate)
#         self.set_balance(balance)
#
#         print(f"Счёт №{self.__account_number} открыт. Владелец: {self.__owner}.")
#
#
#
#     def get_owner(self):
#         return self.__owner
#
#     def get_account_number(self):
#         return self.__account_number
#
#     def get_interest_rate(self):
#         return self.__interest_rate
#
#     def get_balance(self):
#         return self.__balance
#
#
#     def set_owner(self, owner):
#         if isinstance(owner, str) and owner.strip():
#             self.__owner = owner
#         else:
#             print("Ошибка имя владельца должно быть непустой строкой")
#
#     def set_account_number(self, account_number):
#         if isinstance(account_number, (str, int)) and str(account_number).strip():
#             self.__account_number = str(account_number)
#         else:
#             print("некорректный номер счёта")
#
#     def set_interest_rate(self, interest_rate):
#         if isinstance(interest_rate, (int, float)) and not isinstance(interest_rate, bool) \
#                 and interest_rate >= 0:
#             self.__interest_rate = float(interest_rate)
#         else:
#             print("Ошибка процент должен быть неотрицательным числом")
#
#     def set_balance(self, balance):
#         if isinstance(balance, (int, float)) and not isinstance(balance, bool) \
#                 and balance >= 0:
#             self.__balance = float(balance)
#         else:
#             print("Ошибка баланс должен быть неотрицательным числом")
#
#
#     @classmethod
#     def set_usd_rate(cls, new_rate):
#         if isinstance(new_rate, (int, float)) and new_rate > 0:
#             cls.usd_rate = float(new_rate)
#         else:
#             print("Ошибка курс должен быть положительным числом")
#
#     @classmethod
#     def set_eur_rate(cls, new_rate):
#         if isinstance(new_rate, (int, float)) and new_rate > 0:
#             cls.eur_rate = float(new_rate)
#         else:
#             print("Ошибка курс должен быть положительным числом")
#
#
#     @staticmethod
#     def convert_to_usd(amount_rub):
#         return amount_rub / AccountA.usd_rate
#
#     @staticmethod
#     def convert_to_eur(amount_rub):
#         return amount_rub / AccountA.eur_rate
#
#
#     def change_owner(self, new_owner):
#         self.set_owner(new_owner)
#         print(f"Владелец счёта {self.__account_number} изменён на: {self.__owner}.")
#
#     def withdraw(self, amount):
#         if isinstance(amount, (int, float)) and amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"Снято {amount:.2f} руб. Новый баланс: {self.__balance:.2f} руб.")
#             else:
#                 print("Ошибка: недостаточно средств на счёте")
#         else:
#             print("Ошибка: сумма снятия должна быть положительным числом")
#
#     def deposit(self, amount):
#         if isinstance(amount, (int, float)) and amount > 0:
#             self.__balance += amount
#             print(f"Начислено {amount:.2f} руб. Новый баланс: {self.__balance:.2f} руб.")
#         else:
#             print("Ошибка сумма начисления должна быть положительным числом")
#
#     def accrue_interest(self):
#         percent_sum = self.__balance * self.__interest_rate / 100
#         self.__balance += percent_sum
#         print(f"Начислены проценты ({self.__interest_rate}%): +{percent_sum:.2f} руб. "
#               f"Новый баланс: {self.__balance:.2f} руб.")
#
#     def to_usd(self):
#         return self.__balance / AccountA.usd_rate
#
#     def to_eur(self):
#         return self.__balance / AccountA.eur_rate
#
#     def display_info(self):
#         print("\n Информация о счёте")
#         print(f"Владелец:       {self.__owner}")
#         print(f"Номер счёта:    {self.__account_number}")
#         print(f"Процент:        {self.__interest_rate}%")
#         print(f"Баланс (руб.):  {self.__balance:.2f}")
#         print(f"Баланс (USD):   {self.to_usd():.2f}")
#         print(f"Баланс (EUR):   {self.to_eur():.2f}")
#         print(f"Курс USD:       {AccountA.usd_rate}, Курс EUR: {AccountA.eur_rate}")
#
#
#
#
#     def __del__(self):
#         print(f"Банковский счёт №{self.__account_number} закрыт.")
#
#
#
# if __name__ == "__main__":
#     print("обычные геттеры/сеттеры\n")
#
#     acc = AccountA("Волков", "40615810", 5.0, 10500.0)
#
#
#     acc.display_info()
#
#
#     acc.deposit(5000)
#     acc.withdraw(3000)
#     acc.accrue_interest()
#     acc.change_owner("Волков")
#
#     print(f"Текущий владелец (через get_owner): {acc.get_owner()}")
#     print(f"Баланс в долларах (метод to_usd): {acc.to_usd():.2f} USD")
#
#     print(f"18000 руб. в долларах (стат. метод): {AccountA.convert_to_usd(18000):.2f} USD")
#
#     AccountA.set_usd_rate(95.0)
#     print(f"\nПосле изменения курса USD на 95:")
#     print(f"Баланс в долларах: {acc.to_usd():.2f} USD")
#
#     acc.set_balance(-500)
#
#     del acc




class AccountB:


    eur_rate = 98.0

    def __init__(self, owner, account_number, interest_rate, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = balance

        print(f"Счёт №{self.__account_number} открыт. Владелец: {self.__owner}.")



    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, str) and value.strip():
            self.__owner = value
        else:
            raise ValueError("Имя владельца должно быть непустой строкой.")



    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, (str, int)) and str(value).strip():
            self.__account_number = str(value)
        else:
            raise ValueError("Некорректный номер счёта.")



    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0:
            self.__interest_rate = float(value)
        else:
            raise ValueError("Процент должен быть неотрицательным числом.")



    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0:
            self.__balance = float(value)
        else:
            raise ValueError("Баланс должен быть неотрицательным числом.")



    @classmethod
    def set_usd_rate(cls, new_rate):
        if isinstance(new_rate, (int, float)) and new_rate > 0:
            cls.usd_rate = float(new_rate)
        else:
            print("Ошибка: курс должен быть положительным числом.")

    @classmethod
    def set_eur_rate(cls, new_rate):
        if isinstance(new_rate, (int, float)) and new_rate > 0:
            cls.eur_rate = float(new_rate)
        else:
            print("Ошибка: курс должен быть положительным числом.")


    @staticmethod
    def convert_to_usd(amount_rub):
        return amount_rub / AccountB.usd_rate

    @staticmethod
    def convert_to_eur(amount_rub):
        return amount_rub / AccountB.eur_rate



    def change_owner(self, new_owner):
        try:
            self.owner = new_owner  # присваивание через property-сеттер
            print(f"Владелец счёта №{self.__account_number} изменён на: {self.__owner}.")
        except ValueError as e:
            print(f"Ошибка смены владельца: {e}")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято {amount:.2f} руб. Новый баланс: {self.__balance:.2f} руб.")
            else:
                print("Ошибка: недостаточно средств на счёте.")
        else:
            print("Ошибка: сумма снятия должна быть положительным числом.")

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__balance += amount
            print(f"Начислено {amount:.2f} руб. Новый баланс: {self.__balance:.2f} руб.")
        else:
            print("Ошибка: сумма начисления должна быть положительным числом.")

    def accrue_interest(self):
        percent_sum = self.__balance * self.__interest_rate / 100
        self.__balance += percent_sum
        print(f"Начислены проценты ({self.__interest_rate}%): +{percent_sum:.2f} руб. "
              f"Новый баланс: {self.__balance:.2f} руб.")

    def to_usd(self):
        return self.__balance / AccountB.usd_rate

    def to_eur(self):
        return self.__balance / AccountB.eur_rate

    def display_info(self):
        print("\nИнформация о счёте ")
        print(f"Владелец:       {self.__owner}")
        print(f"Номер счёта:    {self.__account_number}")
        print(f"Процент:        {self.__interest_rate}%")
        print(f"Баланс (руб.):  {self.__balance:.2f}")
        print(f"Баланс (USD):   {self.to_usd():.2f}")
        print(f"Баланс (EUR):   {self.to_eur():.2f}")
        print(f"Курс USD:       {AccountB.usd_rate}, Курс EUR: {AccountB.eur_rate}")
        print("--------------------------\n")


    def __del__(self):
        print(f"Банковский счёт №{self.__account_number} закрыт.")




if __name__ == "__main__":
    print("\n########## ВАРИАНТ Б: @property ##########\n")


    acc = AccountB("Сидоров", "40817820", 7.5, 20000.0)
    acc.display_info()


    acc.deposit(10000)
    acc.withdraw(5000)
    acc.accrue_interest()
    acc.change_owner("Кузнецов")

    print(f"Текущий владелец (через property): {acc.owner}")
    print(f"Текущий баланс (через property): {acc.balance:.2f} руб.")
    print(f"Баланс в евро (метод to_eur): {acc.to_eur():.2f} EUR")

    acc.balance = 50000
    print(f"После прямого присваивания acc.balance = 50000: {acc.balance:.2f} руб.")

    try:
        acc.balance = -1000
    except ValueError as e:
        print(f"Защита сработала: {e}")


    print(f"27000 руб. в евро (стат. метод): {AccountB.convert_to_eur(27000):.2f} EUR")


    AccountB.set_eur_rate(100.0)
    print(f"\nПосле изменения курса EUR на 100:")
    print(f"Баланс в евро: {acc.to_eur():.2f} EUR")

    del acc