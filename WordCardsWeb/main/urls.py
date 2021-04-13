from django.urls import path
from .views import WordListView, WordCreateView, WordDetailView

urlpatterns = [
    # path('', WordCreateView.as_view(), name='main'),
    path('dictionary/', WordListView.as_view(), name='dictionary'),
    path('create/', WordCreateView.as_view(), name='word-create'),
    path('<int:id>/', WordDetailView.as_view(), name='word-detail'),
]
