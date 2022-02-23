
from unicodedata import name
from django.urls import path

from app.views import AllPasteBinView, CreatePasteBinView, PasteBinView

urlpatterns = [
    path('', CreatePasteBinView.as_view(), name="index"),
    path('all', AllPasteBinView.as_view(), name="all"),
    path('<str:pk>', PasteBinView.as_view(), name="paste"),
]