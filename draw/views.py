from django.shortcuts import render
import random
# Create your views here.
def totolotek(request):
    numbers = random.sample(range(1,49),6)
    context = {
        "numbers": numbers
    }
    return render(request, "draw/totolotek.html",context=context)