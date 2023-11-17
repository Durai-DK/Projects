from django.urls import path,include

from .views import *
urlpatterns = [
    path('',MediumList.as_view(),name = "list")
]
