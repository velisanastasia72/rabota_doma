class Liquid:


    def __init__(self, name, density):
        self.name = name
        self.density = density

    def change_density(self, new_density):
        self.density = new_density

    def calc_volume(self, mass):
        return mass / self.density

    def calc_mass(self, volume):
        return volume * self.density

    def display_info(self):
        print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")


class Alcohol(Liquid):

    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def change_strength(self, new_strength):
        self.strength = new_strength



if __name__ == '__main__':
    wine = Liquid('Wine', 1064.2)

    wine.display_info()


    wine.change_density(1000)
    wine.display_info()

    print(f"\nВес 0.5 m^3 of Wine составляет {wine.calc_mass(0.5)} кг.")
    print(f"Объем 300 кг Wine равен {wine.calc_volume(300)} m^3.")

    print("\n--- Тест класса Alcohol ---")
    spirit = Alcohol('Vodka', 789, 40)
    print(f"Создан: {spirit.name}, Крепость: {spirit.strength}%")

    spirit.change_strength(45)
    print(f"Новая крепость: {spirit.strength}%")