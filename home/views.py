#from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"

'''
#Вариант с функциями
def home(request):
    return render(request, 'home/home.html')


def contacts(request):
    return render(request, 'contacts.html')
'''


