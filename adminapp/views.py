from django.shortcuts import render

# Create your views here.


def fair(request):
    return render(request, 'admin_app/fair.html')


def rout(request):
    return render(request, 'admin_app/rout.html')


def complaints(request):
    return render(request, 'admin_app/complaints.html')


def train(request):
    return render(request, 'admin_app/train.html')


def ad_logout(request):
    return render(request, 'admin_app/ad_logout.html')


def ad_station(request):
    return render(request, 'admin_app/ad_station.html')


def aprofile(request):
    return render(request, 'admin_app/aprofile.html')


def reply(request):
    return render(request, 'admin_app/reply.html')


def hello(request):
    return render(request, 'admin_app/hello.html')

def welcome(request):
    return render(request, 'admin_app/welcome.html')
