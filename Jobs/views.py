from django.shortcuts import render
from .models import Job, Myimage


def home(request):
    jobs = Job.objects
    images = Myimage.objects
    for imageurls in images.all():
        myimageurl = imageurls.image.url
    return render(request, 'jobs/index-5.html',{'jobs': jobs,'images':myimageurl})
