from django.db import models
from registration.models import User
from django.utils import timezone
# Create your models here.
class Diary(models.Model):


    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT,)
    title = models.CharField(verbose_name='タイトル', max_length=100, blank=True, null=True)  # タイトル
    content = models.TextField(verbose_name='本文', max_length=1000, blank=True, null=True)  # 内容
    create_at = models.DateField(verbose_name='作成日時', auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)  #更新日時

    class Meta:
        verbose_name_plural = '日記'


    def __str__(self):
        return self.title

