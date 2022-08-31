from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:wikiEntry>", views.goToEntry, name="wikiEntry"),
    path("search/", views.search, name="search"),
    path("createpage/", views.createpage, name="createpage")
]
