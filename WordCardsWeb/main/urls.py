from django.urls import path
from .views import (
    WordListView,
    WordDetailView,
    WordUpdateView,

    MainView,

    list_and_create,
    word_delete_view,

    AboutView,
    ContactsView,
    MyLoginView,
    MyRegisterView
    )

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('main/', MainView, name='main'),

    path('register/', MyRegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),

    path('ubaut/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('dictionary/', list_and_create, name='dictionary'),

    path('dictionary/<int:pk>/', WordDetailView.as_view(), name='word-detail'),
    path('dictionary/<int:pk>/update/', WordUpdateView.as_view(), name='word-update'),
    path('dictionary/<int:pk>/delete/', word_delete_view, name='word-delete'),

]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
