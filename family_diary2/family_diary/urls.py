"""
URL configuration for family_diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import settings

from registration import views
"""
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user.name', 'email', 'create_at')"""

from django.contrib.auth.models import Group

#  管理サイトの表示の設定を変更
admin.site.site_title = 'デジタル母子手帳 内部管理サイト'
admin.site.site_header = 'デジタル母子手帳 内部管理サイト'
admin.site.index_title = 'メニュー'
#  グループを非表示にする
#admin.site.unregister(Group)
#  削除を非表示にする
#admin.site.disable_action('delete_selected')


index_view = TemplateView.as_view(template_name="registration/registration_index.html")

urlpatterns = [
    path('staff-admin/', admin.site.urls),
    path('', login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path('', include('diary.urls'), name="diary"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name="activate"),
    path('', include('health.urls')),
]
