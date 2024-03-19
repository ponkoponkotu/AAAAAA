from django.db import models

# Create your models here.
from registration.models import User
from django.utils import timezone
from django.conf import settings


#母親の基本情報
class MomsInfo(models.Model):
    #  血液型の選択項目
    choice_results_blood = (
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    )

    #  血液型,Rh値の選択項目
    choice_results_rh = (
        ('＋', '＋'),
        ('－', '－'),
    )

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT, default=2)
    height = models.FloatField(verbose_name='身長', default=150)  # 身長
    blood_tipe = models.CharField(verbose_name='血液型', max_length=10, choices=choice_results_blood, blank=True)
    rh_tipe = models.CharField(verbose_name='Rh型', max_length=10, choices=choice_results_rh, blank=True)
    check_1 = models.DateField(verbose_name='不規則抗体', blank=True)
    check_2 = models.DateField(verbose_name='子宮頸がん検診', blank=True)
    check_3 = models.DateField(verbose_name='梅毒血清検診', blank=True)
    check_4 = models.DateField(verbose_name='HBs抗原', blank=True)
    check_5 = models.DateField(verbose_name='HCV抗体', blank=True)
    check_6 = models.DateField(verbose_name='HIV抗体', blank=True)
    check_7 = models.DateField(verbose_name='風しんウィルス抗体', blank=True)
    check_8 = models.DateField(verbose_name='HTLV-1抗体', blank=True)
    check_9 = models.DateField(verbose_name='クラミジア抗原', blank=True)
    check_10 = models.DateField(verbose_name='B群溶血性連鎖球菌', blank=True)


    class Meta:
        verbose_name_plural = '母親基本情報'

    def __str__(self):
        return self



#  妊娠中の検査項目
class PregnantMomsHealth(models.Model):


    #  浮腫,血糖,尿蛋白の選択項目
    choice_results = (
                ('－', '－'),
                ('＋', '＋'),
                ('＋＋', '＋＋'),
    )

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT,default=2)
    pregnancy_week = models.IntegerField(verbose_name='妊娠週', default=20)
    my_date = models.DateField(verbose_name='', blank=False, default=timezone.now)
    height = models.FloatField(verbose_name='身長', default=150)  # 身長
    weight = models.FloatField(verbose_name='体重', default=55)  # 体重
    blood_pressure_upper = models.IntegerField(verbose_name='血圧(上)', default='100')  # 血圧上
    blood_pressure_under = models.IntegerField(verbose_name='血圧(下)', default='50')  # 血圧下
    waist = models.FloatField(verbose_name='腹囲', default=85,)  # 腹囲
    fundall_length = models.FloatField(verbose_name='子宮底長', default=20,)  # 子宮底長
    edema = models.CharField(verbose_name='浮腫', max_length=10, choices=choice_results, blank=True)  # 浮腫
    unrine_protein = models.CharField(verbose_name='尿蛋白', max_length=10, choices=choice_results, blank=True)  # 尿蛋白
    diabetes = models.CharField(verbose_name='血糖', max_length=10, choices=choice_results, blank=True)  # 血糖
    other_test = models.TextField(verbose_name='他検査,特記事項など', max_length=1000, blank=True)  # 他検査

    class Meta:
        verbose_name_plural = '妊娠中'

    def __str__(self):
        return self

#  ---------------------ここから下は今後追加の機能分のテーブル-------------------------

#  産後の検査項目
"""
class PostpartumMomsHealth(models.Model):

    #  浮腫,血糖,尿蛋白の選択項目
    choice_results = (
        ('－', '－'),
        ('＋', '＋'),
        ('＋＋', '＋＋'),
    )

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT,)
    my_date = models.DateField(verbose_name='', blank=False, default=timezone.now, )
    blood_pressure_upper = models.IntegerField(verbose_name='血圧(上)', default='100', blank=True)  # 血圧上
    blood_pressure_under = models.IntegerField(verbose_name='血圧(下)', default='50', blank=True)  # 血圧下
    uterus_repair = models.CharField(verbose_name='子宮復古', max_length=10, choices=(('good','良'), ('bad','否')), blank=True)  #子宮復古(選択)
    lochia = models.CharField(verbose_name='悪露', max_length=10, choices=(('good','正'), ('bad','否')), blank=True)  #悪露(選択)
    unrine_protein = models.CharField(verbose_name='尿蛋白', max_length=10, choices=choice_results, blank=True)  # 尿蛋白
    diabetes = models.CharField(verbose_name='血糖', max_length=10, choices=choice_results, blank=True)  # 血糖

    class Meta:
        verbose_name_plural = '産後'


    def __str__(self):
        return '検査日' + str(self.my_date)
"""
#  子の基本情報
"""class BabysInfo(models.Model):
    
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT, default=2)
    birthday = models.DateField(verbose_name='誕生日')
    vaccine_1 = models.CharField(verbose_name='')
    vaccine_2 = models.CharField(verbose_name='')
    vaccine_3 = models.CharField(verbose_name='')
    
    
        class Meta:
        verbose_name_plural = '子の基本情報'

    def __str__(self):
        return self
    """

#  新生児期の検査項目
"""
class NewbornBabysHealth(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT,)
    my_date = models.DateField(verbose_name='検査日', blank=False, default=timezone.now)  # 検査日
    after_birth_day = models.IntegerField(verbose_name='日齢', default=1)  # 日齢
    height = models.FloatField(verbose_name='身長', default=50)  # 身長
    weight = models.FloatField(verbose_name='体重', default=5)  # 体重
    head_circumference = models.FloatField(verbose_name='頭囲', default=40)  # 頭囲
    chest_measurement = models.FloatField(verbose_name='胸囲', default=40)  # 胸囲
    others = models.TextField(verbose_name='他検査,特記事項など', max_length=1000, blank=True)  # 他記入事項

    class Meta:
        verbose_name_plural = '新生児期'

    def __str__(self):
        return '日齢' + str(self.after_birth_day)
"""

#  乳幼児期の検査項目
"""
class InfantBabysHealth(models.Model):

    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT,)
    my_date = models.DateField(verbose_name='検査日', blank=False, default=timezone.now)  # 検査日
    after_birth_month = models.IntegerField(verbose_name='月齢', default=1)  # 月齢
    height = models.FloatField(verbose_name='身長',default=50)  # 身長
    weight = models.FloatField(verbose_name='体重',default=5)  # 体重
    head_circumference = models.FloatField(verbose_name='頭囲', default='40')  # 頭囲
    others = models.TextField(verbose_name='他検査,特記事項など', max_length=1000, blank=True)  # 他記入事項

    class Meta:
        verbose_name_plural = '乳幼児期'

    def __str__(self):
        return '月齢' + str(self.after_birth_month)
"""
