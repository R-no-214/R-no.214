from django.shortcuts import render
# from django.http import HttpResponse

def hello(request):
    return render(request, 'main/hello.html')

# Create your views here.
