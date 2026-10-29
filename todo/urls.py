from django.urls import include, path 

from .import views  # pyright: ignore[reportMissingModuleSource]

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),  # Include the URLs from the todo app
]