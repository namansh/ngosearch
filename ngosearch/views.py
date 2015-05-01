from django.shortcuts import render
from ngolist.forms import StateSelectSearchForm


def searchpage(request):
    form = StateSelectSearchForm()
    return render(request, "index.html", {'form': form})

def jobspage(request):
    return render(request, "jobs.html")

def employerspage(request):
    return render(request, "employers.html")

def contactuspage(request):
    return render(request, "contactus.html")

def clientspage(request):
    return render(request, "clients.html")

def aboutuspage(request):
    return render(request, "aboutus.html")
