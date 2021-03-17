from django.urls import path
from .views import SportsListView , SportsCreateView, SportsUpdateView, SportsDeleteView
from . import views

urlpatterns = [
    path('', SportsListView.as_view(), name='home'),
    path('sport/new/', SportsCreateView.as_view(), name='sport-create'),
    path('sport/<int:pk>/update/', SportsUpdateView.as_view(), name='sport-update'),
    path('sport/<int:pk>/delete/', SportsDeleteView.as_view(), name='sport-delete'),
]