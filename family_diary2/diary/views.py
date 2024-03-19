from django.shortcuts import render

# Create your views here.
import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import get_object_or_404

from .forms import DiaryCreateForm
from .models import Diary


class DiaryList(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate = 2

    #  ユーザーで絞り込んみ作成日時の逆順に並べ替える
    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-create_at', '-updated_at')
        return diaries


class DiaryDetail(LoginRequiredMixin, DetailView):
    model = Diary
    template_name = 'diary_detail.html'



class DiaryCreate(LoginRequiredMixin, CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日記の作成に失敗しました。')
        return super().form_invalid(form)


class DiaryUpdate(LoginRequiredMixin, UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    #fields = ['title', 'content']
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')


class DiaryDelete(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class DiarySearch(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary_search.html'

    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__icontains=title)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.request.GET.get('title', '')
        return context
