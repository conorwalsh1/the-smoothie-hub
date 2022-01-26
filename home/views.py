from django.shortcuts import render

# This function renders the about.html page


def home(request):

    return render(request, "home.html")
