from django.shortcuts import render

# Create your views here.
def fnIndex(request):
    return render(request,'index.html')
def fnHome(req):
    return render(req,'home.html')
