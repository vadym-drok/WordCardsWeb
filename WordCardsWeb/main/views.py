from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from django.urls import reverse, reverse_lazy
from .forms import WordModelForm

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
    TemplateView
    )


import random

def MainView(request):
    queryset = list(Word.objects.all())
    one_query = random.sample(queryset,1)
    context = {
        'object':one_query
    }
    return render(request, 'main/main_page.html', context)

# class MainView(TemplateView):
#     template_name = "main/main_page.html"



class MyRegisterView(CreateView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    success_url = '/'


class WordDeleteView(DeleteView):
    model = Word
    template_name = "main/delete_word.html"
    success_url = '../../'


class MyLoginView(LoginView):
    template_name = "main/login.html"

class AboutView(TemplateView):
    template_name = "main/about.html"

class ContactsView(TemplateView):
    template_name = "main/contacts.html"


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
    success_url = '/dictionary/'


class WordDetailView(DetailView):
    template_name = 'main/word_detail.html'
    queryset = Word.objects.all()
