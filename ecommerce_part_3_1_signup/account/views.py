from django.shortcuts import render

from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse





from django.contrib.auth import login

from .forms import RegisterationForm
from .models import UserBase
from .tokens import account_acctivation_token


@login_required
def dashboard(request):
    return render(request, 'account/users/dashboard.html') 
                                 
                  

def account_register(request):   
   
    if request.method == 'POST':
        registerForm = RegisterationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # setup email
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registeration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_acctivation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message) 
            return HttpResponse('Registered successfully and activation sent')       
    else:
        registerForm = RegisterationForm()
    return render(request, 'account/registeration/register.html', {'form':registerForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except:        
        pass
    if user is not None and account_acctivation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')