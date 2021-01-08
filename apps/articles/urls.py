from django.urls import path
from articles import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<int:pk>',views.detail,name="detail"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('search/',views.search,name="search"),
    path('category/<int:id>',views.category,name="category"),
    path('tag/<int:id>',views.tag,name="tag")
]