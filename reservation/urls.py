from django.urls import path
from . import views
app_name = "reservation"

urlpatterns = [
  path('',views.reserve,name="reservation"),
  path('about/', views.about_page, name='about_page'),
  path('accounts/signup/', views.signup, name='signup'),

]