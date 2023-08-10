from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


# Create your views here.
def authorization(request):
    return render(
        request,'authorization.html'
    )
def registration(request):
    # text = get_template('registration/registration_email.html')
    # html = get_template('registration/registration_email.html')
    # context = {'username':email,'password': password}
    # subject = 'Регистрация'
    # from_email = 'vm3416294@gmail.com'
    #
    # text_content = text.render(context)
    # html_content = html.render(context)
    #
    # msg = EmailMultiAlternatives(subject,text_content,from_email,[email])
    # msg.attach_alternative(html_content,'text-html')
    # msg.send()
    return render(
        # request,'registration_email.html'
        request,'registration.html'
    )

def index(request):

    return render(
        request,'index.html'
    )