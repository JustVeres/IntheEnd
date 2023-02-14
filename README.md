# Автотест для дипломного проекта.

**Андрей Коротнев — 1-я когорта, дипломный проект.**

### Примечание:
- Для запуска тестов должны быть установлены пакеты **pytest** и **requests**.
- В коде остались закомментированные строки для проверки работоспособности моего кода.

### Запуск автотеста:
- Запустить сервер Яндекс Прилавка.
- Сгенерированный url скопировать и вставить в **for_request.py** в параметр **URL** (пример: URL = "https://cbea6ecc-a388-4a18-b33d-05e39be6b0e7.serverhub.praktikum-services.ru" **ВАЖНО**: без знака / в конце).
- Открыть вкладку с файлом **for_test.py**.
- Открыть **Terminal** и вставить значение: **pytest for_test.py**

### Видеоотчёт:
Видеодемонстрация моей работы: https://disk.yandex.ru/i/lgKUe4Du9HD6Jw

На видео продемонстрировано:
- Выполняется запрос на создание заказа.
- Сохраняется номер трека заказа.
- Выполняется запрос на получение заказа по треку того же заказа.
- Вручную ввёл несуществующий трек, чтобы убедеиться, что тест правильно реагирует на такой сценарий.
- Проверил, что код ответа равен 200 с правильным треком.

### Логи:
error.log
- https://disk.yandex.ru/i/dsRVX4azl7rcSw
- https://disk.yandex.ru/d/gjvTGqO-Pe7jnA

info.log
- https://disk.yandex.ru/i/9J-yR0fWehOmsA
- https://disk.yandex.ru/d/0CgmjiLiuEw7Sw