from django.shortcuts import render
from .models import Job, Myimage
from datetime import datetime

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def home(request):
    jobs = Job.objects
    images = Myimage.objects
    no_of_months=diff_month(datetime.now(), datetime(2014,7,7))+20
    for imageurls in images.all():
        myimageurl = imageurls.image.url
    return render(request, 'jobs/index-5.html',{'jobs': jobs,'no_of_months':no_of_months})
