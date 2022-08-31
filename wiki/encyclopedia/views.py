import markdown2
from django.shortcuts import render
from . import util
from django.http import Http404
from django import forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def goToEntry(request, wikiEntry):
    if wikiEntry in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "wikiEntry": markdown2.markdown(util.get_entry(wikiEntry)),
            "wikiEntryTitle": wikiEntry
        })
    else:
        raise Http404("The Wiki Entry does not exist")

def search(request):
    SearchTitle = request.GET['q']
    if util.get_entry(SearchTitle) is not None:
        return goToEntry(request, SearchTitle)
    else:
        return render(request, "encyclopedia/searchResults.html", {
            "entries": util.list_entries(),
            "searchString": SearchTitle
        })

def createpage(request):
    return render(request, "encyclopedia/createpage.html")