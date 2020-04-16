from django.http import HttpResponse
from django.shortcuts import render, redirect
from admin_app.forms import AdminLoginForm
from admin_app.models import AdminLogin
from django.contrib import messages

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