from django.urls import path, include

from jackets import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
]