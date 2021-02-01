from django.shortcuts import render
from django.views.generic import DetailView
from blog.models import Post, Project

from django.core.mail import send_mail
from django.conf import settings


def index(request):
    post_list = Post.objects.filter(project__name='Strona glowna').order_by('create_date').reverse()
    context_dict = {'posts': post_list}
    return render(request, 'blog/index.html', context_dict)


def solo(request):
    header_list = Post.objects.filter(project__name='Solo', header=True).order_by('create_date').reverse()
    post_list = Post.objects.filter(project__name='Solo', header=False).order_by('create_date').reverse()
    context_dict = {'posts': post_list, 'headers': header_list}
    return render(request, 'blog/solo.html', context_dict)


def bohomaz(request):
    header_list = Post.objects.filter(project__name='Bohomaz', header=True).order_by('create_date').reverse()
    post_list = Post.objects.filter(project__name='Bohomaz', header=False).order_by('create_date').reverse()
    context_dict = {'posts': post_list, 'headers': header_list}
    return render(request, 'blog/bohomaz.html', context_dict)


def petla(request):
    header_list = Post.objects.filter(project__name='Petla', header=True).order_by('create_date').reverse()
    post_list = Post.objects.filter(project__name='Petla', header=False).order_by('create_date').reverse()
    context_dict = {'posts': post_list, 'headers': header_list}
    return render(request, 'blog/petla.html', context_dict)


def kontakt(request):
    if request.method == 'POST':
        email_imie = request.POST['email-imie']
        email_adres = request.POST['email-adres']
        email_text = request.POST['email-text']

        # send an email
        send_mail(
            email_imie + ' - ' + email_adres, # subject
            'Wiadomosc od: ' + email_imie+'\n' + 'Adres email: ' + email_adres +'\n\n' + email_text, # message
            email_adres, # from email
            ['tomidrapaa@gmail.com'], # to email
        )

        return render(request, 'blog/kontakt.html',
                      {'email_imie': email_imie})
    else:
        return render(request, 'blog/kontakt.html', {})
