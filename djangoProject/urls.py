from django.contrib import admin
from django.urls import path
from ads import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page),
    path("ads/", views.AdsView.as_view()),
    path('category/', views.CategoriesView.as_view()),
    path('category/<int:category_id>/', views.CategoriesView.get_by_pk),
    path('ads/<int:ads_id>/', views.AdsView.get_by_pk),
]
