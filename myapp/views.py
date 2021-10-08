from django.shortcuts import render
from myapp.models import User

def home(request):
    data = User.objects.all()
    return render(request,'home/index.html',{'access_records':data})