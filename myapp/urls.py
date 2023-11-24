from django.urls import path
from .views import ItemAPI, Create_ItemAPI

urlpatterns = [
    path("<str:item_id>/", ItemAPI.as_view()),
    path("", Create_ItemAPI.as_view()),
]