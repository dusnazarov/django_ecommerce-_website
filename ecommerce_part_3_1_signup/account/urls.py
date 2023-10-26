from django.urls import path


from . import views

# https://docs.djangoproject.com/en/3.1/topics/auth/default/
# https://ccbv.co.uk/projects/Django/3.0/django.contrib.auth.views/PasswordResetConfirmView/

app_name = 'account'

urlpatterns = [    
    path('register/', views.account_register, name='register'),
    path('acctivate/<slug:uidb64>/<slug:token>', views.account_activate, name='activate'),
    # User dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]