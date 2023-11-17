from django.urls import path
from .views import *

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view())
]
