from django.urls import path
from app.views import youtube

urlpatterns = [
    path('', youtube, name='youtube'),
]
