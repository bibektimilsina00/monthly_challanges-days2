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
'december':'Learn Django for at least 20 minutes every day'

}


months=list(challenges.keys())

def index(request):
    return render(request,'index.html',{
        'months':months})
    


def months_challanges(request,month):
    return  HttpResponse(
        f"<p>{challenges[month]}</p>"
    )