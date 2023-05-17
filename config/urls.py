from django.urls import path
from .views import RegistrationView


urlpatterns = [
    path('post/', RegistrationView.as_view()),
    # path('activate/', ActivationView.as_view()),
]