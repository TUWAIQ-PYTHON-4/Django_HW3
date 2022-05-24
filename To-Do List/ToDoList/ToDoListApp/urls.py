from django.urls import path
from django.contrib import admin
import ToDoListApp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ToDoListApp.views.base),
    path('home/' , ToDoListApp.views.home ),
    path('about/', ToDoListApp.views.about)

]