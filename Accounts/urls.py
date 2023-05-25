from django.urls import path
from Accounts.views import *

urlpatterns=[
    path('register/',UserRegistration.as_view(),name='register'),
    path('login/',UserLogin.as_view(),name='login'),
    path('profile/',UserProfile.as_view(),name='profile'),
    path('changepassword/',UserChangepassword.as_view(),name='changepassword'),
    path('sendresetpasswordemail/',UserPasswordSendEmail.as_view(),name='sendresetpasswordemail'),
    path('reset-password/<uid>/<token>/',ResetPassword.as_view(),name='resetpassword'),
]