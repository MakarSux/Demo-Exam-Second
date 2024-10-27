from django.db import models
from django.contrib.auth.models import AbstractUser


SERVICES = [
    ('cleaning', 'Общий клининг'),
    ('deep_cleaning', 'Генеральная уборка'),
    ('post_construction', 'Послестроительная уборка'),
    ('dry_cleaning', 'Химчистка ковров и мебели'),
]

PAYMENT_TYPE = [
    ('cash', 'Наличные'),
    ('card', 'Банковская карта')
]


class CustomUser(AbstractUser):
    username = models.CharField('Логин', max_length=255, unique=True)
    email = models.EmailField('E-mail', unique=True)
    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=11)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'phone']

class Order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    adress = models.CharField('Адрес', max_length=255)
    desired_date = models.DateField()
    desired_time = models.TimeField()
    service_kind = models.CharField('Вид услуги', choices=SERVICES, max_length=255)
    other_service = models.TextField( blank=True, null=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE)
    
    def __str__(self):
        return f'{self.adress} - {self.service_kind}'
