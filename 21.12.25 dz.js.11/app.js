document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('generator-form');
    const input = document.getElementById('max-value');
    const resultBox = document.getElementById('result');

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        handleGenerate();
    });

    function handleGenerate() {
        const rawValue = input.value.trim();

        // 1. Проверка на пустое поле
        if (rawValue === '') {
            showError('Введите корректное целое число');
            return;
        }

        // 2. Преобразование и проверка на число
        const parsed = Number(rawValue);

        if (
            Number.isNaN(parsed) ||          // не число (буквы, спецсимволы)
            !Number.isFinite(parsed) ||      // бесконечность
            !Number.isInteger(parsed) ||     // дробное число
            parsed < 0                       // отрицательное число
        ) {
            showError('Введите корректное целое число');
            return;
        }

        // 3. Генерация случайного числа от 0 до N включительно
        const n = parsed;
        const randomValue = Math.floor(Math.random() * (n + 1));

        showSuccess(randomValue, n);
    }

    function showError(message) {
        resultBox.className = 'result error';
        resultBox.textContent = message;
    }

    function showSuccess(value, n) {
        resultBox.className = 'result success';
        resultBox.innerHTML =
            `Случайное число от 0 до ${n}:<span class="number">${value}</span>`;
    }
});