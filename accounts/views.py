from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.mail import send_mail
from Recipe import settings
from django.http import HttpResponse
from django.contrib.auth.models import User


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    if User.is_active:
        emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)

    subject = "Greetings"
    msg = "Congratulations for your success"
    email_from = "settings.EMAIL_HOST_USER"
    to = emails


    # res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    res = send_mail(subject, msg, email_from, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"


'''def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    email_from = "settings.EMAIL_HOST_USER"
    to = "shyamkrishnanpv535@gmail.com"

        #res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    res = send_mail(subject, msg, email_from, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)'''


'''if User.is_active:
    emails = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)
'''


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/accounts/login")





'''class logout(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'logout2.html'

    def logout(request):
        logout(request)
        return HttpResponseRedirect("login")
'''