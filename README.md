# Fit Flow

REST API для управления фитнес-клубом: клиенты, тренеры, абонементы,
расписание, бронирования, посещения, уведомления, платежи и контакты.

## Запуск

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Swagger доступен по адресу `http://127.0.0.1:8000/swagger/`, ReDoc:
`http://127.0.0.1:8000/redoc/`.

## Проверки

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run --noinput
python manage.py test
```

## Настройки

Переменные окружения перечислены в `.env.example`. Для production обязательно
задайте собственный `DJANGO_SECRET_KEY`, установите `DJANGO_DEBUG=false` и
укажите домены в `DJANGO_ALLOWED_HOSTS`.

## Основные API

- `/api/v1/trainers/`, `/api/v1/client/`, `/api/v1/admin/`
- `/api/v1/subscriptions/` и действия `freeze/`, `unfreeze/`
- `/api/v1/schedule/`, `/api/v1/trainings/`, `/api/v1/scheduled-event/`
- `/api/v1/booking/`, `/api/v1/waiting-list/`
- `/api/v1/check-ins/`, `/api/v1/visit-history/`
- `/api/v1/notifications/`, `/api/v1/payments/`, `/api/v1/contacts/`
