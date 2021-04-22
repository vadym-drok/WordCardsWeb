from django.shortcuts import render, redirect, get_object_or_404
from .models import Word
from django.urls import reverse, reverse_lazy
from .forms import WordModelForm

from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, BaseCreateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.list import BaseListView

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


class MyRegisterView(CreateView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    success_url = '/'


def word_delete_view(request, pk):
    model = Word.objects.get(id=pk)
    if request.method == 'POST':
#       print('Prining POST:', request.POST, pk, model, model.image)
        if model.image != '../images/default.jpg':
            model.delete_img()
            return redirect('/dictionary/')
        else:
            model.delete_def()
            return redirect('/dictionary/')

    context = {'object':model}
    return render(request, "main/delete_word.html", context)


class MyLoginView(LoginView):
    template_name = "main/login.html"

class AboutView(TemplateView):
    template_name = "main/about.html"

class ContactsView(TemplateView):
    template_name = "main/contacts.html"


class WordUpdateView(UpdateView):
    model = Word
    form_class = WordModelForm
    template_name = 'main/word_create.html'
    success_url = '/dictionary/'


class WordListView(ListView):
    template_name = 'main/dictionary.html'
    queryset = Word.objects.all()


def list_and_create(request):
    form = WordModelForm(request.POST, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = WordModelForm()
        return HttpResponseRedirect(reverse("dictionary"))

    # notice this comes after saving the form to pick up new objects
    objects = Word.objects.all()
    len_dict = len(list(objects))
    return render(request, 'main/dictionary.html', {
    'object_list': objects,
    'form1': form,
    'len_dict' : len_dict
    })


class WordDetailView(DetailView):
    template_name = 'main/word_detail.html'
    queryset = Word.objects.all()

# class WordCreateView(CreateView):
#     template_name = 'main/word_create.html'
#     form_class = WordModelForm
#     success_url = '/dictionary/'


# class MainView(TemplateView):
#     template_name = "main/main_page.html"


# class WordDeleteView(DeleteView):
#     model = Word
#     template_name = "main/delete_word.html"
#     success_url = '../../'
