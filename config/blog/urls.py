from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about_view),
    path('blog/<slug:slug>/', detail),
    path('category/<int:pk>/', category_view),
    path('search/', search_view),

]
