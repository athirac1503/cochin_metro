import imp
from turtle import distance
from django.shortcuts import redirect, render
from adminapp.models import AddFair, AddStationDetails
from datetime import date
from datetime import datetime
import qrcode

from metro.models import BookTicket, Contact, UserRegistration


# Create your views here.

def index(request):
    prof_details=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        prof_details=UserRegistration.objects.get(id=current_user)
    return render(request,'userapp/index.html',{'prof':prof_details})

def user_welcome(request):
    welcome=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        welcome=UserRegistration.objects.get(id=current_user)
    return render(request,'userapp/user_welcome.html',{'wel':welcome})

def main(request):
    return render(request,'userap  p/main.html')

def login(request):
    error=''
    if request.method=='POST':
        user_email=request.POST['u_email']
        user_pass=request.POST['u_pass']
        user_data=UserRegistration.objects.filter(email=user_email,password=user_pass).exists()
        if user_data:
            Metro_user=UserRegistration.objects.get(email=user_email,password=user_pass)
            request.session['MetroUser_id']=Metro_user.id
            return redirect('index')
        else:
            error="Invalied username or password"
    return render(request,'userapp/login.html',{"error":error})

def signup(request):
    if request.method=="POST":
        user_fname=request.POST["f_name"]
        user_lname=request.POST["l_name"]
        user_email=request.POST["e_mail"]
        user_pass=request.POST["pass"]
        sign=UserRegistration(fname=user_fname,lname=user_lname,email=user_email,password=user_pass)
        sign.save()
        
    return render(request,'userapp/signup.html')

def station(request):
    station=AddStationDetails.objects.all()
    return render(request,'userapp/station.html',{"station":station})

def ticket(request):
    if request.method=='POST':
        current_user=request.session['MetroUser_id']
        user=UserRegistration.objects.get(id=current_user)
        t_type=request.POST['type']
        t_from=request.POST['from']
        t_to=request.POST['to']
        t_pass=request.POST['passenger']
        c_date=today = date.today()
        now = datetime.now()
        c_time=now.strftime("%H:%M:%S")
        ticket_id = AddStationDetails.objects.get(id = id)
        ticket_book=BookTicket(ticket_type=t_type,ticket_from=t_from,ticket_to=t_to,no_passenger=t_pass,user_id=user,time=c_time,date=c_date,ticket_id=ticket_id)
        ticket_book.save()
        request.session['ticket_id']=ticket_book.id
        return redirect('ticket1'   )

    return render(request,'userapp/ticket.html')

def contact(request):
    if request.method=='POST':
        
        current_user=request.session['MetroUser_id']
        contact_us=UserRegistration.objects.get(id=current_user)

        c_fullname=request.POST['fname']
        c_email=request.POST['e_mail']
        c_message=request.POST['msg']
        contact_msg=Contact(fullname=c_fullname,email=c_email,message=c_message,contact_id=contact_us)
        contact_msg.save()
    return render(request,'userapp/contact.html')

def about(request):
    return render(request,'userapp/about.html')
def train_details(request):
    return render(request,'userapp/train_details.html')

def price(request):
    fair=AddFair.objects.all()
    return render(request,'userapp/price.html',{'fair':fair})

def ticket1(request):
    
    if 'ticket_id' in request.session:
        current_user=request.session['ticket_id']
        ticket_details=BookTicket.objects.get(id=current_user)
    return render(request,'userapp/ticket1.html',{'ticket':ticket_details})

def ticket2(request):
    if 'ticket_id' in request.session:
        current_user=request.session['ticket_id']
        ticket_details=BookTicket.objects.get(id=current_user)
    return render(request,'userapp/ticket2.html',{'ticket':ticket_details})

def index1(request):
    return render(request,'userapp/index1.html')

def qrcode1(request):
    img=qrcode.make('Hello World')
    img.save('hello.png')
    return render(request,'userapp/qrcode.html')

def new(request):
    return render(request,'userapp/new.html')

def change_password(request):
    message=""
    if request.method=='POST':
        old=request.POST['old_pass']
        new=request.POST['new_pass']
        confirm=request.POST['confirm_pass']
        data=UserRegistration.objects.get(id=request.session['MetroUser_id'])
        if data.password==old:
            if new==confirm:
                data.password==new
                data.save()
                message="Password change successfully"
            else:
                message="Password does not match"
        else:
            message="Password incorrect"
    return render(request,'userapp/change_password.html',{"msg":message})

def travel(request):
    travel=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        travel=BookTicket.objects.filter(user_id=current_user)
    return render(request,'userapp/travel.html',{'travel':travel})

def logout(request):
    del request.session['MetroUser_id']
    request.session.flush()
    return render(request,'userapp/logout.html')

def uprofile(request):
    prof_details=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        prof_details=UserRegistration.objects.get(id=current_user)
    return render(request,'userapp/uprofile.html',{'prof':prof_details})

def upayment(request):
    payment=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        payment=BookTicket.objects.filter(user_id=current_user)
    return render(request,'userapp/upayment.html',{'payment':payment})

def track(request):
    return render(request,'userapp/track.html')

def message_view(request):
    msg_details=""
    if 'MetroUser_id' in request.session:
        current_user=request.session['MetroUser_id']
        msg_details=Contact.objects.filter(contact_id_id=current_user)
        # print(msg_details.message)
    return render(request,'userapp/message_view.html',{"msg":msg_details})









