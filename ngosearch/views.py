from django.shortcuts import render


def searchpage(request):
    return render(request, "index.html")

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
