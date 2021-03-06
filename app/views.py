from django.shortcuts import render, HttpResponse
from app.models import Event,Participant
from django.core.mail import send_mail
import datetime
import os
from twilio.rest import Client


# home page
def home(request):
    return render(request,"home.html")

# Function for event registration
def event(request):
    if request.method=='POST':              #collecting data if method is post
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
        data.save()                        #saving data into database
        

        # sending mail to event host
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



# Function for participant registration
def part(request):
    c=[]                       # this array will be used to save all event's name in which participant registered
    pars=Participant.objects.all()          #all participant's data

    # coming_events is set of events whose deadline is not gone 
    coming_events=Event.objects.filter(Reg_deadline__gte=datetime.datetime.now())
    if request.method=="POST":
        constrain=0         #this constrain will be set to 1 if participant register more than 1 time in same event
        constrain1=0        #this constrain will be set to 1 if participant leave the field registration type blank
        ername=""           #to store the event name in which participant is trying to register more than 1 time
        pname=request.POST['name1']
        pcontact=request.POST['contact']
        pemail=request.POST['email1']
        for obj in coming_events:           #appending all events which participant selected to register
            
           if request.POST.get(obj.name,False):
               c.append(obj.name)
        for obj1 in pars:                   #checking whether participant registered in same event in past or not
            if pname==obj1.Name:
                for ovj in c:
                    res=obj1.Checked.find(ovj)
                    if res!=-1:
                        c=[]
                        ername=ovj
                        constrain=1
                        break
        if len(c)!=0:         #means if participant don't tick any event to register, then his data will not be saved as it is useless

            ptype1=request.POST.get('type',False)
            
            if(ptype1==False):
                constrain1=1       
            else:
                if(ptype1=="Individual"):
                    people=0
                    ptype='I'
                if(ptype1=="Group"):
                    ptype='G'
                    people=request.POST['people']
                if(ptype1!=False):
                    data1=Participant(Name=pname,Contact=pcontact,Email=pemail,Checked=c,Reg_type=ptype,No_of=people)
                    data1.save()        #saving data if all looks fine

                    # message sending from twilio
                    account_sid = os.environ.get('id')      #id, token is user variable,using os.environ to access it
                    auth_token = os.environ.get('token')
                    client = Client(account_sid, auth_token)
                    b=[]     #all this arrays to store fields of events so we can send nice message
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
                    # adding all registered event's details to message
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
                    if ptype=='G':          #if group is selected, then only send no. of people detail in message
                        msg1=msg1 \
                            +"\nNo. of People : "+ str(people)
                    message = client.messages \
                                    .create(
                                        body=msg1,
                                        from_='+19167131128',
                                        to='+919099696053'     #sending msg to only registered number bacause of trail account
                                    )

                    #mail feature for participant also
                    subject="Participation done suceessfully..."
                    send_mail(subject,msg1,'jangotry123@gmail.com',[pemail],fail_silently=False)
                    return render(request,"home.html")
            
        # con1 context is for constrains and to show error messages on front end
        con1={
            'ername':ername,
            'constrain':constrain,
            'constrain1':constrain1,
            'content': coming_events
        }
        return render(request,"part.html",con1)
        
    context={ 'content': coming_events }
    return render(request,"part.html",context)


# Function for event dashboard
def dashboard(request):
    # ae , be are error perameters
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
        
        for obj in eves:            # authentication
            
            if (str(id1)==str(obj.id)):
                ae=0
                if password==obj.password:
                    final=str(obj.name)     #saving event name for which host is trying to see data of participants
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
                    ans.append(obj)         #appending all participants who has registered in given event

        #this context1 is for error maping on front end  
        context1={
            "ae":ae,
            "be":be,
            "ans":ans,
          
        }
        
        return render(request,"dashboard.html",context1)
    
    return render(request,"dashboard.html")
                    
        
        
        
       


                
