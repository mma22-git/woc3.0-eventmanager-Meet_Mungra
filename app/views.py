from django.shortcuts import render, HttpResponse
from app.models import Event,Participant
from django.core.mail import send_mail
import datetime
import os
from twilio.rest import Client


# Create your views here.
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
def part(request):
    c=[]
    
    pars=Participant.objects.all()
    coming_events=Event.objects.filter(Reg_deadline__gte=datetime.datetime.now())
    if request.method=="POST":
        constrain=0
        ername=""
        pname=request.POST['name1']
        pcontact=request.POST['contact']
        pemail=request.POST['email1']
        for obj in coming_events:
            
           if request.POST.get(obj.name,False):
               c.append(obj.name)
        for obj1 in pars:
            if pname==obj1.Name:
                for ovj in c:
                    res=obj1.Checked.find(ovj)
                    if res!=-1:
                        c=[]
                        ername=ovj
                        constrain=1
                        break
        if len(c)!=0:

            ptype1=request.POST.get('type',False)
            if(ptype1=="Individual"):
                people=0
                ptype='I'
            if(ptype1=="Group"):
                ptype='G'
                people=request.POST['people']
            if(ptype1!=False):
                data1=Participant(Name=pname,Contact=pcontact,Email=pemail,Checked=c,Reg_type=ptype,No_of=people)
                data1.save()
            account_sid = os.environ.get('id')
            auth_token = os.environ.get('token')
            client = Client(account_sid, auth_token)
            b=[]
            elocations=[]
            efdates=[]
            etdates =[]
            eftimes=[]
            ettimes=[]
            for obj in coming_events:
                for name in c:
                    if name==obj.name:
                        b.append(obj)
            for obj1 in b:
                elocations.append(obj1.location)
                efdates.append(str(obj1.from_date))
                etdates.append(str(obj1.to_date))
                eftimes.append(str(obj1.from_time))
                ettimes.append(str(obj1.to_time))
            msg1="\nHello "+ pname +". Thank you for Registration.\n"
            for i in range(len(c)):
                
                msg1 = msg1 + "\n\nEvent name : "+ str(c[i])\
                    +"\nLocation : "+ (elocations[i])\
                    +"\nFrom : "+ str(efdates[i])\
                    +"\t"+ str(eftimes[i])\
                    +"\nTo : "\
                    + str(etdates[i])\
                    +"\t"+ str(ettimes[i])\

            
            msg1=msg1 +"\n\nPerson ID: "\
                    +str(data1.id)\
                    +"\nRegistration type: "+ str(ptype1)
            if ptype=='G':
                msg1=msg1 \
                    +"\nNo. of People : "+ str(people)
            message = client.messages \
                            .create(
                                body=msg1,
                                from_='+19167131128',
                                to='+919099696053'
                            )
            return render(request,"home.html")
            

        con1={
            'ername':ername,
            'constrain':constrain,
            'content': coming_events
        }
        return render(request,"part.html",con1)
        
    context={ 'content': coming_events }
    return render(request,"part.html",context)

def dashboard(request):
    ae=0
    be=0
    
    ans=[]
    if request.method=='POST':
        id1=request.POST['ID']
        password=request.POST['password']
        ae=0
        
        be=0
        ans=[]
        final=""
        eves=Event.objects.all()
        pars=Participant.objects.all()
        
        for obj in eves:
            
            if (str(id1)==str(obj.id)):
                ae=0
                if password==obj.password:
                    final=str(obj.name)
                    break
                else:
                    be=1
                    break
            else:
                ae=1
        if ae==0 and be==0:
            for obj in pars:
                m=obj.Checked.find(final)
                if (m!=-1):
                    ans.append(obj)
                   
                    
        
        
        context1={
            "ae":ae,
            "be":be,
            "ans":ans,
          
        }
        
        return render(request,"dashboard.html",context1)
    
    return render(request,"dashboard.html")
        
       


                
