from django.urls import path
import ToDoListApp.views
urlpatterns = [
    path('', ToDoListApp.views.home, name='home'),
    path('about/', ToDoListApp.views.about, name='about')
]