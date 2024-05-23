from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Event, Service, EventImage
from django.utils import translation
from django.conf import settings


def index(request):
    template = 'home.html'
    events = Event.objects.all()
    event_name = Event.objects.values_list('event_name', flat=True)

    context = {'events': events, 'event_name': event_name}
    return render(request, template, context)


def consultation(request):
    template = 'Consultation.html'
    consult = Service.objects.filter(title='consultation')
    consult_title = Service.objects.values_list('title', flat=True)

    context = {'consult': consult, 'consult_title': consult_title}
    return render(request, template, context)


def physiotherapy(request):
    template = 'PHYSIOTHERAPIE.html'
    consult = Service.objects.filter(title='physio_therapy')
    consult_title = Service.objects.values_list('title', flat=True)

    context = {'consult': consult, 'consult_title': consult_title}
    return render(request, template, context)


def medecine_generale(request):
    template = 'medecine_generale.html'
    consult = Service.objects.filter(title='MEDEINE GENERALCE')
    consult_title = Service.objects.values_list('title', flat=True)

    context = {'consult': consult, 'consult_title': consult_title}
    return render(request, template, context)


def imagerie_medicale(request):
    template = 'imagerie_medicale.html'
    consult = Service.objects.filter(title='IMAGERIE MEDICALE')
    consult_title = Service.objects.values_list('title', flat=True)

    context = {'consult': consult, 'consult_title': consult_title}
    return render(request, template, context)


def rehabilitation_fonctionnelle(request):
    template = 'rehabilitation_fonctionnelle.html'
    consult = Service.objects.filter(title='REHABILITATION FONCTIONNELLE')
    consult_title = Service.objects.values_list('title', flat=True)

    context = {'consult': consult, 'consult_title': consult_title}
    return render(request, template, context)


def event(request, event_id):
    template = 'event_page.html'
    event_detail = get_object_or_404(Event, id=event_id)
    event_images = EventImage.objects.filter(event=event_detail)

    context = {'event_detail': event_detail, 'event_images': event_images}

    return render(request, template, context)


def your_view(request):
    return render(request, 'home.html')
