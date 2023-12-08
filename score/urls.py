from django.urls import path
from . import views

app_name = 'score'

urlpatterns = [
    path('', views.score_view, name='main'),
    path('search', views.search_res, name='result'),
]
