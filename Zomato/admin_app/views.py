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