from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(verbose_name='メールアドレス', unique=True)
    note_num = models.IntegerField(verbose_name='交付番号', unique=True, )
    name = models.CharField(verbose_name='氏名',max_length= 100, blank=True)
    address = models.CharField(verbose_name='住所', max_length=100, blank=True)


    def save(self, *args, **kwargs):
        # name フィールドに名前をセットする
        self.name = f'{self.last_name} {self.first_name}'
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = '利用者情報'


