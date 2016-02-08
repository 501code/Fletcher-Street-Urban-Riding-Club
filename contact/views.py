from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from site_details.models import SiteDetail

def get_name(request):
    if request.method == 'POST':
        # create a from instance and populate with data
        form = ContactForm(request.POST)
        # if form is valid, process
        if form.is_valid():
            # save form data, send email, post thank you
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']

            # get site email address
            try:
                contact_email = SiteDetail.objects.get(key='site_email')[:1]
            except SiteDetail.DoesNotExist:
                contact_email = 'info@501code.org'

            recipients = [contact_email]
            if cc_myself:
                recipients.append(email)

            send_mail(subject, body, email, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
