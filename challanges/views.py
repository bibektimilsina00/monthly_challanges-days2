from django.shortcuts import render
from django.http import HttpResponse

challenges  ={
'january':'Eat no meat for the entire month',
'february':'Walk for at least 20 minutes every day',
'march':'Learn Django for at least 20 minutes every day',
'april':'Learn Django for at least 20 minutes every day',
'may':'Learn Django for at least 20 minutes every day',
'june':'Learn Django for at least 20 minutes every day',
'july':'Learn Django for at least 20 minutes every day',
'august':'Learn Django for at least 20 minutes every day',
'september':'Learn Django for at least 20 minutes every day',
'october':'Learn Django for at least 20 minutes every day',
'november':'Learn Django for at least 20 minutes every day',
'december':None

}


months=list(challenges.keys())
# months=['january','february','march','april','may','june','july','august','september','october','november','december']

def index(request):
    return render(request,'index.html',{
        'month_list':months})

 
    


def months_challanges(request,month):
    return render(request,'months.html',{
        'text':challenges[month],
    },)
    
    