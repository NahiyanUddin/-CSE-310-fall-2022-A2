from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request, mk):
    dict = {
        "name": "Dhrubo",
        "ID" : 18101010,
        "courses": ["CSE 309","CSE 310","CSE 303","CSE 304"],
        "marks": int(mk)
    }
    return render(request, "home/home.html", context = dict)
