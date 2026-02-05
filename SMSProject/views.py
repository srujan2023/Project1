from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    return render(request,'index.html')