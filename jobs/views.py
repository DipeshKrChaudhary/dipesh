from django.shortcuts import render
from django.http import Http404
from .models import Job

def dipesh(request):

    return render(request, 'jobs/dipesh.html')

def home(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/home.html',{'jobs':jobs})

def detail(request, job_id):
    try:
        jobs=Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404('Jobs not found')
    return render(request, 'jobs/detail.html',{'job':jobs})

