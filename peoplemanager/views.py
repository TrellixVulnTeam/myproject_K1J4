from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import StaffDetail, PeopleDetail, StudentDetail

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone # to display date and time as per timezone


# Create your views here.
def corestaff(request):
    peopledetails = PeopleDetail.objects.order_by('id')
    return render(request, "corestaff.html", {'peopledetails': peopledetails})


def person(request):
   return render(request, "person.html", {})


def people(request):
   return render(request, "people.html", {})


def postdcrfellows(request):
   return render(request, "postdcrfellows.html", {})


def researchafellows(request):
   return render(request, "researchafellows.html", {})
   

def students(request):
   return render(request, "students.html", {})


def home(request):
   return render(request, "home.html", {})
   return redirect('home')
