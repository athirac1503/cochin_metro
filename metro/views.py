from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'userapp/index.html')

def main(request):
    return render(request,'userapp/main.html')

def login(request):
    return render(request,'userapp/login.html')

def signup(request):
    return render(request,'userapp/signup.html')

def station(request):
    return render(request,'userapp/station.html')

def ticket(request):
    return render(request,'userapp/ticket.html')

def contact(request):
    return render(request,'userapp/contact.html')

def contact1(request):
    return render(request,'userapp/contact1.html')

def about(request):
    return render(request,'userapp/about.html')

def price(request):
    return render(request,'userapp/price.html')

def ticket1(request):
    return render(request,'userapp/ticket1.html')

def ticket2(request):
    return render(request,'userapp/ticket2.html')

def index1(request):
    return render(request,'userapp/index1.html')

def payment(request):
    return render(request,'userapp/payment.html')

def otp(request):
    return render(request,'userapp/otp.html')

def otp1(request):
    return render(request,'userapp/otp1.html')
    
def payment1(request):
    return render(request,'userapp/payment1.html')

def qrcode(request):
    return render(request,'userapp/qrcode.html')

def new(request):
    return render(request,'userapp/new.html')

def travel(request):
    return render(request,'userapp/travel.html')

def logout(request):
    return render(request,'userapp/logout.html')

def uprofile(request):
    return render(request,'userapp/uprofile.html')

def upayment(request):
    return render(request,'userapp/upayment.html')

def track(request):
    return render(request,'userapp/track.html')





