from django.urls import path
from .views import article_view, article_detail, article_create, article_delete, article_update

urlpatterns = [
    path('list/', article_view),
    path('<int:pk>/', article_detail),
    path('create/', article_create),
    path('delete/<int:pk>/', article_delete),
    path('edit/<int:pk>/', article_update),
]

