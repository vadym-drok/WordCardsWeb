from django.urls import path
from .views import (
    WordListView,
    WordCreateView,
    WordDetailView,
    WordUpdateView,
    )

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', WordCreateView.as_view(), name='main'),
    path('dictionary/', WordListView.as_view(), name='dictionary'),
    path('dictionary/create/', WordCreateView.as_view(), name='word-create'),
    path('dictionary/<int:pk>/', WordDetailView.as_view(), name='word-detail'),
    path('dictionary/<int:pk>/update/', WordUpdateView.as_view(), name='word-update'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
