from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from home.models import Person


def create_person(request, name, lastname, age, email):
    guy = Person(name=name, last_name=lastname, age=age, create=datetime.now(), mail=email)
    guy.save()
    template = loader.get_template('create_person.html')
    document = template.render({'person': guy})
    return HttpResponse(document)


def get_persons(request):
    guys = Person.objects.all()
    template = loader.get_template('show_person.html')
    document = template.render({'person': guys})
    return HttpResponse(document)