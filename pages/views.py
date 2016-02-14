from django.shortcuts import render
from contact.forms import ContactForm


def index(request):
    form = ContactForm()
    return render(request, 'pages/index.html', {'form': form})
