from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "primeiro_app/pages/home.html")


def about(request):
    return render(request, "primeiro_app/pages/about.html")
