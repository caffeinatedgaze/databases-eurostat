from django.urls import path

from .views import main_view, query_view, search

urlpatterns = [
    path("", main_view),
    path("query/<int:num>", query_view),
    path("search/", search),
]
