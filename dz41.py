import json
import os



class Movie:

    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Movie(**data)


class MovieCatalog:

    def __init__(self, filename="movies_db.json"):
        self.filename = filename
        self.movies = []
        self.load_data()

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_data()

    def get_all_movies(self):
        return self.movies

    def get_movie_by_index(self, index):
        if 0 <= index < len(self.movies):
            return self.movies[index]
        return None

    def delete_movie(self, index):
        if 0 <= index < len(self.movies):
            removed = self.movies.pop(index)
            self.save_data()
            return removed
        return None

    def save_data(self):
        data = [m.to_dict() for m in self.movies]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.movies = [Movie.from_dict(item) for item in data]



class MovieView:

    @staticmethod
    def show_menu():
        print("\n===== Редактирование данных каталога фильмов =====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")
        print("=" * 50)

    @staticmethod
    def get_input(prompt):
        return input(prompt).strip()

    @staticmethod
    def show_movie_list(movies):
        if not movies:
            print("Каталог пуст.")
            return
        print(f"\n{'№':<4} {'Название':<30} {'Год':<6} {'Жанр':<15}")
        print("-" * 60)
        for i, movie in enumerate(movies):
            print(f"{i + 1:<4} {movie.title:<30} {movie.year:<6} {movie.genre:<15}")

    @staticmethod
    def show_movie_details(movie):
        print("\n--- Информация о фильме ---")
        print(f"Название:    {movie.title}")
        print(f"Жанр:        {movie.genre}")
        print(f"Режиссер:    {movie.director}")
        print(f"Год выпуска: {movie.year}")
        print(f"Длительность:{movie.duration} мин.")
        print(f"Студия:      {movie.studio}")
        print(f"Актеры:      {movie.actors}")
        print("-" * 30)

    @staticmethod
    def show_message(message):
        print(f"\n>>> {message}")




class MovieController:
    def __init__(self):
        self.catalog = MovieCatalog()
        self.view = MovieView()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Выберите вариант действия: ")

            if choice == '1':
                self.add_movie_flow()
            elif choice == '2':
                self.show_catalog_flow()
            elif choice == '3':
                self.view_movie_flow()
            elif choice == '4':
                self.delete_movie_flow()
            elif choice.lower() == 'q':
                self.view.show_message("Выход из программы. До свидания!")
                break
            else:
                self.view.show_message("Неверный выбор, попробуйте снова.")

    def add_movie_flow(self):
        print("\n--- Добавление нового фильма ---")
        title = self.view.get_input("Название фильма: ")
        genre = self.view.get_input("Жанр: ")
        director = self.view.get_input("Режиссер: ")
        year = self.view.get_input("Год выпуска: ")
        duration = self.view.get_input("Длительность (мин): ")
        studio = self.view.get_input("Студия: ")
        actors = self.view.get_input("Актеры (через запятую): ")

        new_movie = Movie(title, genre, director, year, duration, studio, actors)
        self.catalog.add_movie(new_movie)
        self.view.show_message(f"Фильм '{title}' успешно добавлен!")

    def show_catalog_flow(self):
        movies = self.catalog.get_all_movies()
        self.view.show_movie_list(movies)

    def view_movie_flow(self):
        movies = self.catalog.get_all_movies()
        if not movies:
            self.view.show_message("Каталог пуст. Добавьте фильмы.")
            return

        self.view.show_movie_list(movies)
        try:
            idx = int(self.view.get_input("Введите номер фильма для просмотра: ")) - 1
            movie = self.catalog.get_movie_by_index(idx)
            if movie:
                self.view.show_movie_details(movie)
            else:
                self.view.show_message("Фильм с таким номером не найден.")
        except ValueError:
            self.view.show_message("Ошибка: нужно ввести число.")

    def delete_movie_flow(self):
        movies = self.catalog.get_all_movies()
        if not movies:
            self.view.show_message("Каталог пуст.")
            return

        self.view.show_movie_list(movies)
        try:
            idx = int(self.view.get_input("Введите номер фильма для удаления: ")) - 1
            removed = self.catalog.delete_movie(idx)
            if removed:
                self.view.show_message(f"Фильм '{removed.title}' удален.")
            else:
                self.view.show_message("Фильм с таким номером не найден.")
        except ValueError:
            self.view.show_message("Ошибка: нужно ввести число.")


if __name__ == '__main__':
    app = MovieController()
    app.run()