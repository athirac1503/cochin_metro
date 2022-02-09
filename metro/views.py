from django.shortcuts import render

# Create your views here.
def fnLogin(request):
    return render(request,'login.html')
def fnHome(req):
    return render(req,'home.html')
def fnSignup(requ):
    return render(requ,'signup.html')

