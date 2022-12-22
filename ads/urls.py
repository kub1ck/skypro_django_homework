from django.urls import path

from ads import views


urlpatterns = [
    path('', views.index),

    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/<int:pk>/add_image/', views.AdImageView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),

    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),

    path('selections/', views.SelectionView.as_view()),
    path('selections/<int:pk>/', views.SelectionDetailView.as_view()),
    path('selections/create/', views.SelectionCreateView.as_view()),
    path('selections/<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('selections/<int:pk>/del/', views.SelectionDeleteView.as_view()),
]


