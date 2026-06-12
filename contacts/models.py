from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


phone_validator = RegexValidator(
    regex=r"^[0-9+\-() ]{7,20}$",
    message="Телефон может содержать только цифры, пробелы, '+', '-' и скобки.",
)


class ContactList(models.Model):
    client_list = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, validators=[phone_validator])
    registration_date = models.DateField()

    def clean(self):
        self.client_list = self.client_list.strip()
        self.phone = self.phone.strip()
        if not self.client_list:
            raise ValidationError({"client_list": "Список клиентов не может быть пустым."})
        if not self.phone:
            raise ValidationError({"phone": "Телефон не может быть пустым."})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
