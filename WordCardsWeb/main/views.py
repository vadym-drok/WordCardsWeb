from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from django.urls import reverse
from .forms import WordModelForm

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView
    )


class WordCreateView(CreateView):
    template_name = 'main/word_create.html'
    form_class = WordModelForm
    queryset = Word.objects.all()

class WordListView(ListView):
    template_name = 'main/dictionary.html'
    queryset = Word.objects.all()

class WordDetailView(DetailView):
    template_name = 'main/word_detail.html'
    # queryset = Word.objects.all()
