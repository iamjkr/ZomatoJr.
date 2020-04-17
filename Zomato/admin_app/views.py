from django.http import HttpResponse
from django.shortcuts import render, redirect
from admin_app.forms import AdminLoginForm
from django.contrib import messages
from admin_app.models import *
from admin_app.forms import *

# Create your views here.
def adminLogin(request):
    if request.method == "POST":
        lform = AdminLoginForm(request.POST)
        if lform.is_valid():
            un = request.POST.get('username')
            ps = request.POST.get('password')
            try:
                AdminLogin.objects.get(username=un, password=ps)
                request.session['status'] = True
                return render(request, 'admin_app/admin_home.html')
            except AdminLogin.DoesNotExist:
                messages.error(request, 'Invalid Details')
                return redirect('admin_login')
        else:
            messages.error(request, 'Invalid')
            redirect('admin_login')
    else:
        lform = AdminLoginForm()
        return render(request, 'admin_app/login.html', {'lform':lform} )


def countryData(request):
    if request.method == 'POST':
        cf = CountryForm(request.POST)
        if cf.is_valid():
            cf.save()
            messages.success(request, 'country successfully saved!! ')
            return redirect('country_data')
        return None
    else:
        return render(request, 'admin_app/country.html', context={'country': Country.objects.all(), "cf": CountryForm})


def stateData(request):
    if request.method == 'POST':
        sf = StateForm(request.POST)
        if sf.is_valid():
            sf.save()
            messages.success(request, 'successfully saved!! ')
            return redirect('state')
        return None
    else:
        return render(request, 'admin_app/state.html', context={'state': State.objects.all(), "sf": StateForm})


def cityData(request):
    if request.method == 'POST':
        cf = CityForm(request.POST)
        if cf.is_valid():
            cf.save()
            messages.success(request, 'successfully saved!! ')
            return redirect('city')
        return None
    else:
        return render(request, 'admin_app/city.html', context={'city': City.objects.all(), "cf": CityForm})


def regionData(request):
    if request.method == 'POST':
        rf = RegionForm(request.POST)
        if rf.is_valid():
            rf.save()
            messages.success(request, 'successfully saved!! ')
            return redirect('region')
        return None
    else:
        return render(request, 'admin_app/region.html', context={'region': Region.objects.all(), "rf": RegionForm})


def restoData(request):
    if request.method == 'POST':
        rtf = RestoCategoryForm(request.POST)
        if rtf.is_valid():
            rtf.save()
            messages.success(request, 'successfully saved!! ')
            return redirect('resto')
        return None
    else:
        return render(request, 'admin_app/resto.html', context={'resto': RestaurantCategory.objects.all(), "rtf": RestoCategoryForm})