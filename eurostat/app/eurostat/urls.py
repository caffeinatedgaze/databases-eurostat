from django.urls import path

from .views import main_view, query_view

urlpatterns = [
    path("", main_view),
    path("query/<int:num>", query_view),
]
