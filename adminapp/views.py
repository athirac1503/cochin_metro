from django.shortcuts import redirect, render
from adminapp.models import AddFair, AddStationDetails, AdminLogin
from django.core.mail import send_mail
from django.conf import settings

from metro.models import Contact

# Create your views here.


def fair(request):
    return render(request, 'admin_app/fair.html')

def add_fair(request):
    if request.method=='POST':
        f_zone=request.POST['zone']
        f_distance=request.POST['distance']
        f_fair=request.POST['fair']
        add=AddFair(zone=f_zone,distance=f_distance,fair=f_fair)
        add.save()
    return render(request, 'admin_app/add_fair.html')


# def rout(request):
#     return render(request, 'admin_app/rout.html')

def admin_login(request):
    error=""
    if request.method=='POST':
        admin_name=request.POST['name']
        admin_pass=request.POST['pass']
        try:
            admin_data=AdminLogin.objects.get(user_name=admin_name,password=admin_pass)
            request.session['admin_id']=admin_data.id
            return redirect('welcome')
        except:
            error="Invalied username or password"
    return render(request, 'admin_app/admin_login.html',{'error':error})

def complaints(request):
    contact=Contact.objects.all()
    return render(request, 'admin_app/complaints.html',{"contact":contact})


def train(request):
    return render(request, 'admin_app/train.html')


def ad_logout(request):
    return render(request, 'admin_app/ad_logout.html')

def update_fair(request):
    fair=AddFair.objects.all()

    if request.method=="POST":
        f_zone=request.POST["zone"]
        f_distance=request.POST["distance"]
        f_fair=request.POST["fair"]

        fair.f_zone=f_zone
        fair.f_distance=f_distance
        fair.f_fair=f_fair
        fair.save()

    return render(request, 'admin_app/update_fair.html',{"fair":fair})

def add_station_details (request):
    if request.method=='POST':
        s_img=request.FILES['img']
        s_name=request.POST['name']
        s_address=request.POST['address']
        s_platform=request.POST['platform']
        s_distance=request.POST['dist']
        s_num1=request.POST['num1']
        s_num2=request.POST['num2']
        station=AddStationDetails(add_image=s_img, station_name=s_name,station_address=s_address,platform_type=s_platform,distance=s_distance,number_1=s_num1,number_2= s_num2)
        station.save()
    return render(request, 'admin_app/add_station_details.html')

def aprofile(request):
    return render(request, 'admin_app/aprofile.html')


def reply(request,id):
    contact=Contact.objects.get(id=id)
    if request.method=='POST':
        contact.reply=request.POST['rply']
        contact.save()
        return redirect('complaints')
    return render(request, 'admin_app/reply.html',{"contact":contact})


def hello(request):
    return render(request, 'admin_app/hello.html')

def welcome(request):
    welcome=""
    if 'admin_id' in request.session:
        current_user=request.session['admin_id']
        welcome=AdminLogin.objects.get(id=current_user)
    return render(request, 'admin_app/welcome.html',{'wel':welcome})
