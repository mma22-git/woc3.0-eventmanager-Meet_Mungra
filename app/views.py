from django.shortcuts import render, HttpResponse
from app.models import Event,Participant
from django.core.mail import send_mail
import datetime

# Create your views here.
def part(request):
    c=[]
    c1=[]
    coming_events=Event.objects.filter(Reg_deadline__gte=datetime.datetime.now())
    if request.method=="POST":
        pname=request.POST['name1']
        pcontact=request.POST['contact']
        pemail=request.POST['email1']
        for obj in coming_events:
            
           if request.POST.get(obj.name,False):
               c.append(obj.name)
            # pevents=request.POST.get(obj.name,False)
        ptype1=request.POST.get('type',False)
        if(ptype1=="Individual"):
            people=0
            ptype='I'
        if(ptype1=="Group"):
            ptype='G'
            people=request.POST['people']
        # print(pname,c,ptype)
        data1=Participant(Name=pname,Contact=pcontact,Email=pemail,Checked=c,Reg_type=ptype,No_of=people)
        data1.save()
        return render(request,"home.html")
    context={ 'content': coming_events }
    return render(request,"part.html",context)

def home1(request):
    return render(request,"home.html")

def home2(request):
    if request.method=='POST':
        nam1= request.POST['name']
        loc1= request.POST['location']
        lin1= request.POST['link']
        fro1= request.POST['from']
        to1= request.POST['to']
        dea1= request.POST['dead']
        ema1= request.POST['email']
        pas1= request.POST['password']
        des1=request.POST['desc']
        fti1= request.POST['ftime']
        tti1= request.POST['ttime']
        dti1= request.POST['dtime']
        data= Event(name=nam1,location=loc1,link=lin1,from_date=fro1,to_date=to1,Reg_deadline=dea1,email=ema1,password=pas1,from_time=fti1,to_time=tti1,deadline_time=dti1,description=des1)
        data.save()
        
        subject="Event registered successfully..."
        message="Thank you for using our service..\n"\
                +"Event name : "+ nam1\
                +"\nEvent ID : "+ str(data.id)\
                +"\nUse this ID to access Event Dashboard"
        send_mail(subject,message,
        'jangotry123@gmail.com',
        [ema1],
        fail_silently=False)
        return render(request,"home.html")
    return render(request,"event.html")