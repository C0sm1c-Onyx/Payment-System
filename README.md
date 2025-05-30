# Payment System

## Установка и настройка окружения
Склонируйте репозиторий
```bash
git clone https://github.com/C0sm1c-Onyx/Payment-System.git
```
Отредактируйте переменный окружения под свои значения
```env
DB_NAME='db'
DB_USER='root'
DB_PASSWORD='root'
DB_HOST='localhost'
DB_PORT='3306'
```
Установите зависимости
```bash
pip install -r requeirements.txt
```
Выполните миграции
```bash
cd django_service
```
```bash
python manage.py migrate
```
## Запуск проекта
```bash
python manage.py runserver
```

## Admin Панель
Cоздайте суперпользователя
```bash
python manage.py createsuperuser
```
Войдите в админ панель
http://127.0.0.1:8000/admin

Можете создать Организацию и задать начальный баланс для этой организации

## API
1.  POST http://127.0.0.1:8000/api/webhook/bank/
Принимает JSON следующего вида:
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}

Создает Payment, если такая операция с таким id еще не производилась
После срабатывает сигнал, если создался Payment и начисляет amount для организации по payer_inn

2. GET http://127.0.0.1:8000/api/organizations/<inn>/balance
Выводит текущий баланс организации по инн
{
   "inn": "1234567890",
   "balance": 1000.00
}

