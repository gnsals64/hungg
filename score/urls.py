from django.urls import path
from . import views

app_name = 'score'

urlpatterns = [
    path('', views.score_view),
    path('search', views.search_res),
]
