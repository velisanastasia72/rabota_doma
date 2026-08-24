function greet(name) {
    // Убираем лишние пробелы и приводим к строке
    const trimmedName = name.trim();
    // Приводим первую букву к заглавной, остальные к строчным
    const capitalized = trimmedName.charAt(0).toUpperCase() + trimmedName.slice(1).toLowerCase();
    return `Привет, ${capitalized}!`;
}

// Пример использования
console.log(greet(" настя ")); // "Привет, Настя!"


function isNumeric(str) {
    // Регулярное выражение для проверки числа
    return /^-?\d+(\.\d+)?$/.test(str);
}

// Примеры использования
console.log(isNumeric("123"));      // true
console.log(isNumeric("-45.6"));    // true
console.log(isNumeric("abc"));      // false


function maskEmail(email) {
    const [localPart, domain] = email.split('@');
    if (localPart.length <= 2) return email; // Если локальная часть слишком короткая

    const firstChar = localPart.charAt(0);
    const lastChar = localPart.charAt(localPart.length - 1);
    const maskedPart = '*'.repeat(localPart.length - 2);
    
    return `${firstChar}${maskedPart}${lastChar}@${domain}`;
}

// Пример использования
console.log(maskEmail("alexander.shumakov@example.com")); // a**************v@example.com


function isPalindrome(str) {
    // Убираем все не буквенно-цифровые символы и приводим к нижнему регистру
    const cleanedStr = str.replace(/[\W_]/g, '').toLowerCase();
    // Проверяем, является ли строка палиндромом
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

// Примеры использования
console.log(isPalindrome("А роза упала на лапу Азора")); // true
console.log(isPalindrome("hello"));                       // false


