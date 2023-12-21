from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def reserve(request):
    reserve_form = ReservationForm()
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForm()

    context = {
        "form":reserve_form,
    }

    return render(request,"reservation/reservation.html",context)

def about_page(request):
    return render(request, 'reservation/about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('menu')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)