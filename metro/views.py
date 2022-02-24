from django.shortcuts import render

# Create your views here.
def fnLogin(request):
    return render(request,'login.html')
def fnHome(request1):
    return render(request1,'home.html')
def fnSignup(request2):
    return render(request2,'signup.html')
def fnStation(request3):
    return render(request3,'station.html')
def fnIndex(request4):
    return render(request4,'index.html')
def fnTicket(request5):
    return render(request5,'ticket.html')
def fnContact(request6):
    return render(request6,'contact.html')
def fnContact1(request7):
    return render(request7,'contact1.html')
def fnAbout(request8):
    return render(request8,'about.html')
def fnPrice(request9):
    return render(request9,'price.html')



