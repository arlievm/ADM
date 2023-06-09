from django.db import models


user_status = [
  [
    "Партнер",
    "Партнер"
  ],
  [
    "Участник",
    "Участник"
  ]
]


class Application(models.Model):
    
    class Meta:
        db_table = 'application'
        verbose_name = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        verbose_name_plural = 'ПРЕДВАРИТЕЛЬНАЯ ЗАЯВКА'
        
    name_organic = models.CharField(verbose_name="Название организации", max_length=128)
    surname = models.CharField(verbose_name="Фамилия", max_length=16)
    name = models.CharField(verbose_name="Имя", max_length=16)
    email = models.EmailField(verbose_name="E-mail", max_length=32)
    number = models.CharField(verbose_name="Телефон", max_length=16)
    user_status = models.CharField(verbose_name="Выберите направление", max_length=100, default=None, choices=user_status, blank=True, null=True)
    data = models.BooleanField(verbose_name="Я согласен на обработку моих персональных данных", default=False)
    
    def __str__(self):
        return self.name