from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import SignalCorps
from .models import Communication
from .forms import UserForm

def index(request):
    return render(request,'index.html', {})
@csrf_exempt
def validate_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            if SignalCorps.objects.get(user_name = "redarmy01"):
                return render(request,'home.html')
    else:
        form = UserForm()
    return render(request,'index.html', {'form':form})

def home(request):
    return render(request,'home.html', {})

def profile(request):
    data = SignalCorps.objects.all()
    
    return render(request,'profile.html',{"data":data})

def view_msg(request):
    msg = Communication.objects.all()
    return render(request,'viewMessages.html',{'msg':msg})
                
def log_out(request):
    return render(request,'index.html',{})
