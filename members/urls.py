from django.urls import path
from .views import login_view, signup_view
from . import views

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    # path('home/', views.home, name='home'),
]
