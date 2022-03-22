from django.shortcuts import render

# Create your views here.
def buisness_card(request):
    return render(request, "intro/card.html")