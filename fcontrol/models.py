from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=16, help_text='телефон',unique=True,verbose_name='телефон')



# class Employees(models.Model):
#     first_name = models.CharField(max_length=70, help_text='Имя сотрудника',unique=True,verbose_name='Имя сотрудника')
#     last_name  = models.CharField(max_length=70, help_text='Фамилия сотрудника',unique=True,verbose_name='Фамилия сотрудника')
#     phone_number = models.CharField(max_length=16, help_text='телефон',unique=True,verbose_name='телефон')
#     # email = models.EmailField()
#     # account = models.OneToOneField
#     class Meta:
#         ordering =['id']
#         verbose_name = 'Сотрудник'
#         verbose_name_plural = 'Сотрудники'
# 
#     def __str__(self):
#         return self.first_name

class Institution(models.Model):
    name = models.CharField(max_length=70, help_text='Название учреждения',verbose_name='Название учреждения')
    address = models.CharField(max_length=70, help_text='Адрес учреждения',unique=True,verbose_name='Адрес учреждения')
    class Meta:
        ordering =['id']
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждения'

    def __str__(self):
        return self.address

class Controller(models.Model):
    name = models.CharField(max_length=70, help_text='Название оборудования',default='', verbose_name='Название датчика')
    institution = models.ForeignKey(Institution, verbose_name='Учреждение', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['id']
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name

class ControllerData(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='data')
    temperature = models.DecimalField(verbose_name='температура',max_digits=5, decimal_places=2 )
    humidity = models.PositiveSmallIntegerField(verbose_name='Влажность', )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['id']
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'




    def __str__(self):
        return self.controller.name




class Fridge(models.Model):
    name = models.CharField(max_length=70, help_text='Название оборудования',verbose_name='Название оборудования')
    institution = models.ForeignKey(Institution, verbose_name='Учреждение',on_delete=models.SET_NULL,null=True)
    controller = models.ForeignKey(Controller, verbose_name='датчик',on_delete=models.SET_NULL,null=True)
    class Meta:
        ordering =['id']
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'
        constraints = [
            models.UniqueConstraint(
                fields=['name','institution'],
                name= 'Unique name within institution'
            )
        ]



    def __str__(self):
        return self.name


