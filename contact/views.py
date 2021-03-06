from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from site_details.models import SiteDetail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        # create a from instance and populate with data
        form = ContactForm(request.POST)
        # if form is valid, process
        if form.is_valid():
            # get form data
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']

            # save form data
            new_contact = Contact(subject=subject, body=body, name=name, email=email, cc_myself=cc_myself)
            new_contact.save()

            # get site email address
            try:
                contact_email = SiteDetail.objects.get(key='site_email')
            except SiteDetail.DoesNotExist:
                contact_email = 'info@501code.org'

            recipients = [contact_email]
            if cc_myself:
                recipients.append(email)

            # send email
            # send_mail(subject, body, email, recipients)

            # post thank you
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()

    return render(request, 'contact/form.html', {'form': form})
