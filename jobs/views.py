from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Job,Company

# Create your views here.
def dashboard(request):
    return render(request, "jobs/dashboard.html")

class JobsView(ListView):
    model = Job
    template_name: str = "jobs/jobs.html"
    context_object_name = "jobs"