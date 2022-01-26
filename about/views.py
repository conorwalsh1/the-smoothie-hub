from django.shortcuts import render

# This function renders the about.html page


def about(request):

    return render(request, "about.html")
