from django.shortcuts import render

# This function renders the about.html page


def contact(request):

    return render(request, "contact.html")
