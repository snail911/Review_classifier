from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_submission, name='submit_review'),
]