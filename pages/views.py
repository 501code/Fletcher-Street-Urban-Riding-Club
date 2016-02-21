from django.shortcuts import render
from contact.forms import ContactForm
from site_details.models import SiteDetail
from .models import Page, Section


def index(request):
    form = ContactForm()

    # get site details
    title = SiteDetail.objects.get(key='site_title')
    slogan = SiteDetail.objects.get(key='site_slogan')

    sections = Section.objects.all().filter(visible=True).order_by('order')
    values = {'form': form, 'title': title, 'slogan': slogan, 'sections': sections, 'pages': get_pages(sections)}

    return render(request, 'pages/index.html', values)


def get_pages(sections):

    values = {}
    for this_section in sections:
        section_pages = Page.objects.all().filter(section=this_section)
        if section_pages:
            values[this_section.key] = {'section': this_section, 'content': section_pages}

    return values
