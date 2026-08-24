function printEntries(arr) {
    arr.forEach((value, index) => {
        console.log(`Индекс ${index}: ${value}`);
    });
}

// Пример использования
printEntries(['яблоко', 'груша']);


function getEvenIndexedValues(arr) {
    return Array.from(arr.entries())
        .filter(([index]) => index % 2 === 0)
        .map(([, value]) => value);
}

// Пример использования
console.log(getEvenIndexedValues(['a', 'b', 'c', 'd', 'e'])); // → ['a', 'c', 'e']


function logUserNames(users) {
    users.forEach(user => {
        console.log(user.имя);
    });
}

// Пример использования
logUserNames([{ имя: "Аня", возраст: 25 }, { имя: "Боря", возраст: 30 }]);


function countByRole(users, stats) {
    users.forEach(user => {
        stats[user.роль] = (stats[user.роль] || 0) + 1;
    });
}

// Пример использования
const stats = {};
countByRole([
    { имя: "Аня", роль: "админ" },
    { имя: "Боря", роль: "пользователь" },
    { имя: "Вася", роль: "админ" }
], stats);
console.log(stats); // { админ: 2, пользователь: 1 }


function getSquares(numbers) {
    return numbers.map(num => num * num);
}

// Пример использования
console.log(getSquares([1, 2, 3])); // → [1, 4, 9]


function getOrderTotals(заказы) {
    return заказы.map(order => {
        const итог = order.товары.reduce((sum, item) => sum + item.цена, 0);
        return { id: order.id, итог };
    });
}

// Пример использования
const заказы = [
    { id: 1, товары: [{ цена: 100 }, { цена: 50 }] },
    { id: 2, товары: [{ цена: 200 }] }
];
console.log(getOrderTotals(заказы)); // → [{ id: 1, итог: 150 }, { id: 2, итог: 200 }]


function getAdults(люди) {
    return люди.filter(person => person.возраст >= 18);
}

// Пример использования
console.log(getAdults([{ имя: "Аня", возраст: 16 }, { имя: "Боря", возраст: 20 }])); // → [{ имя: "Боря", возраст: 20 }]


function getUniqueTags(tags) {
    return tags.filter(tag => tags.indexOf(tag) === tags.lastIndexOf(tag));
}

// Пример использования
console.log(getUniqueTags(['js', 'react', 'js', 'python', 'react'])); // → ['python']
