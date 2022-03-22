from django.shortcuts import render

# Create your views here.
def mem(request):
    return render(request, 'mem/sample.html')