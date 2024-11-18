from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField('Телефон', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


SERVICES = [
    ('Общий клининг', 'Общий клининг'),
    ('Генеральная уборка', 'Генеральная уборка'),
    ('Послестроительная уборка', 'Послестроительная уборка'),
    ('Химчистка ковров и мебели', 'Химчистка ковров и мебели'),
]

PAYMENT_TYPE = [
    ('Наличные', 'Наличные'),
    ('Банковская карта', 'Банковская карта')
]

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
