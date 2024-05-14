from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
    # return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            msg = "Error in Login.Please check your credentials."
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
def profile(request):
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('/')