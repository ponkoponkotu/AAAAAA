from django.urls import path
from . import views
from .views import PregnantMomsListView, PregnantMomsDetailView, PregnantMomsCreateView, \
    PregnantMomsUpdateView, PregnantMomsDeleteView

app_name = 'health'

urlpatterns = [
    path('preg_moms_list/', PregnantMomsListView.as_view(), name='preg_moms_list'),
    path('preg_moms_detail/<int:pk>/', PregnantMomsDetailView.as_view(), name='preg_moms_detail'),
    path('preg_moms_create/', PregnantMomsCreateView.as_view(), name='preg_moms_create'),
    path('preg_moms_update/<int:pk>', PregnantMomsUpdateView.as_view(), name='preg_moms_update'),
    path('preg_moms_delete/<int:pk>', PregnantMomsDeleteView.as_view(), name='preg_moms_delete'),
    ]
