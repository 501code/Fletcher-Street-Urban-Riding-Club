from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    name = forms.CharField(label='Full Names', max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)