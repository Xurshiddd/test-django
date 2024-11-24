from django.urls import path
from .views import HomePageView, AboutPgeView, ContactPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPgeView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact')
]