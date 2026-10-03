class Student:


    class Laptop:
        def __init__(self, model, processor, ram):
            self.model = model
            self.processor = processor
            self.ram = ram

        def get_info(self):
            return f"{self.model}, {self.processor}, {self.ram}"

    def __init__(self, name, laptop_model, laptop_processor, laptop_ram):
        self.name = name
        self.laptop = self.Laptop(laptop_model, laptop_processor, laptop_ram)

    def display_info(self):
        print(f"{self.name} => {self.laptop.get_info()}")


if __name__ == '__main__':
    roman = Student("Roman", "HP", "i7", 16)
    vladimir = Student("Vladimir", "HP", "i7", 16)


 # вывод
    roman.display_info()
    vladimir.display_info()