from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):

    # 表示を変更
    list_display = ('note_num', 'name','address')

admin.site.register(User, UserAdmin)

