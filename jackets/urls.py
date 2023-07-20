from django.urls import path, include

from jackets import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('all-products/', views.ProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetailView.as_view()),
]