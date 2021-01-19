from django.shortcuts import render, HttpResponse
from app.models import Event
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
        return render(request,"home.html")
    return render(request,"event.html")