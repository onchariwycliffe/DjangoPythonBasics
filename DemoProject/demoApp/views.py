from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    #return HttpResponse('<h1>This is my homepage </h1>')
    return render(request, 'demoApp/Hi.html')
# Create your views here.
