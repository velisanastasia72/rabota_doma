const library = {
    name: "Моя Библиотека",
    books: [],
    readers: [],
    
    addBook(title, author, year) {
        if (typeof title === 'string' && typeof author === 'string' && typeof year === 'number') {
            this.books.push({
                title: title,
                author: author,
                year: year,
                isAvailable: true
            });
            console.log(`Книга "${title}" добавлена в библиотеку.`);
        } else {
            console.log("Ошибка: Неверные аргументы для добавления книги.");
        }
    },
    
    borrowBook(title, readerName) {
        const book = this.books.find(book => book.title === title);
        if (!book) {
            console.log("Предупреждение: Книга не найдена в библиотеке.");
            return;
        }
        if (!book.isAvailable) {
            console.log("Книга уже на руках.");
            return;
        }
        
        if (!this.readers.includes(readerName)) {
            this.readers.push(readerName);
        }
        
        book.isAvailable = false;
        console.log(`Книга "${title}" выдана читателю "${readerName}".`);
    },
    
    returnBook(title) {
        const book = this.books.find(book => book.title === title);
        if (!book) {
            console.log("Ошибка: Книга не найдена в библиотеке.");
            return;
        }
        if (book.isAvailable) {
            console.log("Ошибка: Книга уже доступна.");
            return;
        }
        
        book.isAvailable = true;
        console.log(`Книга "${title}" возвращена в библиотеку.`);
    },
    
    getAvailableBooks() {
        return this.books
            .filter(book => book.isAvailable)
            .map(book => book.title);
    },
    
    getBooksByAuthor(author) {
        return this.books
            .filter(book => book.author === author)
            .map(book => book.title);
    },
    
    printStatus() {
        const totalBooks = this.books.length;
        const availableBooks = this.getAvailableBooks().length;
        const totalReaders = this.readers.length;
        
        console.log(`Общее количество книг: ${totalBooks}`);
        console.log(`Количество доступных книг: ${availableBooks}`);
        console.log(`Количество читателей: ${totalReaders}`);
        console.log(`Список доступных книг: ${this.getAvailableBooks().join(', ')}`);
    }
};

// Примеры использования
library.addBook("1984", "Джордж Оруэлл", 1949);
library.addBook("Моби Дик", "Герман Мелвилл", 1851);
library.borrowBook("1984", "Иван");
library.printStatus();
library.returnBook("1984");
library.printStatus();
