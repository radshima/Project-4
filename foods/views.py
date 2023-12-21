from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def food_list(request):
  food_list = Food.objects.all()
  context = {
    "foods" : food_list
  }
  return render(request,"foods/list.html",context)


def food_detail(request , id):
  food = Food.objects.get(id=id)
  context = {
    "food":food
  }
  return render(request, "foods/detail.html",context)

def menu_page(request):
    foods = Food.objects.all()
    context = {
        "foods": foods
    }
    return render(request, 'foods/menu.html', context)
  
  
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('foods:food_list')  # Redirect to your desired page after login
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'registration/login.html')