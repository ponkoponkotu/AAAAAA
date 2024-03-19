from django.shortcuts import render

# Create your views here.
import logging
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import  messages
from django.urls import reverse_lazy
from django.views import generic
from .models import PregnantMomsHealth
from .forms import PregnantMomsCreateForm

class PregnantMomsListView(LoginRequiredMixin, generic.ListView):
    model = PregnantMomsHealth
    template_name = 'preg_moms_list.html'

    #  ユーザーで絞り込む
    def get_queryset(self):
        pregnantmomshealth = PregnantMomsHealth.objects.filter(user=self.request.user).order_by('-my_date')


        return pregnantmomshealth



class PregnantMomsDetailView(LoginRequiredMixin, DetailView):
    model = PregnantMomsHealth
    template_name = 'preg_moms_detail.html'



class PregnantMomsCreateView(LoginRequiredMixin, CreateView):
    model = PregnantMomsHealth
    template_name = 'preg_moms_create.html'
    form_class = PregnantMomsCreateForm
    success_url = reverse_lazy('health:preg_moms_list')

    def form_valid(self, form):
        pregnant = form.save(commit = False)
        pregnant.user = self.request.user
        pregnant.save()
        messages.success(self.request, '検診結果を記録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '記録の作成に失敗しました。')
        return super().form_invalid(form)


class PregnantMomsUpdateView(LoginRequiredMixin, UpdateView):
    model = PregnantMomsHealth
    fields = ['pregnancy_week',
                  'my_date',
                  'height',
                  'weight',
                  'blood_pressure_upper',
                  'blood_pressure_under',
                  'waist',
                  'fundall_length',
                  'edema',
                  'unrine_protein',
                  'diabetes',
                  'other_test',
              ]

    template_name = 'preg_moms_update.html'
    success_url = reverse_lazy('health:preg_moms_list')

class PregnantMomsDeleteView(LoginRequiredMixin, DeleteView):
    model = PregnantMomsHealth
    template_name = 'preg_moms_delete.html'
