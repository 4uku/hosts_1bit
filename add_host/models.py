from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Host(models.Model):
    CHOICES = (
        ('Win', 'Windows'),
        ('Unix', 'UNIX'),
        ('SQL', 'SQL')
    )
    ip_adress = models.GenericIPAddressField('Ip адрес')
    port = models.IntegerField('Порт', validators=[
        MinValueValidator(0), MaxValueValidator(65536)])
    resource = models.CharField('Ресурс', choices=CHOICES, max_length=50)
    owners = models.ManyToManyField(User, verbose_name='Владелец',
                                    related_name='hosts')
    date_edit = models.DateTimeField('Дата редактирования', auto_now=True)

    class Meta:
        ordering = ['ip_adress']
        verbose_name = 'Хост'
        verbose_name_plural = 'Хосты'
        constraints = (
            models.UniqueConstraint(
                fields=['ip_adress', 'port'], name='uniq host/port'),
        )

    def __str__(self) -> str:
        return f'{self.ip_adress}:{self.port}'
