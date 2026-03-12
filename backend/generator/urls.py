from django.urls import path
from .views import GenerateCardView

urlpatterns = [
    path('generate/', GenerateCardView.as_view(), name='generate_card'),
]
