from django.urls import path
from playground.views import PlayView

urlpatterns = [
    path('play/', PlayView.as_view(), name='play_for_kid'),
]