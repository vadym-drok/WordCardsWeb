from django.urls import path
from .views import (
    WordListView,
    WordCreateView,
    WordDetailView,
    WordUpdateView,
    MainView,
    AboutView,
    ContactsView,
    MyLoginView,
    MyRegisterView,
    WordDeleteView
    )

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main/', MainView, name='main'),
    # path('main/', MainView.as_view(), name='main'),

    path('register/', MyRegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),


    path('ubaut/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('dictionary/', WordListView.as_view(), name='dictionary'),
    path('dictionary/create/', WordCreateView.as_view(), name='word-create'),
    path('dictionary/<int:pk>/', WordDetailView.as_view(), name='word-detail'),
    path('dictionary/<int:pk>/update/', WordUpdateView.as_view(), name='word-update'),
    path('dictionary/<int:pk>/delete/', WordDeleteView.as_view(), name='word-delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
