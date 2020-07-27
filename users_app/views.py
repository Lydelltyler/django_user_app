from django.shortcuts import render, HttpResponse, redirect
from .models import Users


def index(request):
    print(request.POST)

    context = {
        "user_info": Users.objects.all()
    }

    return render(request, "index.html", context)

def create(request):
    fName_from_form = request.POST['fName']
    lName_from_form = request.POST['lName']
    email_from_form = request.POST['email']
    age_from_form = request.POST['age']
    Users.objects.create(first_name=fName_from_form, last_name=lName_from_form, email_address=email_from_form, age=age_from_form)
    print(fName_from_form, lName_from_form, email_from_form, age_from_form)
    return redirect('/success_page')

def success(request):
    return render(request, "success.html")
    
def delete(request):
    Users.objects.last().delete()
    return redirect('/')