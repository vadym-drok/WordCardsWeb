from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from django.urls import reverse, reverse_lazy
from .forms import WordModelForm

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
    )


class WordListView(ListView):
    template_name = 'main/dictionary.html'
    queryset = Word.objects.all()


class WordUpdateView(UpdateView):
    model = Word
    form_class = WordModelForm
    template_name = 'main/word_create.html'
    success_url = '/dictionary/'


class WordCreateView(CreateView):
    template_name = 'main/word_create.html'
    form_class = WordModelForm
    queryset = Word.objects.all()
    success_url = '/dictionary/'


class WordCreateView(DeleteView):
    model = Word
    success_url = reverse_lazy('dictionary')


class WordDetailView(DetailView):
    template_name = 'main/word_detail.html'
    queryset = Word.objects.all()
